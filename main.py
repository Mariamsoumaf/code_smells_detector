"""Code Smells Detector: finds Clean Code problems in a Python file.

Usage:
    python main.py <file.py>
"""

import sys
from pathlib import Path

from report import print_report
from analyzer import analyze_source


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.py>")
        return 1

    file_path = Path(sys.argv[1])
    if not file_path.is_file():
        print(f"File not found: {file_path}")
        return 1

    source = file_path.read_text(encoding="utf-8")
    smells = analyze_source(source)
    print_report(file_path, smells)
    return 0


if __name__ == "__main__":
    sys.exit(main())
