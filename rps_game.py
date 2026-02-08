import random

options=("rock","paper","scissors")
game_running=True

while game_running:
    comp=random.choice(options)
    player=None

    while player not in options:
        player=input("ENTER A CHOICE (ROCK,PAPER,SCISSORS):").lower()

    print(f"Player:{player}")
    print(f"Computer:{comp}")

    if player==comp:
        print("IT'S A TIE!")
    elif player=="scissors" and comp=="paper":
        print("YOU WIN!")
    elif player=="paper" and comp=="rock":
        print("YOU WIN!")
    elif player=="rock" and comp=="scissors":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

    play_again=input("Want to Play Again?(y/n): ").lower()
    if play_again == "n":
        game_running = False
    
print("GET OUT YOU LOSSER!🤡")
