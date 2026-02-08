#HANGMAN PROGRAM
import random

words = [
    "apple", "house", "chair", "table", "mouse",
    "water", "bread", "phone", "light", "clock",
    "shirt", "plant", "river", "music", "smile"
]

hangman_art = {
    0: """
     ------
     |    |
     |
     |
     |
     |
    ------
    """,
    1: """
     ------
     |    |
     |    O
     |
     |
     |
    ------
    """,
    2: """
     ------
     |    |
     |    O
     |    |
     |
     |
    ------
    """,
    3: """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ------
    """,
    4: """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ------
    """,
    5: """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ------
    """,
    6: """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ------
    """
}

def display_man(wrong_guesses):
    print(hangman_art[wrong_guesses])

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answwer):
    print(" ".join(answwer))

def main():
    answer=random.choice(words)
    hint= ["_"] * len(answer)
    wrong_guesses=0
    guessed_letters= set()
    is_running=True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess=input("GUESS A LETTER:").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("INVALID GUESS!")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else :
            wrong_guesses += 1
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!🥳")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!preeti mota lenda haii💀")
            is_running = False
         
if __name__ == '__main__':
    main()





