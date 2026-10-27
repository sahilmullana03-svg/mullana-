"""
Number Guessing Game

Concepts: Loops, random module, conditions.

Goal: Repetition aur user interaction सीखना.
"""

""" Python में random numbers generate करने के लिए हमें random module import करना पड़ता है.

import random लिखने से हम random module की functions use कर सकते हैं

ये module हमें random numbers, choices, shuffle जैसी functionalities देता है"""


import random  

secret_number = random.randint(1, 10)  # Computer chooses number
guess = None

while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right.")
    else:
        print("❌ Wrong guess, try again!")
