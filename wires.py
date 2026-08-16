from asyncio.tasks import sleep
import random
import time

print("""
╔══════════════════════════════════════════════════╗
║                 🔌 WIRES MODULE                  ║
╠══════════════════════════════════════════════════╣
║ RULES                                            ║
║                                                  ║
║ 1. If there are exactly TWO red wires,           ║
║    cut the wire immediately AFTER the second     ║
║    red wire.                                     ║
║                                                  ║
║ 2. If there is exactly ONE yellow wire,          ║
║    cut the wire immediately BEFORE it.           ║
║                                                  ║
║ 3. If there are more blue wires than green,      ║
║    cut the LAST blue wire.                       ║
║                                                  ║
║ 4. If none of the rules above apply,             ║
║    cut the FIRST wire.                           ║
║                                                  ║
║ ⚠ Rules are checked from TOP to BOTTOM.          ║
║   The FIRST valid rule determines the answer.    ║
╚══════════════════════════════════════════════════╝
""")

color=["Red", "Blue", "Green", "Yellow", "White"]
order=[]
for i in range (5):
    current=random.choice(color)
    print(current)
    order.append(current)
