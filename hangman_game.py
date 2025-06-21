import random
# Word list
words = ("apple", "orange", "banana", "coconut", "melon","lemon")

# Hangman ASCII art based on the number of incorrect guesses
hangman_art = {
    0: (
        "  _______",
        " |/      |",
        " |",
        " |",
        " |",
        " |",
        "_|___"
    ),
    1: (
        "  _______",
        " |/      |",
        " |      (_)",
        " |",
        " |",
        " |",
        "_|___"
    ),
    2: (
        "  _______",
        " |/      |",
        " |      (_)",
        " |       |",
        " |       |",
        " |",
        "_|___"
    ),
    3: (
        "  _______",
        " |/      |",
        " |      (_)",
        " |      \|",
        " |       |",
        " |",
        "_|___"
    ),
    4: (
        "  _______",
        " |/      |",
        " |      (_)",
        " |      \|/",
        " |       |",
        " |",
        "_|___"
    ),
    5: (
        "  _______",
        " |/      |",
        " |      (_)",
        " |      \|/",
        " |       |",
        " |      /",
        "_|___"
    ),
    6: (
        "  _______",
        " |/      |",
        " |      (_)",
        " |      \|/",
        " |       |",
        " |      / \\",
        "_|___"
    )
}

def display_man(wrong_guess):
    print("***********************")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("***********************")
    if(wrong_guess == 6):
        print("Sorry game over")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
     print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter one letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1

        if "_" not in hint:
            print("\nCongratulations! You guessed the word:")
            display_answer(hint)
            break

        if wrong_guess == 6:
            display_man(wrong_guess)
            print("The word was:", answer)
            break
main()