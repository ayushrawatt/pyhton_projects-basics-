import random
import time

def spin_row():
    symbols=["🤡" , "⭐" , "💎" , "🔔" , "🍒"]
    results=[]
    
    for _ in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print(" |".join(row))

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[1]=='🤡':
            return bet * 2
        elif row[0]=='⭐':
            return bet * 3
        elif row[0]=='💎':
            print("💥 JACKPOT!!! 💥")
            return bet * 10
        elif row[0]=='🔔':
            return bet * 5
        elif row[0]=='🍒':
            return bet * 4
    return 0


def main():
    balance=100
    print("**************************")
    print("LET'S GAMBLE!!")
    print("Symbols: 🤡  ⭐ 💎 🔔 🍒")
    print("**************************")

    while balance > 0:
        print(f"\nCurrent balance ₹{balance}\n")
        bet=input("Place your bet amount:")

        if not bet.isdigit():
            print("Please enter a valid amount")
            continue
        
        bet=int(bet)

        if bet > balance:
            print("Insufficient Balance!")
            continue
        
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        balance -= bet

        row=spin_row()
        print("Spinning", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="")
        print("\n")

        print("-----------")
        print_row(row)
        print("-----------")

        payout=get_payout(row,bet)
        balance += payout

        if payout > 0:
            print(f"🎉 You won ₹{payout}!")
        else:
            print("😢 No win this time.")

        play_again=input("DO YOU WANT TO PLAY AGAIN(Y/N):").upper
        
        if play_again !='N':
            break
    
    print("________________________________________")
    print(f"GAME OVER! YOUR FINAL BBALANCE IS {balance}.")
if __name__ == '__main__':
    main()