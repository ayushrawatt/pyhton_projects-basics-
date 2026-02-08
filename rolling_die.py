import random

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
num_of_dice=int(input("HOW MANY DICE YOU WANT TO ROLL?: "))

for die in range(num_of_dice):
    num=random.randint(1,6)
    dice.append(num)


for line in range(5):
    for die in dice:
        print(my_dice[die][line], end="  ")
    print()


for die in dice:
    total += die
print(f"Total is {total}")