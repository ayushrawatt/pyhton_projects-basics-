# PYTHON COMPOUND INTEREST CALCULATOR
principle=0
rate=0
time=0

while True:
    principle=float(input("ENTER PRINCIPLE AMOUNT:"))
    if principle<=0:
        print("PRINCIPLE CAN NOT BE LESS THAN OR EQUAL TO 0")
    else:
        break
while True:
    rate=int(input("ENTER RATE OF INTERREST:"))
    if rate<0:
        print("interest can not be negative")
    else:
        break
    
while True:
    time=int(input("ENTER TIME: "))
    if time<=0:
        print("TIME CAN NOT BE NEGATIVE OR 0")
    else:
        break

total=principle*(pow(1+rate/100,time))
print(f"BALANCE AFTER {time} years is ₹{total:.2f}")

