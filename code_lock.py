import random
import string


NAMES = ["first", "second", "third", "fourth"]
BOX_WIDTH = 68


def generate_secret():
    return [random.randint(0, 9) for _ in range(4)]


def validate_clues(clues):
    count = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    candidate = [a, b, c, d]
                    if all(fn(candidate) for fn, _ in clues):
                        count += 1
    return count


def gen_greater_than(secret):
    a, b = random.sample(range(4), 2)
    if secret[a] > secret[b]:
        return (
            lambda c, _a=a, _b=b: c[_a] > c[_b],
            f"The {NAMES[a]} digit is greater than the {NAMES[b]} digit."
        )
    return None


def gen_less_than(secret):
    a, b = random.sample(range(4), 2)
    if secret[a] < secret[b]:
        return (
            lambda c, _a=a, _b=b: c[_a] < c[_b],
            f"The {NAMES[a]} digit is less than the {NAMES[b]} digit."
        )
    return None


def gen_equal(secret):
    a, b = random.sample(range(4), 2)
    if secret[a] == secret[b]:
        return (
            lambda c, _a=a, _b=b: c[_a] == c[_b],
            f"The {NAMES[a]} digit equals the {NAMES[b]} digit."
        )
    return None


def gen_different(secret):
    a, b = random.sample(range(4), 2)
    if secret[a] != secret[b]:
        return (
            lambda c, _a=a, _b=b: c[_a] != c[_b],
            f"The {NAMES[a]} digit is different from the {NAMES[b]} digit."
        )
    return None


def gen_even(secret):
    a = random.randint(0, 3)
    if secret[a] % 2 == 0:
        return (
            lambda c, _a=a: c[_a] % 2 == 0,
            f"The {NAMES[a]} digit is even."
        )
    return None


def gen_odd(secret):
    a = random.randint(0, 3)
    if secret[a] % 2 == 1:
        return (
            lambda c, _a=a: c[_a] % 2 == 1,
            f"The {NAMES[a]} digit is odd."
        )
    return None


def gen_sum2(secret):
    a, b = random.sample(range(4), 2)
    x = secret[a] + secret[b]
    return (
        lambda c, _a=a, _b=b, _x=x: c[_a] + c[_b] == _x,
        f"The sum of the {NAMES[a]} and {NAMES[b]} digits is {x}."
    )


def gen_diff2(secret):
    a, b = random.sample(range(4), 2)
    x = abs(secret[a] - secret[b])
    if x == 0:
        return None
    return (
        lambda c, _a=a, _b=b, _x=x: abs(c[_a] - c[_b]) == _x,
        f"The difference between the {NAMES[a]} and {NAMES[b]} digits is {x}."
    )


def gen_product(secret):
    a, b = random.sample(range(4), 2)
    if secret[a] != 0 and secret[b] % secret[a] == 0:
        k = secret[b] // secret[a]
        if k > 1:
            return (
                lambda c, _a=a, _b=b, _k=k: c[_b] == c[_a] * _k,
                f"The {NAMES[b]} digit equals the {NAMES[a]} digit multiplied by {k}."
            )
    if secret[b] != 0 and secret[a] % secret[b] == 0:
        k = secret[a] // secret[b]
        if k > 1:
            return (
                lambda c, _a=a, _b=b, _k=k: c[_a] == c[_b] * _k,
                f"The {NAMES[a]} digit equals the {NAMES[b]} digit multiplied by {k}."
            )
    return None


def gen_sum3(secret):
    positions = random.sample(range(4), 3)
    x = sum(secret[p] for p in positions)
    names = ", ".join(NAMES[p] for p in positions[:-1]) + f" and {NAMES[positions[-1]]}"
    return (
        lambda c, _ps=tuple(positions), _x=x: sum(c[p] for p in _ps) == _x,
        f"The sum of the {names} digits is {x}."
    )


def gen_total_sum(secret):
    x = sum(secret)
    return (
        lambda c, _x=x: sum(c) == _x,
        f"The sum of all four digits is {x}."
    )


def gen_no_duplicates(secret):
    if len(set(secret)) == 4:
        return (
            lambda c: len(set(c)) == 4,
            "No digit is repeated."
        )
    return None


def gen_exactly_n_even(secret):
    even_count = sum(1 for d in secret if d % 2 == 0)
    labels = {1: "one", 2: "two", 3: "three"}
    if even_count in labels:
        n = even_count
        label = labels[n]
        word = "digit" if n == 1 else "digits"
        return (
            lambda c, _n=n: sum(1 for d in c if d % 2 == 0) == _n,
            f"There are exactly {label} even {word}."
        )
    return None


def gen_pos_value_gt(secret):
    a = random.randint(0, 3)
    if secret[a] > 0:
        v = random.randint(0, secret[a] - 1)
        return (
            lambda c, _a=a, _v=v: c[_a] > _v,
            f"The {NAMES[a]} digit is greater than {v}."
        )
    return None


def gen_pos_value_lt(secret):
    a = random.randint(0, 3)
    if secret[a] < 9:
        v = random.randint(secret[a] + 1, 9)
        return (
            lambda c, _a=a, _v=v: c[_a] < _v,
            f"The {NAMES[a]} digit is less than {v}."
        )
    return None


CLUE_GENERATORS = [
    gen_greater_than,
    gen_less_than,
    gen_equal,
    gen_different,
    gen_even,
    gen_odd,
    gen_sum2,
    gen_diff2,
    gen_product,
    gen_sum3,
    gen_total_sum,
    gen_no_duplicates,
    gen_exactly_n_even,
    gen_pos_value_gt,
    gen_pos_value_lt,
]

TARGET_CLUES = 6


def generate_clues(secret):
    clues = []
    current_count = 10000

    for _ in range(500):
        if len(clues) >= TARGET_CLUES and current_count == 1:
            break
        random.shuffle(CLUE_GENERATORS)
        for gen in CLUE_GENERATORS:
            clue = gen(secret)
            if clue is None:
                continue
            test_clues = clues + [clue]
            new_count = validate_clues(test_clues)
            if new_count < current_count and new_count > 0:
                clues.append(clue)
                current_count = new_count
                if new_count == 1:
                    return clues
                break
    return clues


def generate_fragment():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=2))


def play_code_lock(timer):
    secret = None
    clues = []
    while len(clues) < 3:
        secret = generate_secret()
        clues = generate_clues(secret)
    fragment = generate_fragment()
    wrong_count = 0

    print(f"""
    ╔{'═' * BOX_WIDTH}╗
    ║{'CODE LOCK':^{BOX_WIDTH}}║
    ╠{'═' * BOX_WIDTH}╣
    ║{'':^{BOX_WIDTH}}║
    ║{'Find the secret 4-digit code.':^{BOX_WIDTH}}║
    ║{'':^{BOX_WIDTH}}║
    ║{'Clues:':<{BOX_WIDTH}}║""")
    for _, desc in clues:
        padding = BOX_WIDTH - 4 - len(desc)
        print(f"    ║  • {desc}{' ' * padding}║")
    print(f"""    ║{'':^{BOX_WIDTH}}║
    ║{'Type q to quit.':<{BOX_WIDTH}}║
    ║{'':^{BOX_WIDTH}}║
    ╚{'═' * BOX_WIDTH}╝
    """)

    while True:
        answer = input("  Code (4 digits): ").strip()

        if answer == "q":
            return None

        if not answer.isdigit() or len(answer) != 4:
            print("  Invalid input. Enter exactly 4 digits.\n")
            continue

        candidate = [int(c) for c in answer]
        if candidate == secret:
            print(f"\n  CORRECT! Fragment: {fragment}")
            input("  Press Enter to continue...")
            return fragment
        else:
            wrong_count += 1
            if wrong_count >= 2:
                print("  2 wrong answers! Regenerating level...\n")
                secret = None
                clues = []
                while len(clues) < 3:
                    secret = generate_secret()
                    clues = generate_clues(secret)
                fragment = generate_fragment()
                wrong_count = 0
                print("    New code generated. Good luck!\n")
                for _, desc in clues:
                    print(f"    • {desc}")
                print()
            else:
                print(f"  WRONG! ({wrong_count}/2) Try again or type 'q' to quit.\n")
