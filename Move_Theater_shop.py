menu = {"pizza": 3.00,
        "pasta" : 4.50,
        "popcorn" : 6.00,
        "chips" : 1.00,
        "soda" : 2.50,
        "nachos" : 3.00,
}

total = 0
cart = []
print("---------------------")
for key, value in menu.items():
    print(f"{key:10}: value {value:.2f}")
print("---------------------")

while True:
    food = str(input("Enter a food to buy (Enter q to exist ) : ")).lower()
    if(food == "q"):
        break
    elif food not in menu:
        print("Item not found")

    else:
        cart.append(food)

for x in cart:
    total = total + menu.get(x)
    print(x, end=" ")

print(f"total value {total}")