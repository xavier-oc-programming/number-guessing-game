import os
import sys
import time
import tty
import termios

from config import TYPEWRITER_DELAY, DIVIDER_CHAR, DIVIDER_WIDTH

LOGO = """\
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


class Colors:
    CYAN   = "\033[96m"
    GREEN  = "\033[92m"
    RED    = "\033[91m"
    YELLOW = "\033[93m"
    DIM    = "\033[2m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def typewriter(text: str, delay: float = TYPEWRITER_DELAY) -> None:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def divider() -> None:
    print(Colors.DIM + DIVIDER_CHAR * DIVIDER_WIDTH + Colors.RESET)


def print_result(message: str) -> None:
    print(f"{Colors.GREEN}{message}{Colors.RESET}")


def print_error(message: str) -> None:
    print(f"{Colors.RED}{message}{Colors.RESET}")


def get_keypress() -> str:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == "\x1b":
            ch += sys.stdin.read(2)
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def print_logo() -> None:
    clear()
    for char in Colors.CYAN + Colors.BOLD + LOGO + Colors.RESET:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(TYPEWRITER_DELAY)
    print()
    time.sleep(0.5)
