# Hardware

CAD design and reference images for the robot chassis.

- [`fusion360/`](fusion360) — Native Fusion 360 design file(s) and/or exported `.step`/`.stl` files for the two-tier acrylic chassis (The files are not available yet, I plan to upload them once my project is completed)
- [`images/`](images) — Rendered views of the CAD model, for use in documentation (the `docs/media/fusion360_render.png` shown in the main README is a copy/export of one of these).

### Bill of materials (summary)

| Part | Qty | Notes |
|---|---|---|
| Acrylic deck plates | 3 | Laser-cut, two-tier standoff design |
| Metal standoffs | 4-8 | Connects upper and lower decks |
| DC gear motors | 2–4 | Drive wheels |
| Motor driver | 1 | Driven from robot ESP32 |
| ESP32 dev board | 1 (this bot) + 1 master + N access points | See [`firmware/`](../firmware) |
| IMU module | 1 | Added in Phase 2 for EKF fusion |
| Perfboard / protoboard | 1–2 | Power distribution and wiring breakout |

