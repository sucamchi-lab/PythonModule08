import os
import sys
import site


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    if is_in_venv():
        print("MATRIX STATUS: Welcome to the construct!")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("Package installation path:")
        print(f"{site.getsitepackages()[0]}")

    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print()
        print("python3 -m venv .venv")
        print("source .venv/bin/activate")
        print()
        print("Then run this program again.")
