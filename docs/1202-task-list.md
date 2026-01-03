# New Simple Way Task List

Status legend: [ ] todo, [~] in progress, [x] done

## Tasks
- [ ] T1 Connect to MT5 and prove the bridge works
  - Use MT5 terminal path: C:\Program Files\MetaTrader 5 IC Markets EU\terminal64.exe
  - Deliverables: `simple/bridge/mt5_probe.py`, `simple/config/.env.example`, `data/connection-proof.json`
  - Proof: `mt5.initialize()` succeeds and connection proof file is written

- [ ] T2 Initiate a manual backtest from this repo (KISS)
  - Provide a repo command or script that launches MT5 and points to the right config
  - Save HTML report to `data/reports/`

- [ ] T3 Parse HTML report (host)
  - Deliverable: `simple/analysis/parse_report.py`
  - Output: key metrics (net profit, drawdown, trade count)

- [ ] T4 Dockerize the analysis
  - Deliverable: `simple/analysis/Dockerfile`
  - Container reads `data/reports/` and prints the same metrics as host

- [ ] T5 Cross-platform notes
  - Document Windows vs Linux paths and volume mounts

- [ ] T6 Optional automation (later)
  - Headless backtest via MT5 CLI or UI automation
  - Keep disabled until asked
