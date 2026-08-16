import sys


def save_cursor():
    sys.stdout.write("\033[s")


def restore_cursor():
    sys.stdout.write("\033[u")


def move_to_row_col(row, col=1):
    sys.stdout.write(f"\033[{row};{col}H")


def clear_line():
    sys.stdout.write("\033[K")


def flush():
    sys.stdout.flush()
