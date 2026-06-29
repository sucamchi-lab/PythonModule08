import os
import sys
import site


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix
