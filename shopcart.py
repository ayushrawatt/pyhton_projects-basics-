menu={"pizza": 99,
      "fries": 50,
      "popcorn": 59,
      "cold drink": 40,
      "burger": 49,
      "water bottle": 30,
      "chips": 30
}

cart=[]

print("--------MENU--------")
for key,values in menu.items():
    print(f"{key:10}: ₹{values:.2f}")
print("--------------------")
print("")

while True:
    food=input("SELECT FOOD TO BUY FROM GIVEN MENU(q to quit):").lower()
    
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

total = 0

print("\n--------YOUR ORDER--------")
for food in cart:
    price = menu.get(food)
    total += price
    print(f"{food:10}: ₹{price:.2f}")

print("--------------------------")
print(f"Total Amount: ₹{total:.2f}")
