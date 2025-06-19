Balance = 0
is_running = True

def show_balance():
    print(f"Your Current Balance is: {Balance}")

def Deposit():
    global Balance
    depo = int(input("How much do you want to deposit: "))
    Balance += depo
    print("Deposit successful.")

def Withdraw():
    global Balance
    if Balance > 0:
        wit = int(input("How much do you want to withdraw: "))
        if wit > Balance:
            show_balance()
            print("You can't withdraw that much money.")
        else:
            Balance -= wit
            print("Withdrawal successful.")
    else:
        print("Your balance is 0, bro!")

while is_running:
    print("\nWelcome to the Banking Program")
    print("Select an Option:")
    print("1. Deposit")
    print("2. Show Balance")
    print("3. Withdraw")
    print("Q. Quit")
    
    choice = input("Your Option: ").strip()

    if choice == "1":
        Deposit()
    elif choice == "2":
        show_balance()
    elif choice == "3":
        Withdraw()
    elif choice.lower() == "q":
        is_running = False
        print("Thank you for using our banking system!")
    else:
        print("Invalid option. Try again.")
