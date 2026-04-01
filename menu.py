import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGO = """
  ____  _   _ _____ ____ ____    _____ _   _ _____
 / ___|| | | | ____/ ___/ ___|  |_   _| | | | ____|
| |  _ | | | |  _| \\___\\___ \\    | | | |_| |  _|
| |_| || |_| | |___|___) |__) |   | | |  _  | |___
 \\____| \\___/|_____|____/____/    |_| |_| |_|_____|

 _   _ _   _ __  __ ____  _____ ____
| \\ | | | | |  \\/  | __ )| ____|  _ \\
|  \\| | | | | |\\/| |  _ \\|  _| | |_) |
| |\\  | |_| | |  | | |_) | |___|  _ <
|_| \\_|\\___/|_|  |_|____/|_____|_| \\_\\
"""

VERSIONS: dict[str, tuple[str, str]] = {
    "1": ("Original  (course, procedural)", "original/main.py"),
    "2": ("Advanced  (OOP rebuild)",         "advanced/main.py"),
}


def main() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    print(LOGO)
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
