# Docs

Supporting documentation, media, and result captures referenced from the main [README](../README.md).

- [`report/`](report) — The full EKF derivation document (the mathematical model underlying Phase 2), in both `.docx` and `.pdf` form.
- [`media/`](media) — Images and video used directly in the README: the system architecture diagram, the hardware photo, the Fusion 360 render, and the EKF simulation video + thumbnail.
- [`results/`](results) — Raw result captures from Phase 1 testing:
  - [`phase1_static/`](results/phase1_static) — three captures of the visualization with the robot held stationary, used to illustrate baseline RSSI noise.
  - [`phase1_dynamic/`](results/phase1_dynamic) — eight captures of the visualization as the robot moved from access point 1 to access point 2, used to confirm the position estimate tracks real motion.

### Adding the EKF simulation video to GitHub

GitHub renders `.mp4` files natively when they're uploaded directly through the GitHub web UI (drag-and-drop into a Markdown file editor, an Issue, or a Release) — GitHub then hosts the file on its own CDN and gives you a URL to paste into the README. A `.mp4` committed via `git push` alone will **not** auto-embed as a player; it just shows as a downloadable binary. So for the video specifically:

1. Open `README.md` in the GitHub web editor (or open a new Issue — either works for generating the link).
2. Drag `ekf_simulation_demo.mp4` into the text box.
3. GitHub uploads it and inserts a `https://github.com/user-attachments/...` link automatically.
4. Copy that generated link and replace the placeholder `docs/media/ekf_simulation_demo.mp4` path in the README with it.

Alternatively, attach the video to a GitHub Release and link to it from the README — same effect, and keeps large binaries out of the main git history.
