questions = (
     ("How many elements are in the periodic table? : "),
    ("Which animal lays the largest eggs? : "),
    ("Which crypto is known as Digital Gold? : "),
    ("Minimum age limit to smoke cigarettes? : "),
    ("Who is the richest man right now? : "),
    ("What is the Best Programming language to start over")
)

options = (
    ("A. 116", "B. 118", "C. 120", "D. 112"),
    ("A. Ostrich", "B. Eagle", "C. Whale", "D. Crocodile"),
    ("A. Bitcoin", "B. Ethereum", "C. DogeCoin", "D. Litecoin"),
    ("A. 16", "B. 18", "C. 21", "D. 25"),
    ("A. Elon Musk", "B. Jeff Bezos", "C. Jon Cina", "D. Bill Gates"),
    ("A. C", "B. C++", "C. Java", "D. Python")
)

answers = ("B", "A", "A", "B", "A","D")

guesses = []
score = 0
questions_num = 0

for x in questions:
    print("--------------")
    print(x) #print question form questions one by one
    for option in options[questions_num]: # options[Index] so (0 to 4) for five question
        print(option) # so print the option from index number
    guess = input("Enter (A, B, C, D): ").upper() 
    guesses.append(guess)

    if guess == answers[questions_num]:
        score += 1
        print("Correct Answer")
    else:
        print("Incorrect")
        print(f"The correct answer is {answers[questions_num]}")

    questions_num += 1

print("--------------")
print(f"Your total score is {score}/{len(questions)}")
