# Software

Host-side (laptop) Python code, split by project phase.

- [`phase1_visualization/`](phase1_visualization) — RSSI-to-distance conversion, trilateration solver, and the live matplotlib visualization used for the Phase 1 results in the main README. (Files not available yet)
- [`phase2_ekf_fusion/`](phase2_ekf_fusion) — Extended Kalman Filter implementation fusing RSSI-derived position with IMU data, currently validated in simulation (see [`docs/report/`](../docs/report) for the full derivation this code implements).

Each subfolder has its own `requirements.txt`. Recommended: use a virtual environment per subfolder, or one shared environment with the union of both requirements files if you're actively working across both phases.

```bash
python -m venv venv
source venv/bin/activate   # venv\Scripts\activate on Windows
pip install -r phase1_visualization/requirements.txt
pip install -r phase2_ekf_fusion/requirements.txt
```
