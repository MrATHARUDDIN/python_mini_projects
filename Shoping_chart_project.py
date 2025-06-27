# Shopping cart program

foods = []
prices = []
total = 0

 
while True:
    food = str(input("Enter a food to buy (Enter q to exist ) : "))
    if(food.lower() == "q"):
        break
    else:
        price = float(input(f"Enter the price {food} : $"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart ------")
for food in foods:
    print(food)

for price in prices:
    total = total + price

print(f"Your total  is : {total}$")
