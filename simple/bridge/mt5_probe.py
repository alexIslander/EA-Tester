import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def load_env_file(path: Path) -> dict:
    if not path.exists():
        return {}

    values = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key] = value
    return values


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    env_path = repo_root / "simple" / "config" / ".env"
    env_values = load_env_file(env_path)

    def get_setting(name: str) -> str | None:
        return os.environ.get(name) or env_values.get(name)

    terminal_path = get_setting("MT5_TERMINAL_PATH")
    if not terminal_path:
        print(
            "MT5_TERMINAL_PATH is required. Set it in simple/config/.env or as an env var.",
            file=sys.stderr,
        )
        return 2

    login_raw = get_setting("MT5_LOGIN")
    password = get_setting("MT5_PASSWORD")
    server = get_setting("MT5_SERVER")

    kwargs = {"path": terminal_path}
    if login_raw:
        try:
            kwargs["login"] = int(login_raw)
        except ValueError:
            print("MT5_LOGIN must be an integer account id.", file=sys.stderr)
            return 2
    if password:
        kwargs["password"] = password
    if server:
        kwargs["server"] = server

    try:
        import MetaTrader5 as mt5
    except ImportError:
        print("MetaTrader5 package not installed. Install it and retry.", file=sys.stderr)
        return 2

    if not mt5.initialize(**kwargs):
        code, message = mt5.last_error()
        print(f"mt5.initialize() failed: {code} {message}", file=sys.stderr)
        return 1

    try:
        terminal_info = mt5.terminal_info()
        version_info = mt5.version()
        account_info = mt5.account_info()

        proof = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "terminal_path": terminal_path,
            "terminal_info": terminal_info._asdict() if terminal_info else None,
            "version": {
                "version": version_info[0],
                "build": version_info[1],
                "date": version_info[2],
            }
            if version_info
            else None,
            "account_id": account_info.login if account_info else None,
        }

        data_dir = repo_root / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        proof_path = data_dir / "connection-proof.json"
        proof_path.write_text(
            json.dumps(proof, indent=2, sort_keys=True), encoding="utf-8"
        )
        print(f"Connection proof written to {proof_path}")
    finally:
        mt5.shutdown()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
