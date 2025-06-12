import random

options = ("rock", "paper", "siccor")
point = 0
    
while True :
    option = random.choice(options)
    Us = str(input(("Our option between rock, paper, siccor :  "))).lower()
    print(f" Computer : {option}")
    if (Us == "rock" and option == "siccor"):
        print(f"You win... ")
        point += 1
        print(f"Your Current point {point}")

    elif (Us == "paper" and option == "rock"):
        print(f"You win... ")
        point += 1
        print(f"Your Current point {point}")

    elif (Us == "siccor" and option == "paper"):
        print(f"You win... ")
        point += 1
        print(f"Your Current point {point}")

    elif (Us == option):
        print(f"Draw")
        point = point
        print(f"Your Current point {point}")
    else:
        print("You lost")
        break

print(point)