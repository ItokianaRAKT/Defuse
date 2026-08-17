# FAILSAFE 💣

A small terminal-based bomb defusal puzzle game written in Python.

## 🎮 Concept

You have **15 minutes** to defuse a bomb.

The bomb contains **3 modules**:

1. 🔌 Wires
2. 🔢 Binary Core
3. 🔐 Code Lock

Each module contains a puzzle.

Successfully solving a module gives you **one fragment of the bomb's password**.

The final password is composed of the three fragments:

```text
WIRES       → Fragment 1
BINARY CORE → Fragment 2
CODE LOCK   → Fragment 3

Fragment 1 + Fragment 2 + Fragment 3
                  ↓
             BOMB PASSWORD
                  ↓
              💚 DEFUSED
```

You must solve all three modules before you can enter the final password.

---

## ⏱️ Timer

The bomb starts with:

```text
15:00
```

The timer only runs while the player is inside a module.

The timer is paused while the player is on the main bomb screen.


If the timer reaches `00:00`, the bomb explodes.

---

## 🔄 Leaving a module

A module can be abandoned at any time.

However:

> **Leaving an unsolved module completely resets its current challenge.**

Example:

```text
Wires challenge:
🔴 🔵 🟡 🟢 🔴

Player leaves.

↓

New Wires challenge:
🟢 🟡 🔵 🔴
```

The player must start again from the beginning.

The timer does **not** reset.

This makes leaving a module a strategic decision.

---

# 🔌 Module 1: Wires

## Objective

Determine which wire must be cut based on a set of rules.

The player receives a randomly generated set of **5 wires**.

Each wire has a color:

* Red
* Blue
* Yellow
* Green
* White

The player must determine the correct wire to cut.

## Rules

The rules are evaluated **from top to bottom**.

### Example of rules

#### Rule 1

If there are **exactly two red wires**, cut the wire immediately after the second red wire.

If the second red wire is the last wire, this rule is invalid.

#### Rule 2

If there is **exactly one yellow wire**, cut the wire immediately before it.

If the yellow wire is first, this rule is invalid.

#### Rule 3

If there are more blue wires than green wires, cut the **last blue wire**.

#### Rule 4

If none of the previous rules produced a valid wire, cut the **first wire**.

## Important

Only the **first valid rule** is used.

The player therefore needs to:

1. Count colors.
2. Check conditions.
3. Respect rule priority.
4. Determine the exact position.

## Example

```text
WIRES

1. 🔵 Blue
2. 🟢 Green
3. 🔴 Red
4. 🟡 Yellow
5. 🔴 Red
```

Rule 1:

There are exactly two red wires.

The second red wire is position 5.

There is no wire after it.

Therefore Rule 1 is invalid.

Rule 2:

There is exactly one yellow wire.

It is position 4.

The wire immediately before it is position 3.

Therefore:

```text
Correct wire: 3
```

---

# 🔢 Module 2: Binary Core

## Objective

Transform a binary number according to a sequence of operations.

The player receives:

* a binary number
* a key

## Rules

The player must perform the following operations in order.

### Step 1

Convert the binary number to decimal.

### Step 2

Add the provided key.

### Step 3

Check whether the result is even or odd.

### Step 4

If the result is even:

Convert the result to hexadecimal.

If the result is odd:

Convert the result back to binary and reverse it.

### Step 5

The resulting value is the module's answer.

## Example

```text
Binary: 10110
Key: 8
```

Convert:

```text
10110₂ = 22
```

Add the key:

```text
22 + 8 = 30
```

30 is even.

Convert to hexadecimal:

```text
30 = 1E
```

Answer:

```text
1E
```

## Important

The player must perform the operations **in order**.

The challenge is generated randomly, so the binary number and key change each time.

---

# 🔐 Module 3: Code Lock

## Objective

Find a secret **4-digit code** using logical clues.

The code is generated randomly each game.

The player receives a set of dynamically generated clues.

## How it works

1. The program generates a random 4-digit secret code.
2. It generates 5-7 logical clues compatible with that code.
3. It verifies that only **one** combination (0000-9990) satisfies all clues.
4. The player reads the clues and deduces the code.

## Clue types

The following types of clues can appear:

- Position comparisons: A > B, A < B, A = B, A ≠ B
- Parity: A is even, A is odd
- Arithmetic: A + B = X, A - B = X, A = B × X
- Aggregation: A + B + C = X, sum of all digits = X
- Properties: no repeated digits, exactly N even digits
- Value constraints: A > X, A < X

## Example

The challenge might produce:

```text
CODE LOCK

Find the secret 4-digit code.

Clues:
• The first digit is greater than the third digit.
• The second digit is even.
• The sum of the first and fourth digits is 11.
• The third digit equals the second digit multiplied by 2.
• No digit is repeated.
```

The player must combine multiple clues to deduce the code.

---

# 🔐 Final Password

Each successful module produces a password fragment.

Example:

```text
Wires       → A7
Binary Core → 1E
Code Lock   → 42
```

The final password becomes:

```text
A71E42
```

The player enters it into the bomb.

If correct:

```text
╔══════════════════════════╗
║      SYSTEM DISARMED     ║
╚══════════════════════════╝

Password accepted.

Time remaining: 04:37

💚 BOMB DEFUSED
```

If incorrect:

```text
ACCESS DENIED

The password is incorrect.
```

The player can try again as long as there is time remaining.

---

# 🏁 Victory

The player wins when:

1. All three modules are solved.
2. The three fragments have been collected.
3. The final password is entered correctly.

The final screen should display:

* Remaining time
* Number of attempts/errors
* Completion time
* Final score/rank

---

# 💥 Defeat

The player loses when:

```text
Time remaining = 00:00
```

The bomb explodes.

```text
╔══════════════════════════╗
║       💥 BOOM 💥          ║
╚══════════════════════════╝

MISSION FAILED.

The bomb detonated.
```

---

# 🛠️ Technology

Python 3

Only Python's standard library is required.

Suggested modules:

```python
import random
import time
```

Optional later:

```python
import os
```

No external dependencies are required.

---

# 📁 Initial project structure

Start extremely small:

```text
failsafe/
│
├── .venv/
└── main.py
```

Do not split the project into multiple files until the first playable version works.

Later, the project can become:

```text
failsafe/
│
├── main.py
├── bomb.py
├── wires.py
├── binary_core.py
├── code_lock.py
└── utils.py
```

---

# 🎯 Project Goal

The goal is not to build a huge game.

The goal is to practice:

* Python functions
* conditionals
* loops
* lists
* dictionaries
* random generation
* string manipulation
* number conversion
* time management
* input validation
* program structure
* debugging

while building an actual playable mini-game.
