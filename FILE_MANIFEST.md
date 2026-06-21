# File manifest — what to name your files and where to put them

This document is your checklist. I've already built the repo skeleton, the `README.md`, the EKF derivation (doc + PDF), the hardware photo, and the architecture diagram — those are done and already placed correctly. Everything below is what **you** still need to drop in, named exactly as shown, so every link and image in the README resolves correctly on GitHub.

Legend: ✅ = already done for you · ⬜ = you need to add this

> **Note on `.gitkeep` files:** you'll notice empty-looking folders contain a file called `.gitkeep`. Git doesn't track empty folders at all, so this is a standard trick to make the folder show up once you push to GitHub. **Once you add your real file to that folder, delete the `.gitkeep`** — it's just a placeholder.

---

## 1. `docs/media/` — core visuals used directly in the README

| Filename (exact) | What it is | Status |
|---|---|---|
| `system_architecture_diagram.png` | Architecture diagram (AP nodes → robot → master → laptop) | ✅ Generated for you |
| `bot_hardware_photo.png` | Photo of the assembled robot | ✅ Placed from your upload |
| `fusion360_render.png` | A render/screenshot from your Fusion 360 model | ⬜ Export a PNG from Fusion 360 (File → Export, or just a screenshot of the model view) and save it with this exact name |
| `ekf_simulation_demo.mp4` | Your EKF simulation video | ⬜ **Do not just commit this with `git push`** — see the note below. Upload it through the GitHub web UI to get an embeddable link, then update the README link |
| `ekf_simulation_thumbnail.png` | A single still frame from the simulation video, used as the clickable thumbnail | ⬜ Grab one frame from your video (e.g. via `ffmpeg -i ekf_simulation_demo.mp4 -frames:v 1 -ss 00:00:02 ekf_simulation_thumbnail.png`, or just a screenshot of the video paused on a good frame) |

### Important — about the video specifically

GitHub does **not** auto-embed `.mp4` files just because they exist in your repo folder. To get a playable inline video in your README, you must upload it through the **GitHub web interface** (drag it into the README editor on github.com, or into a new Issue) — GitHub will host it on its CDN and hand you back a link like `https://github.com/user-attachments/assets/...`. Paste that link into the README in place of `docs/media/ekf_simulation_demo.mp4`. Full instructions are already written out for you in [`docs/README.md`](docs/README.md).

---

## 2. `docs/results/phase1_static/` — your 3 static-test screenshots

| Filename (exact) |
|---|
| `static_capture_01.png` |
| `static_capture_02.png` |
| `static_capture_03.png` |

⬜ Rename your 3 static-robot visualization screenshots to these exact names, in whatever order you captured them, and place them in this folder.

---

## 3. `docs/results/phase1_dynamic/` — your 8 motion-test screenshots

| Filename (exact) |
|---|
| `motion_capture_01.png` |
| `motion_capture_02.png` |
| `motion_capture_03.png` |
| `motion_capture_04.png` |
| `motion_capture_05.png` |
| `motion_capture_06.png` |
| `motion_capture_07.png` |
| `motion_capture_08.png` |

⬜ Rename your 8 motion-test visualization screenshots to these exact names, **in chronological order** (01 = robot near AP1, 08 = robot near AP2), and place them in this folder.

---

## 4. `hardware/fusion360/` — your CAD source

| Filename | Notes |
|---|---|
| `chassis_design.f3d` (or `.step` / `.stl`) | ⬜ Export your Fusion 360 design and place it here. If you'd rather not share the native `.f3d`, exporting to `.step` (editable) or `.stl` (print-only) is a fine substitute — just update the filename reference in `README.md`'s repo-structure tree if you change the extension |

## 5. `hardware/images/`

| Filename | Notes |
|---|---|
| `fusion360_render_full.png` | ⬜ Optional: a higher-res or alternate-angle render than the one in `docs/media/`, if you have one. Not strictly required — `docs/media/fusion360_render.png` is the one actually shown in the README |

---

## 6. `firmware/` — your three `.ino` files

| Path (exact) | Content |
|---|---|
| `firmware/access_point_node/access_point_node.ino` | ⬜ Your access-point ESP32 code |
| `firmware/robot_node/robot_node.ino` | ⬜ Your robot-side ESP32 code (RSSI scanning + ESP-NOW send, and later IMU read) |
| `firmware/master_node/master_node.ino` | ⬜ Your master ESP32 code (ESP-NOW receive + serial bridge) |

If your actual sketch files have different internal names, that's fine — just rename the `.ino` file itself to match the folder (Arduino requires the `.ino` filename to match its parent folder name) and keep the rest of the code as-is.

---

## 7. `software/phase1_visualization/` — your Phase 1 Python code

| Filename (exact) | Content |
|---|---|
| `trilateration_visualizer.py` | ⬜ Your Python script that reads serial RSSI data, converts to distance, trilaterates, and plots live |
| `requirements.txt` | ✅ Already created — double check it matches the actual packages your script imports (e.g. add `pandas` if you use it) |

---

## 8. `software/phase2_ekf_fusion/` — your EKF code

| Filename (exact) | Content |
|---|---|
| `ekf_simulation.py` | ⬜ Your EKF simulation script |
| `requirements.txt` | ✅ Already created — double check against your actual imports |
| `results/` | ⬜ Optional: if your simulation saves any output plots (e.g. estimated vs. true trajectory), drop them here. If you add any, list them in the README's Phase 2 section too |

---

## 9. Things to personalize before publishing

- [ ] Replace `[Your Name]` in `README.md` (Author section) and `LICENSE` (copyright line) with your actual name
- [ ] Add your email/LinkedIn in the Author section if you want professors to be able to reach you directly
- [ ] Double check the AP SSIDs / coordinates mentioned generically in the firmware README match what you actually used
- [ ] If your access point count wasn't 3, adjust "AP node N" language in the README/diagram description as needed (the diagram already uses "AP node 1, 2, N" to stay generic)

---

## Quick copy-paste setup (once you have all files renamed)

```bash
git init
git add .
git commit -m "Initial commit: ESP-Mesh-Nav — RSSI trilateration + EKF sensor fusion"
git branch -M main
git remote add origin https://github.com/<your-username>/ESP-Mesh-Nav.git
git push -u origin main
```

Then go back into the GitHub web UI specifically to upload the `.mp4` (see section 1) and patch that one link in the README afterward.
