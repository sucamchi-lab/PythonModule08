"""
loading.py — Matrix Data Analysis Tool
=======================================
Demonstrates package management with pip and Poetry.

This program simulates Matrix data using numpy, analyzes it with pandas,
and generates visualizations with matplotlib. It showcases proper dependency
management by checking for required packages and providing installation
instructions for both pip and Poetry.
"""

import sys


# ── Dependency check ───────────────────────────────────────

def check_dependencies():
    """Check if required packages are installed and report their versions."""
    packages = [
        ("numpy",   "Numerical computation"),
        ("pandas",     "Data manipulation"),
        ("matplotlib",  "Visualization"),
    ]

    available = {}
    missing = []

    for pkg_name, purpose in packages:
        try:
            pkg = __import__(pkg_name)
            ver = getattr(pkg, "__version__", "unknown")
            available[pkg_name] = (ver, purpose)
            print(f"  [OK] {pkg_name} ({ver}) - {purpose} ready")
        except ImportError:
            missing.append(pkg_name)
            print(f"  [FAIL] {pkg_name} - {purpose} NOT INSTALLED")

    return available, missing


# ── Installation guide ──────────────────────────────────────

INSTALL_GUIDE = r"""
┌────────────────────────────────────────────────────────────┐
│                   INSTALLATION GUIDE                       │
├────────────────────────────────────────────────────────────┤
│                                                           │
│  Option 1: Using pip                                      │
│    $ pip install -r requirements.txt                      │
│    $ python3 loading.py                                   │
│                                                           │
│  Option 2: Using Poetry                                   │
│    $ poetry install                                       │
│    $ poetry run python loading.py                         │
│                                                           │
│  pip:    Installs packages globally or in active venv     │
│          Uses requirements.txt for flat listing           │
│                                                           │
│  Poetry: Creates isolated environment automatically       │
│          Uses pyproject.toml with metadata & versions     │
│          Locks exact deps in poetry.lock                  │
└───────────────────────────────────────────────────────────┘
"""


# ── Data analysis & visualisation ───────────────────────────

def run_analysis():
    import numpy
    import pandas
    import matplotlib
    import matplotlib.pyplot as plot

    print("\nAnalyzing Matrix data...")

    # Generate data with numpy
    x = numpy.linspace(0, 10, 50)
    y = numpy.sin(x) + numpy.random.normal(0, 0.2, 50)

    # Build a DataFrame with pandas
    df = pandas.DataFrame({"x": x, "y": y})
    print(df.describe())

    # Simple plot with matplotlib
    plot.figure(figsize=(8, 4))
    plot.plot(df["x"].to_numpy(), df["y"].to_numpy(), "g-", linewidth=1.5)
    plot.title("Matrix Data — Sine Wave with Noise")
    plot.xlabel("Time")
    plot.ylabel("Amplitude")
    plot.grid(True, alpha=0.3)
    out = "matrix_analysis.png"
    plot.savefig(out)
    plot.close()

    print(f"\nVisualization saved to: {out}")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    _, missing = check_dependencies()

    if missing:
        print("\n  Some dependencies are missing.")
        print(INSTALL_GUIDE)
        sys.exit(1)

    run_analysis()
