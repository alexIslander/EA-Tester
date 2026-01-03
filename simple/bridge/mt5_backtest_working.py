import subprocess
import os
from datetime import datetime
from pathlib import Path

def start_mt5_backtest(expert, symbol, timeframe_str, start_date, end_date, config_ini=None):
    # 1. Define paths
    mt5_terminal_path = r"C:\Program Files\MetaTrader 5 IC Markets EU\terminal64.exe"
    
    # Logic to determine configuration source
    config_path = ""
    repo_root = Path(__file__).resolve().parents[2]
    config_config = repo_root / "simple" / "config" / config_ini
    data_dir = repo_root / "data"
    reports_dir = data_dir / "reports"
    # reports_dir.mkdir(parents=True, exist_ok=True)

    # Generate a unique timestamp for the report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_path = reports_dir / f"backtest_report_{timestamp}.html"
    csv_path = reports_dir / f"backtest_metrics_{timestamp}.csv"
    # csv_path = os.path.abspath("data/reports/backtest_metrics_{timestamp}.csv")
    # Case A: An existing config file is provided
    if config_ini:
        # Check if the file exists (handles full paths or relative paths like 'config/settings.ini')
        if os.path.exists(config_ini):
            print(f"Using existing configuration file: {config_ini}")
            config_path = os.path.abspath(config_ini)
        else:
            print(f"ERROR: The provided config file '{config_ini}' was not found.")
            return

    # 4. Launch MT5 using the /config flag
    # We ONLY pass the config file path. MT5 reads the rest from there.
    command = [
        mt5_terminal_path,
        f"/config:{config_path}",
        f"/report:{html_path}",
        f"/export:{csv_path}"
    ]

    print(f"Launching MT5 with command: {command}")
    
    try:
        subprocess.Popen(command)
        print("MT5 launched. The backtest should start automatically.")
    except Exception as e:
        print(f"Failed to launch MT5: {e}")

if __name__ == "__main__":
    # Settings
    expert_file = "DarkMoon.ex5"  # Ensure this matches exactly what is in your MQL5/Experts folder
    symbol = "EURUSD"
    timeframe = "M15"             # use "D1", "H1", "M15" etc.
    start_date = "2025.12.01"     # Adjusted date
    end_date = "2025.12.31"
    
    # --- usage scenarios ---

    # Scenario 2: Use an existing file from a config folder (Uncomment to test)
    repo_root = Path(__file__).resolve().parents[2]
    custom_config = repo_root / "simple" / "config" / "Dark.Moon.MT5.EURUSD.M15.ini"
    data_dir = repo_root / "data"
    reports_dir = data_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    # print("\n--- Scenario 2: Using Custom Config ---")
    # custom_config = "config/Dark.Moon.MT5.EURUSD.M15.ini"
    start_mt5_backtest(expert_file, symbol, timeframe, start_date, end_date, config_ini=custom_config)