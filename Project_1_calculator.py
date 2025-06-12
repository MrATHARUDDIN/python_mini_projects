# Functions for operations
def plus(x, y):
    print("Result:", x + y)

def minus(x, y):
    print("Result:", x - y)

def multiplication(x, y):
    print("Result:", x * y)

def division(x, y):
    if y == 0:
        print("Error: Division by zero")
    else:
        print("Result:", x / y)

def square(x):
    print("Result:", x * x)

def exponential(x, y):
    print("Result:", x ** y)

    #the the condition and frontend
print("Hello came to terminal calculator ")
print("-----------------------------------------------")
print("")
print("1 (+) plus")
print("2 (-) minous")
print("3 (*) matiplication")
print("4 (/) Division")
print("5 (x^2) square")
print("6 (x^x) exponantinal")
print("")
print("-----------------------------------------------")
chose = int(input("Enter Your Choise Oparation : "))
print("Enter 2 number to calculate")
if(chose<5): 
    x = int(input("Enter Your First number : "))
    y = int(input("Enter Your Second number : "))
if(chose==5):
    x = int(input("Enter Your number that you wnat to square : "))
if(chose==6):
    x = int(input("Enter Your base number : "))
    y = int(input("Enter Your exponantinal : "))

match chose:
    case 1:
        plus(x, y)
    case 2:
        minus(x, y)
    case 3:
        multiplication(x, y)
    case 4:
        division(x, y)
    case 5:
        square(x)
    case 6:
        exponential(x, y)


