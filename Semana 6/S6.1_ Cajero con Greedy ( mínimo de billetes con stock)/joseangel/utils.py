# utils.py — utilidades de E/S
from typing import Optional, Iterable

def open_test_file(test_file: Optional[str]) -> Iterable[str]:
    if test_file is None:
        import sys
        return [ln.rstrip("\n") for ln in sys.stdin.read().splitlines()]
    else:
        with open(test_file, "r", encoding="utf-8") as f:
            return [ln.rstrip("\n") for ln in f.readlines()]

def get_line(source: Iterable[str]) -> str:
    if not source:
        return ""
    return source.pop(0)

def close_test_file(test_file: Optional[str], source: Iterable[str]) -> None:
    pass
