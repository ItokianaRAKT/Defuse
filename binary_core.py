import random
import string


def generate_binary():
    length = random.randint(4, 7)
    bits = [str(random.randint(0, 1)) for _ in range(length)]
    bits[0] = "1"
    return "".join(bits)


def generate_key():
    return random.randint(1, 15)


def solve(binary_str, key):
    decimal = int(binary_str, 2)
    result = decimal + key
    if result % 2 == 0:
        return format(result, "X")
    else:
        binary_result = bin(result)[2:]
        return binary_result[::-1]


def generate_fragment():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=2))


def play_binary_core(timer):
    binary_str = generate_binary()
    key = generate_key()
    correct = solve(binary_str, key)
    fragment = generate_fragment()
    wrong_count = 0

    print(f"""
    ╔══════════════════════════════════════════════════════════╗
    ║                      BINARY CORE                         ║
    ╠══════════════════════════════════════════════════════════╣
    ║                                                          ║
    ║  Binary: {binary_str:<46} ║
    ║  Key:    {key:<46} ║
    ║                                                          ║
    ║  Steps:                                                  ║
    ║  1. Convert binary to decimal                            ║
    ║  2. Add the key                                          ║
    ║  3. If result is EVEN → convert to hexadecimal           ║
    ║     If result is ODD  → convert to binary and reverse    ║
    ║                                                          ║
    ║  Enter your answer.                                      ║
    ║  Type 'q' to quit.                                       ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    while True:
        answer = input("  Answer: ").strip()

        if answer == "q":
            return None

        if not answer:
            print("  Invalid input. Enter an answer.\n")
            continue

        if answer.upper() == correct:
            print(f"\n  CORRECT! Fragment: {fragment}")
            input("  Press Enter to continue...")
            return fragment
        else:
            wrong_count += 1
            if wrong_count >= 2:
                print("  2 wrong answers! Regenerating level...\n")
                binary_str = generate_binary()
                key = generate_key()
                correct = solve(binary_str, key)
                fragment = generate_fragment()
                wrong_count = 0
                print(f"    Binary: {binary_str}")
                print(f"    Key:    {key}")
                print()
            else:
                print(f"  WRONG! ({wrong_count}/2) Try again or 'q' to quit.\n")
