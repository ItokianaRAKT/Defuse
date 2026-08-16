print("DEFUSE")


print("""
╔══════════════════════════════════════════════════════════╗
║                       🔌 WIRES                           ║
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
