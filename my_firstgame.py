import random

lower_num=1
higher_num=100
num=random.randint(lower_num,higher_num)
guesses=0
is_running=True

print("PYHTON NUMBER GUESSING GAME!")
print(" ")
print(f"SELECT A NUMBER BETWEEN {lower_num} TO {higher_num}.")

while is_running:
    guess=input("ENTER YOUR GUESS: ")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess < lower_num or guess > higher_num:
            print(f"PLEASE SELECT NUMBER WITHIN GIVEN RANNGE OF {lower_num} to {higher_num}.")
        elif guess > num:
            print("TOO HIGH!😩 TRY AGAIN")
        elif guess < num:
            print("TOO LOW!👹 TRY AGAIN")
        else:
            print(f"CORRECT!!🥳🥳 NUMBER IS {num}")
            is_running=False
    else:
        print("INVALID GUESS!!")
        print(f"PLEASE SELECT A NUMBER BETWEEN {lower_num} TO {higher_num}.")

print(f"TOTAL NUMBER OF GUESSES: {guesses}")