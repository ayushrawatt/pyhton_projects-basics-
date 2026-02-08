def show_balance(balance):
     print(f"\n💰 YOUR CURRENT BALANCE IS ₹{balance:.2f}\n")

def deposit():
    amount=float(input("➕ ENTER AMOUNT YOU WANT TO DEPOSIT:₹"))
    
    if amount <= 0 :
        print("❌INVALID AMOUNT!")
        return 0
    else:
        print(f"₹{amount} DEPOSITED SUCCESSFULLY!✅")
        return amount
    
def withdraw(balance):
    amount=float(input("➖ ENTER AMOUNT TO BE WITHDRAWN:₹"))

    if amount > balance:
        print("❌ INSUFFIENT BALANCE!")
        return 0
    elif amount <=0:
        print("❌ NOT A VALID AMOUNT TO WITHDRAW!")
        return 0
    else:
        print(f"✅ ₹{amount} IS WITHDRAWN SUCCESSFULLY!")
        return amount


is_running=True
balance=0

def main():
    global balance,is_running
    while is_running:
        print("***********************************")
        print("🏦 WELCOME TO MY SASTA PYTHON BANK")
        print("1️⃣ CHECK BALANCE")
        print("2️⃣ DEPOSIT")
        print("3️⃣ WITHDRAW")
        print("4️⃣ EXIT")
        print("***********************************")

        choice=input("ENTER YOUR CHOICE(1-4):")
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance+=deposit()
        elif choice == '3':
            balance-=withdraw(balance)
        elif choice == '4':
            print("\n👋 THANK YOU FOR USING MY SASTA PYTHON BANK!")
            is_running=False
        else :
            print("INVALID CHOICE! PLEASE TRY AGAIN.\n")

    print("JAA BE GAREEB🤡")
        
if __name__ == '__main__':
    main()