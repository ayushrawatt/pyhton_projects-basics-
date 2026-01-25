import random
import time
import os

COLORS = [
    "\033[31m",  # red
    "\033[32m",  # green
    "\033[33m",  # yellow
    "\033[34m",  # blue
    "\033[35m",  # magenta
    "\033[36m"   # cyan
]
RESET = "\033[0m"

my_dice={
    1: ("╭───────╮",
        "│       │",
        "│   ●   │",
        "│       │",
        "╰───────╯"),
    2: ("╭───────╮",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "╰───────╯"),
    3: ("╭───────╮",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "╰───────╯"),
    4: ("╭───────╮",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "╰───────╯"),
    5: ("╭───────╮",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "╰───────╯"),
    6: ("╭───────╮",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "╰───────╯")
}

dice=[]
total=0
num_of_dice = int(input("HOW MANY DICE YOU WANT TO ROLL?: "))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_dice(dice):
    for line in range(5):
        for i, die in enumerate(dice):
            color = COLORS[i % len(COLORS)]
            print(color + my_dice[die][line] + RESET, end="  ")
        print()

# Animation loop
for _ in range(10):  
    clear()
    dice = [random.randint(1, 6) for _ in range(num_of_dice)]
    print_dice(dice)
    time.sleep(0.15)

# Final result
clear()
dice = [random.randint(1, 6) for _ in range(num_of_dice)]
print_dice(dice)


total = sum(dice)
print(f"\nTotal is {total}")



for die in range(num_of_dice):
    num=random.randint(1,6)
    dice.append(num)

def print_dice(dice):
    for line in range(5):
        for i, die in enumerate(dice):
            color = COLORS[i % len(COLORS)]
            print(color + my_dice[die][line] + RESET, end="  ")
        print()


for die in dice:
    total+=die
