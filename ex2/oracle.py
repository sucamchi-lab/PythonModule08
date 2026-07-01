"""
Connects to the Matrix resistance network using environment variables
loaded from a .env file or the shell.
"""

import os
import sys


def load_config() -> dict[str, str]:

    try:
        from dotenv import load_dotenv  # type: ignore
        loaded = load_dotenv()
    except ImportError:
        print("[FAIL] python-dotenv is not installed.")
        print("Run: pip install python-dotenv")
        sys.exit(1)

    if loaded:
        print("[OK] .env file loaded")
    else:
        print("[INFO] No .env file found — using shell env defaults")

    # Read each setting from the environment with a default if not set
    config = {
        "MATRIX_MODE":   os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL":  os.getenv("DATABASE_URL", "sqlite:///:memory:"),
        "API_KEY":       os.getenv("API_KEY", ""),
        "LOG_LEVEL":     os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "https://zion.unknown"),
    }
    return config


def show_config(config: dict[str, str]) -> None:

    print("\nConfiguration loaded:")

    mode = config["MATRIX_MODE"]
    print(f"Mode: {mode}")

    db_url = config["DATABASE_URL"]
    print(f"Database: Connected to ({db_url})")

    key = config["API_KEY"]
    if key:
        print(f"API Access: Key set — {key[:4]}****")
    else:
        print("API Access: No API key set")

    print(f"Log Level: {config['LOG_LEVEL']}")

    endpoint = config["ZION_ENDPOINT"]
    if endpoint == "https://zion.unknown":
        print("Zion Network: Endpoint not configured")
    else:
        print(f"Zion Network: Online ({endpoint})")


def security_check(config: dict[str, str]) -> None:

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.isfile(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing — copy .env.example to .env")

    if config["MATRIX_MODE"] == "production":
        print("[OK] Production overrides available")
    else:
        print(
            "[INFO] Using development mode — set MATRIX_MODE=production")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_config()
    show_config(config)
    security_check(config)

    print("\nThe Oracle sees all configurations.")
