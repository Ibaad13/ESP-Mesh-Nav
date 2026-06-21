import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# ==========================
# PARAMETERS
# ==========================
DT = 0.05
WORLD_SIZE = 10

MAX_SPEED = 10.0
ACC_GAIN = 2.0
TURN_GAIN = 5.0

# 4 anchor nodes
ANCHORS = np.array([
    [1, 1],
    [9, 1],
    [1, 9],
    [9, 9]
])

# RSSI model params
RSSI_0 = -40      # dBm at 1 meter
PATH_LOSS = 2.0   # free-space approx
RSSI_NOISE_SIGMA = 0.5  # Standard deviation of log-normal shadowing noise (dB)

# EKF matrices
Q = np.diag([0.01, 0.01, 0.05, 0.02, 0.02])
R = np.diag([0.15, 0.15, 0.02])
P = np.eye(5) * 0.5

# State vector [x,y,v,theta,omega]
X = np.array([
    [1.0],
    [1.0],
    [0.0],
    [0.0],
    [0.0]
])

# Ground truth
true_x = 1.0
true_y = 1.0
true_v = 0.0
true_theta = 0.0
true_omega = 0.0

target_x = true_x
target_y = true_y

# ==========================
# EKF
# ==========================
def predict(X, P, accel):
    x = X[0,0]
    y = X[1,0]
    v = X[2,0]
    theta = X[3,0]
    omega = X[4,0]

    X_pred = np.array([
        [x + v*np.cos(theta)*DT],
        [y + v*np.sin(theta)*DT],
        [v + accel*DT],
        [theta + omega*DT],
        [omega]
    ])

    F = np.array([
        [1,0,np.cos(theta)*DT,-v*np.sin(theta)*DT,0],
        [0,1,np.sin(theta)*DT, v*np.cos(theta)*DT,0],
        [0,0,1,0,0],
        [0,0,0,1,DT],
        [0,0,0,0,1]
    ])

    P_pred = F @ P @ F.T + Q
    return X_pred, P_pred


def update(X_pred, P_pred, measurement):
    H = np.array([
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,0,0,1,0]
    ])

    z_pred = np.array([
        [X_pred[0,0]],
        [X_pred[1,0]],
        [X_pred[3,0]]
    ])

    residual = measurement - z_pred

    S = H @ P_pred @ H.T + R
    K = P_pred @ H.T @ np.linalg.inv(S)

    X_new = X_pred + K @ residual
    I = np.eye(5)
    P_new = (I - K @ H) @ P_pred

    return X_new, P_new


# ==========================
# ROBOT SIM
# ==========================
def simulate_robot():
    global true_x, true_y, true_v, true_theta, true_omega

    dx = target_x - true_x
    dy = target_y - true_y
    dist = np.sqrt(dx**2 + dy**2)

    if dist < 0.05:
        true_v = 0
        true_omega = 0
        return 0.0

    desired_theta = np.arctan2(dy, dx)
    angle_error = desired_theta - true_theta

    while angle_error > np.pi:
        angle_error -= 2*np.pi
    while angle_error < -np.pi:
        angle_error += 2*np.pi

    true_omega = TURN_GAIN * angle_error
    accel = ACC_GAIN * (min(MAX_SPEED, dist) - true_v)

    true_v += accel * DT
    true_theta += true_omega * DT

    true_x += true_v*np.cos(true_theta)*DT
    true_y += true_v*np.sin(true_theta)*DT

    return accel


# ==========================
# RSSI + TRILATERATION
# ==========================
def distance_to_rssi(d):
    d = max(d, 0.1)
    noise = np.random.normal(0, RSSI_NOISE_SIGMA)
    return RSSI_0 - 10 * PATH_LOSS * np.log10(d) + noise


def rssi_to_distance(rssi):
    return 10 ** ((RSSI_0 - rssi) / (10 * PATH_LOSS))


def trilateration(distances):
    x1, y1 = ANCHORS[0]
    d1 = distances[0]

    A = []
    b = []

    for i in range(1, len(ANCHORS)):
        xi, yi = ANCHORS[i]
        di = distances[i]

        A.append([
            2*(xi-x1),
            2*(yi-y1)
        ])

        b.append(
            d1**2 - di**2
            - x1**2 + xi**2
            - y1**2 + yi**2
        )

    A = np.array(A)
    b = np.array(b)

    pos, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    return pos[0], pos[1]


def get_measurements():
    distances = []
    rssis = []

    for ax, ay in ANCHORS:
        d = np.sqrt((true_x-ax)**2 + (true_y-ay)**2)
        distances.append(d)

    for d in distances:
        rssis.append(distance_to_rssi(d))

    estimated_distances = [rssi_to_distance(r) for r in rssis]

    trilat_x, trilat_y = trilateration(estimated_distances)

    mag_theta = true_theta + np.random.normal(0, 0.03)

    z = np.array([
        [trilat_x],
        [trilat_y],
        [mag_theta]
    ])

    return z


# ==========================
# GUI
# ==========================
root = tk.Tk()
root.title("Indoor Navigation EKF")

fig = Figure(figsize=(12, 5), dpi=100)
ax_ekf = fig.add_subplot(121)
ax_true = fig.add_subplot(122)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

state_label = tk.Label(root, font=("Courier", 12), justify="left")
state_label.pack()


def setup_axes():
    for ax in [ax_ekf, ax_true]:
        ax.clear()
        ax.set_xlim(0, WORLD_SIZE)
        ax.set_ylim(0, WORLD_SIZE)
        ax.grid(True)

        for px, py in ANCHORS:
            ax.scatter(px, py, s=120, marker='s')
            ax.text(px+0.1, py+0.1, f"N({px},{py})")

    ax_ekf.set_title("EKF Estimate")
    ax_true.set_title("Ground Truth")


def onclick(event):
    global target_x, target_y
    if event.inaxes == ax_true:
        target_x = event.xdata
        target_y = event.ydata


canvas.mpl_connect("button_press_event", onclick)


def animate():
    global X, P

    accel = simulate_robot()
    measurement = get_measurements()

    X_pred, P_pred = predict(X, P, accel)
    X, P = update(X_pred, P_pred, measurement)

    setup_axes()

    # Ground truth plot
    ax_true.scatter(true_x, true_y, c='red', s=120)
    
    # Replaced target circle with a red cross ('x')
    ax_true.scatter(target_x, target_y, c='red', s=100, marker='x', linewidths=2)

    ax_true.text(
        true_x+0.2, true_y+0.2,
        f"({true_x:.2f}, {true_y:.2f})"
    )

    # EKF plot
    ax_ekf.scatter(X[0,0], X[1,0], c='blue', s=120)

    ax_ekf.text(
        X[0,0]+0.2, X[1,0]+0.2,
        f"({X[0,0]:.2f}, {X[1,0]:.2f})"
    )

    state_text = (
        f"EKF STATE\n"
        f"x     = {X[0,0]:.3f}\n"
        f"y     = {X[1,0]:.3f}\n"
        f"v     = {X[2,0]:.3f}\n"
        f"theta = {X[3,0]:.3f} rad\n"
        f"omega = {X[4,0]:.3f} rad/s"
    )
    state_label.config(text=state_text)

    canvas.draw()
    root.after(int(DT*1000), animate)


setup_axes()
animate()
root.mainloop()