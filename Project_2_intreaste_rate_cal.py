mainCapital = 0
interestRate = 0
Time = 0

while mainCapital <=0:
    mainCapital = float(input("Enter your Investment : "))
    if(mainCapital <=0):
        print("Inevesment must be more than 0")

while interestRate <=0:
    interestRate = int(input("Enter your Interest Rate : "))
    if(interestRate <=0):
        print("interest-Rate must be more than 0")

while Time <=0:
    Time = int(input("Enter your Time"))
    if(Time <=0):
        print("You must put your money at least 1 year : ")

total = mainCapital * pow((1 + interestRate/100),Time)
print(f"Your money became ${total}")