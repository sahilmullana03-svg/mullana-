"""
Task: Ek variable signal = "Red" rakho.

Agar signal Green hai → print "Go"

Agar Red hai → print "Stop"
"""

signal = input("Enter signal (Green/Red): ").strip().lower()

if signal == "green":
    print("Go")
elif signal == "red":
    print("Stop")
else:
    print("Invalid signal")
