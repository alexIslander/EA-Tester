# EA Tester

[![Release][github-release-image]][github-release-link]
[![License][license-image]][license-link]
[![AppVeyor][appveyor-ci-build-image]][appveyor-ci-build-link]
[![Status][gha-image-check-master]][gha-link-check-master]
[![Status][gha-image-lint-master]][gha-link-lint-master]
[![Status][gha-image-shell-master]][gha-link-shell-master]
[![Status][gha-image-mql-master]][gha-link-mql-master]
[![Discuss][gh-discuss-badge]][gh-discuss-link]
[![Channel][tg-channel-image]][tg-channel-link]
[![Twitter][twitter-image]][twitter-link]
[![Edit Code][gitpod-image]][gitpod-link]

## About

Headless Forex backtesting for MetaTrader platform using Docker.

## Usage

The easiest way is to [install Docker](https://www.docker.com/get-started), then run tester from the terminal:

```shell
docker run ea31337/ea-tester help
```

to list available commands.

### Backtesting

Here is the example command for running backtest on MACD using historical data from 2019:

```shell
docker run ea31337/ea-tester run_backtest -e MACD -y 2019 -v -t
```

To backtest EA31337 bot, check: [Backtesting using Docker](https://github.com/EA31337/EA31337/wiki/Backtesting-using-Docker).

### CLI options

Check [`scripts/options.txt`](scripts/options.txt) file for supported parameters and variables.

### Support

- For help, open a [new discussion][gh-discuss-link] to ask questions.
- For bugs/features, raise a [new issue at GitHub][gh-issues].
- Join our [Telegram channel][tg-channel-link] for news and discussion group for help.

<!-- Named links -->

[github-release-image]: https://img.shields.io/github/release/EA31337/EA-Tester.svg?logo=github
[github-release-link]: https://github.com/EA31337/EA-Tester/releases

[twitter-image]: https://img.shields.io/badge/EA31337-Follow-1DA1F2.svg?logo=Twitter
[twitter-link]: https://twitter.com/EA31337

[gh-discuss-badge]: https://img.shields.io/badge/Discussions-Q&A-blue.svg?logo=github
[gh-discuss-link]: https://github.com/EA31337/EA-Tester/discussions
[gh-issues]: https://github.com/EA31337/EA-Tester/issues

[license-image]: https://img.shields.io/github/license/EA31337/EA-Tester.svg
[license-link]: https://tldrlegal.com/license/mit-license

[appveyor-ci-build-link]: https://ci.appveyor.com/project/kenorb/ea-tester/branch/master
[appveyor-ci-build-image]: https://ci.appveyor.com/api/projects/status/r4g7ughqovcv5ph5/branch/master?svg=true

[gha-link-check-master]: https://github.com/EA31337/EA-Tester/actions?query=workflow%3ACheck+branch%3Amaster
[gha-image-check-master]: https://github.com/EA31337/EA-Tester/workflows/Check/badge.svg

[gha-link-lint-master]: https://github.com/EA31337/EA-Tester/actions?query=workflow%3ALint+branch%3Amaster
[gha-image-lint-master]: https://github.com/EA31337/EA-Tester/workflows/Lint/badge.svg

[gha-link-shell-master]: https://github.com/EA31337/EA-Tester/actions?query=workflow%3ATests-Shell+branch%3Amaster
[gha-image-shell-master]: https://github.com/EA31337/EA-Tester/workflows/Tests-Shell/badge.svg

[gha-link-mql-master]: https://github.com/EA31337/EA-Tester/actions?query=workflow%3ATests-MQL+branch%3Amaster
[gha-image-mql-master]: https://github.com/EA31337/EA-Tester/workflows/Tests-MQL/badge.svg

[tg-channel-image]: https://img.shields.io/badge/Telegram-join-0088CC.svg?logo=telegram
[tg-channel-link]: https://t.me/EA31337

[gitpod-image]: https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod
[gitpod-link]: https://gitpod.io/#https://github.com/EA31337/EA-Tester
Here is a clean, professional `README.md` file based on our successful Windows setup. You can drop this into your `D:\Workspace\2025\EA-Tester\simple` folder for future reference.

---

# 🚀 MT5 Backtest Runner (Windows Setup)

This project automates MetaTrader 5 backtesting using Python. Because MT5 is a native Windows application, this workflow is designed to run in **PowerShell** rather than WSL or Docker.

## 📋 Prerequisites

* **Windows 10/11**
* **Python 3.11** (Check with `py -0p`)
* **MetaTrader 5** installed at `C:\Program Files\MetaTrader 5 IC Markets EU\`

---

## 🛠️ One-Time Setup

Before running the script for the first time, you must enable script execution in PowerShell and create your Windows-native virtual environment.

### 1. Enable PowerShell Scripts

Open PowerShell and run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

```

*Type `Y` when prompted.*

### 2. Create Virtual Environment

```powershell
py -m venv venv_win

```

### 3. Install Dependencies

```powershell
.\venv_win\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

```

---

## 🏃 How to Run the Backtest

Always run these commands from the project root (`D:\Workspace\2025\EA-Tester\simple`):

1. **Activate Environment:**
```powershell
.\venv_win\Scripts\Activate.ps1

```


2. **Execute Script:**
```powershell
python bridge/mt5_backtest_working.py

```



---

## 🔍 Troubleshooting

### "File Not Found" for terminal64.exe

Ensure the path in `mt5_backtest_working.py` matches your installation:

```python
mt5_terminal_path = r"C:\Program Files\MetaTrader 5 IC Markets EU\terminal64.exe"

```

### Script Execution Error

If you see an "UnauthorizedAccess" error, repeat the `Set-ExecutionPolicy` command in **Step 1** of the Setup.

### Python Path Errors

If `python` is not recognized, use the Windows Python Launcher:

```powershell
py bridge/mt5_backtest_working.py

```

---

**Would you like me to also create a `run_backtest.ps1` file for you, so you can just double-click a shortcut to launch the whole process?**

## Result

```bash
PS D:\Workspace\2025\EA-Tester\simple> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
PS D:\Workspace\2025\EA-Tester\simple> .\venv_win\Scripts\Activate.ps1
(venv_win) PS D:\Workspace\2025\EA-Tester\simple> python bridge/mt5_backtest_working.py
Using existing configuration file: D:\Workspace\2025\EA-Tester\simple\config\Dark.Moon.MT5.EURUSD.M15.ini
Launching MT5 with command: ['C:\\Program Files\\MetaTrader 5 IC Markets EU\\terminal64.exe', '/config:D:\\Workspace\\2025\\EA-Tester\\simple\\config\\Dark.Moon.MT5.EURUSD.M15.ini', '/report:D:\\Workspace\\2025\\EA-Tester\\data\\reports\\backtest_report_20260128_183300.html', '/export:D:\\Workspace\\2025\\EA-Tester\\data\\reports\\backtest_metrics_20260128_183300.csv']
MT5 launched. The backtest should start automatically.
```