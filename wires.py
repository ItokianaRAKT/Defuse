import random
import string


COLORS = ["Red", "Blue", "Green", "Yellow", "White"]

def generate_wires():
    return [random.choice(COLORS) for _ in range(5)]


def count_colors(wires):
    counts = {}
    for c in COLORS:
        counts[c] = wires.count(c)
    return counts


def first_pos(wires, color):
    for i, c in enumerate(wires):
        if c == color:
            return i
    return -1


def last_pos(wires, color):
    for i in range(len(wires) - 1, -1, -1):
        if wires[i] == color:
            return i
    return -1


def all_positions(wires, color):
    return [i for i, c in enumerate(wires) if c == color]


def solve(wires):
    counts = count_colors(wires)

    red_positions = all_positions(wires, "Red")
    blue_positions = all_positions(wires, "Blue")
    yellow_positions = all_positions(wires, "Yellow")
    green_positions = all_positions(wires, "Green")
    white_positions = all_positions(wires, "White")

    # Rule 1: exactly two red wires
    if counts["Red"] == 2 and len(red_positions) == 2:
        pos_a, pos_b = red_positions
        if pos_b - pos_a == 1:
            # adjacent: cut after second red
            if pos_b < 4:
                return pos_b + 2
        else:
            # not adjacent: if position 4 (index 3) is not red, cut it
            if wires[3] != "Red":
                return 4

    # Rule 2: more blue than red
    if counts["Blue"] > counts["Red"]:
        first_blue = first_pos(wires, "Blue")
        first_red = first_pos(wires, "Red")
        if first_blue < first_red:
            # cut after last blue
            last_blue = last_pos(wires, "Blue")
            if last_blue < 4:
                return last_blue + 2
        else:
            # cut before first blue
            if first_blue > 0:
                return first_blue

    # Rule 3: exactly two yellow wires
    if counts["Yellow"] == 2:
        y1, y2 = yellow_positions
        if abs(y1 - y2) == 2:
            # exactly one wire separates them
            between = (y1 + y2) // 2
            if wires[between] != "Yellow" and wires[between] != "Green":
                return between + 1
            elif wires[0] == "Blue":
                return 1

    # Rule 4: more green than yellow
    if counts["Green"] > counts["Yellow"]:
        first_g = first_pos(wires, "Green")
        last_g = last_pos(wires, "Green")
        between_count = last_g - first_g - 1
        if between_count > 0:
            if between_count % 2 == 0:
                # even: cut before first green
                return first_g + 1
            else:
                # odd: cut after last green
                if last_g < 4:
                    return last_g + 2

    # Rule 5: exactly one blue and one yellow
    if counts["Blue"] == 1 and counts["Yellow"] == 1:
        b = blue_positions[0]
        y = yellow_positions[0]
        if b < y:
            # cut after yellow
            if y < 4:
                return y + 2
        else:
            # cut before blue
            if b > 0:
                return b + 1

    # Rule 6: exactly three wires of same color
    for color in COLORS:
        positions = all_positions(wires, color)
        if len(positions) == 3:
            mid = positions[1]
            if mid % 2 == 0:
                # even index (position odd): check white
                if counts["White"] > 0:
                    return white_positions[0] + 1
            else:
                # odd index (position even): cut middle of three
                return mid + 1

    # Final rule
    if counts["Red"] == 0 or counts["Green"] == 0:
        return 5

    first_r = first_pos(wires, "Red")
    last_g = last_pos(wires, "Green")
    total = first_r + last_g
    if total % 2 == 0:
        if counts["Blue"] > 0:
            return first_pos(wires, "Green") + 1
        else:
            return first_r + 1
    else:
        if counts["White"] > 0:
            return white_positions[0] + 1
        elif last_g > 0:
            return last_g
        else:
            return 5

    return 1


def generate_fragment():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=2))


def play_wires(timer):
    wires = generate_wires()
    correct = solve(wires)
    fragment = generate_fragment()
    wrong_count = 0

    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                          WIRES                           ║
    ╠══════════════════════════════════════════════════════════╣
    ║ RULE 1                                                   ║
    ║ If there are exactly two red wires:                      ║
    ║   • If they are adjacent, cut the wire immediately       ║
    ║     after the second red wire.                           ║
    ║   • Otherwise, if position 4 is not red, cut it.         ║
    ║   • Otherwise, move to the next rule.                    ║
    ║                                                          ║
    ║ RULE 2                                                   ║
    ║ If there are more blue wires than red wires:             ║
    ║   • If the first blue wire appears before the first      ║
    ║     red wire, cut the wire immediately after the last    ║
    ║     blue wire.                                           ║
    ║   • Otherwise, cut the wire immediately before the       ║
    ║     first blue wire.                                     ║
    ║                                                          ║
    ║ RULE 3                                                   ║
    ║ If there are exactly two yellow wires:                   ║
    ║   • If exactly one wire separates them:                  ║
    ║       - If position 3 is neither yellow nor green,       ║
    ║         cut it.                                          ║
    ║       - Otherwise, cut the first wire if it is blue.     ║
    ║   • Otherwise, move to the next rule.                    ║
    ║                                                          ║
    ║ RULE 4                                                   ║
    ║ If there are more green wires than yellow wires:         ║
    ║   • Find the first and last green wires.                 ║
    ║   • Count the wires between them.                        ║
    ║   • If there are none, move to the next rule.            ║
    ║   • Otherwise:                                           ║
    ║       - If the number is even, cut the wire immediately  ║
    ║         before the first green wire.                     ║
    ║       - If the number is odd, cut the wire immediately   ║
    ║         after the last green wire.                       ║
    ║                                                          ║
    ║ RULE 5                                                   ║
    ║ If there is exactly one blue wire and one yellow wire:   ║
    ║   • If blue is before yellow, cut the wire immediately   ║
    ║     after yellow.                                        ║
    ║   • If yellow is before blue, cut the wire immediately   ║
    ║     before blue.                                         ║
    ║                                                          ║
    ║ RULE 6                                                   ║
    ║ If there are exactly three wires of the same color:      ║
    ║   • Find the middle wire among the three.                ║
    ║   • If its position is odd:                              ║
    ║       - If there is a white wire, cut the first white    ║
    ║         wire.                                            ║
    ║       - Otherwise, move to the next rule.                ║
    ║   • If its position is even, cut the middle wire among   ║
    ║     the three.                                           ║
    ║                                                          ║
    ║ FINAL RULE                                               ║
    ║ If no wire has been cut:                                 ║
    ║   • If there is no red wire or no green wire, cut the    ║
    ║     last wire.                                           ║
    ║   • Otherwise, calculate:                                ║
    ║       first red position + last green position           ║
    ║                                                          ║
    ║     If the result is even:                               ║
    ║       - If there is a blue wire, cut the first green     ║
    ║         wire.                                            ║
    ║       - Otherwise, cut the first red wire.               ║
    ║                                                          ║
    ║     If the result is odd:                                ║
    ║       - If there is a white wire, cut the first white    ║
    ║         wire.                                            ║
    ║       - Otherwise, if a wire exists before the last      ║
    ║         green wire, cut it.                              ║
    ║       - Otherwise, cut the last wire.                    ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    for i, w in enumerate(wires):
        print(f"    {i + 1}. {w}")
    print()

    while True:
        answer = input("  Which wire to cut? (1-5) or 'q' to quit: ").strip().lower()

        if answer == "q":
            return None

        if answer.isdigit() and answer in "12345":
            choice = int(answer)
            if choice == correct:
                print(f"\n  CORRECT! Fragment: {fragment}")
                input("  Press Enter to continue...")
                return fragment
            else:
                wrong_count += 1
                if wrong_count >= 2:
                    print("  2 wrong answers! Regenerating level...\n")
                    wires = generate_wires()
                    correct = solve(wires)
                    fragment = generate_fragment()
                    wrong_count = 0
                    for i, w in enumerate(wires):
                        print(f"    {i + 1}. {w}")
                    print()
                else:
                    print(f"  WRONG! ({wrong_count}/2) Try again or 'q' to quit.\n")
                continue

        print("  Invalid input. Enter 1-5 or 'q'.\n")
