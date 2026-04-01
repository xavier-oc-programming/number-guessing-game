import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VERSIONS: dict[str, tuple[str, str]] = {
    "1": ("Original  (course, procedural)", "original/main.py"),
    "2": ("Advanced  (OOP rebuild)",         "advanced/main.py"),
}


def main() -> None:
    print("\n  Day 12 — Number Guessing Game\n")
    for key, (label, _) in VERSIONS.items():
        print(f"    [{key}]  {label}")
    print("    [q]  Quit\n")

    while True:
        choice = input("  Select a version: ").strip().lower()
        if choice in VERSIONS:
            _, path = VERSIONS[choice]
            subprocess.run([sys.executable, os.path.join(BASE_DIR, path)])
            break
        elif choice == "q":
            break
        else:
            print("  Please enter 1, 2, or q.")


if __name__ == "__main__":
    main()
