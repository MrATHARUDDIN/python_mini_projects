import random

min = 1
max = 100

randomnumber = random.randint(min, max)
number_guess = 0
is_running = True

print(f"Guess the number between {min} to {max}")

if randomnumber % 2 == 0:
    print("Hint: The number is even.")
else:
    print("Hint: The number is odd.")

def show_hint():
    print("More Hints:")
    if randomnumber > 50:
        print("- The number is more than 50.")
    else:
        print("- The number is 50 or less.")
    
    if randomnumber > 75:
        print("- The number is more than 75.")
    else:
        print("- The number is 75 or less.")
    
    if randomnumber > 25:
        print("- The number is more than 25.")
    else:
        print("- The number is 25 or less.")

while is_running:
    try:
        my_guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if my_guess == randomnumber:
        print("🎉 Your answer is correct! You guessed it!")
        is_running = False
    else:
        number_guess += 1
        if my_guess < randomnumber:
            print("Incorrect. Your guess is too low.")
        else:
            print("Incorrect. Your guess is too high.")
        
        if number_guess == 3:
            show_hint()

        if number_guess == 5:
            is_running = False
            print(f"❌ You used all 5 guesses. The correct number was {randomnumber}.")
