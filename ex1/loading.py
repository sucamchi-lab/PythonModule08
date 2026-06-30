"""
Demonstrates package management with pip and Poetry.

This program simulates data using numpy, analyzes it with pandas,
and generates visualizations with matplotlib. It showcases proper dependency
management by checking for required packages and providing installation
instructions for both pip and Poetry.
"""

import sys


INSTALL_GUIDE = r"""
┌───────────────────────────────────────────────────────────┐
│                   INSTALLATION GUIDE                      │
├───────────────────────────────────────────────────────────┤
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


def check_dependencies() -> list[str]:

    packages = ["numpy", "pandas", "matplotlib"]
    missing = []

    for package in packages:
        try:
            __import__(package)
            print(f"  [OK] {package}")
        except ImportError:
            missing.append(package)
            print(f"  [FAIL] {package}")

    return missing


def run_analysis() -> None:

    print("\nRolling two 6-sided dice 100 times...")
    import numpy
    import pandas  # type: ignore
    import matplotlib.pyplot as plot  # type: ignore

    # Roll two dice 100 times using numpy
    die1 = numpy.random.randint(1, 7, size=100)
    die2 = numpy.random.randint(1, 7, size=100)
    sum = die1 + die2

    # Build a DataFrame with pandas
    df = pandas.DataFrame({"Die1": die1, "Die2": die2, "Sum": sum})
    counts = df["Sum"].value_counts().sort_index()

    # Bar chart with matplotlib
    counts.plot(kind="bar", color="steelblue", edgecolor="black")
    plot.title("Sum of Two 6-Sided Dice (100 rolls)")
    plot.xlabel("Sum")
    plot.ylabel("Frequency")
    plot.xticks(rotation=0)
    plot.yticks(range(0, int(counts.max()) + 1))
    out = "matrix_analysis.png"
    plot.savefig(out)
    plot.close()

    print("\nAnalysis complete!")
    print(f"Bar chart saved to: {out}")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    missing = check_dependencies()

    if missing:
        print("\n  Some dependencies are missing.")
        print(INSTALL_GUIDE)
        sys.exit(1)

    run_analysis()
