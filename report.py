"""Prints the list of smells in a clear, readable way."""


def print_report(file_path, smells):
    print(f"Analyzing: {file_path}\n")
    for smell in smells:
        print(f"[{smell.category:<9}] line {smell.line:>3}: {smell.message}")
    print(f"\nTotal: {len(smells)} smell(s) found")
    if not smells:
        print("Clean code! ✅")
