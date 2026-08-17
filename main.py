import sys
import os

from timer import Timer
from utils import move_to_row_col, clear_line, flush
from wires import play_wires
from binary_core import play_binary_core


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_menu(fragments):
    move_to_row_col(3, 1)
    clear_line()
    sys.stdout.write("  FAILSAFE - Bomb Defusal\n")
    move_to_row_col(4, 1)
    clear_line()
    sys.stdout.write("  -----------------------\n")

    labels = [
        ("1", "Wires",       "WIRES"),
        ("2", "Binary Core", "BINARY"),
        ("3", "Code Lock",   "CODE"),
    ]

    for i, (key, name, tag) in enumerate(labels):
        row = 5 + i
        status = f" [{fragments[tag]}]" if fragments[tag] else ""
        move_to_row_col(row, 1)
        clear_line()
        sys.stdout.write(f"  {key}. {name}{status}\n")

    move_to_row_col(8, 1)
    clear_line()
    all_done = all(fragments[t] for t in ["WIRES", "BINARY", "CODE"])
    if all_done:
        sys.stdout.write("  4. Enter final password\n")
    else:
        sys.stdout.write("  4. Enter final password (need all fragments)\n")

    move_to_row_col(9, 1)
    clear_line()
    sys.stdout.write("  5. Quit\n")
    move_to_row_col(10, 1)
    clear_line()
    sys.stdout.write("  > ")
    flush()


def play_module_wires(timer, fragments):
    timer.resume()
    clear_screen()
    timer._display()
    result = play_wires(timer)
    timer.pause()
    if result is not None:
        fragments["WIRES"] = result
    clear_screen()
    timer._display()


def play_module_binary_core(timer, fragments):
    timer.resume()
    clear_screen()
    timer._display()
    result = play_binary_core(timer)
    timer.pause()
    if result is not None:
        fragments["BINARY"] = result
    clear_screen()
    timer._display()


def main():
    timer = Timer(900)
    fragments = {"WIRES": None, "BINARY": None, "CODE": None}
    clear_screen()
    timer.start()
    timer._display()

    while True:
        show_menu(fragments)
        try:
            choice = input().strip()
        except (EOFError, KeyboardInterrupt):
            break

        if choice == "1":
            timer.pause()
            clear_screen()
            timer._display()
            play_module_wires(timer, fragments)
        elif choice == "2":
            timer.pause()
            clear_screen()
            timer._display()
            play_module_binary_core(timer, fragments)
        elif choice == "4":
            timer.pause()
            clear_screen()
            timer._display()
            all_done = all(fragments[t] for t in ["WIRES", "BINARY", "CODE"])
            move_to_row_col(3, 1)
            clear_line()
            sys.stdout.write("  FINAL PASSWORD\n")
            move_to_row_col(4, 1)
            clear_line()
            if all_done:
                password = fragments["WIRES"] + fragments["BINARY"] + fragments["CODE"]
                sys.stdout.write(f"  Password: {password}\n")
                move_to_row_col(5, 1)
                clear_line()
                sys.stdout.write("  (Not yet implemented)\n")
            else:
                sys.stdout.write("  You need all 3 fragments first.\n")
                move_to_row_col(5, 1)
                clear_line()
                sys.stdout.write(f"  Wires:  {'??' if not fragments['WIRES'] else fragments['WIRES']}\n")
                move_to_row_col(6, 1)
                clear_line()
                sys.stdout.write(f"  Binary: {'??' if not fragments['BINARY'] else fragments['BINARY']}\n")
                move_to_row_col(7, 1)
                clear_line()
                sys.stdout.write(f"  Code:   {'??' if not fragments['CODE'] else fragments['CODE']}\n")
            move_to_row_col(9, 1)
            clear_line()
            sys.stdout.write("  Press Enter to return...\n")
            flush()
            input()
            clear_screen()
            timer._display()
        elif choice == "5":
            timer.stop()
            clear_screen()
            print("  Bomb detonated. Goodbye.\n")
            break


if __name__ == "__main__":
    main()
