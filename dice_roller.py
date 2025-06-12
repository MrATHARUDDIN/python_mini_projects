import random

dice_faces = {
    1: ["+-------+",
        "|       |",
        "|   o   |",
        "|       |",
        "+-------+"],

    2: ["+-------+",
        "| o     |",
        "|       |",
        "|     o |",
        "+-------+"],

    3: ["+-------+",
        "| o     |",
        "|   o   |",
        "|     o |",
        "+-------+"],

    4: ["+-------+",
        "| o   o |",
        "|       |",
        "| o   o |",
        "+-------+"],

    5: ["+-------+",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "+-------+"],

    6: ["+-------+",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "+-------+"],
}

dice = []
total = 0
number_dice = int(input("How many dice do you need? "))

for die in range(number_dice):
    value = random.randint(1, 6)
    dice.append(value)
    total += value

    # Print the dice face
    for line in dice_faces[value]:
        print(line)
    print()  # Blank line between dice

print("Dice rolls:", dice)
print("Total:", total)
