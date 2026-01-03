import subprocess
import os

def start_mt5_backtest(expert, symbol, timeframe_str, start_date, end_date):
    # 1. Define paths
    mt5_terminal_path = r"C:\Program Files\MetaTrader 5 IC Markets EU\terminal64.exe"
    config_filename = "mt5_backtest_config.ini"
    config_path = os.path.abspath(config_filename)

    # 2. Create the Configuration INI content
    # MT5 requires this specific format to auto-start the tester
    # Model: 0=Every tick, 1=1 Minute OHLC, 2=Open Prices Only
    config_content = f"""
[Tester]
Expert={expert}
Symbol={symbol}
Period={timeframe_str}
FromDate={start_date}
ToDate={end_date}
Model=0
Optimization=0
UseLocal=1
Deposit=10000
Currency=USD
Leverage=1:100
Report=BacktestReport
ReplaceReport=1
ShutdownTerminal=0
Visual=1
"""

    # 3. Write the .ini file to disk
    try:
        with open(config_path, "w") as file:
            file.write(config_content)
        print(f"Configuration file created at: {config_path}")
    except IOError as e:
        print(f"Error writing config file: {e}")
        return

    # 4. Launch MT5 using the /config flag
    # We ONLY pass the config file path. MT5 reads the rest from there.
    command = [
        mt5_terminal_path,
        f"/config:{config_path}"
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
    timeframe = "D1"              # use "D1", "H1", "M15" etc. (Strings are safer for INI files)
    start_date = "2025.12.01"     # Adjusted date (2025 is future, ensured format is YYYY.MM.DD)
    end_date = "2025.12.31"

    start_mt5_backtest(expert_file, symbol, timeframe, start_date, end_date)