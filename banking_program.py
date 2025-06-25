Balance = 0
is_running = True
transactions = []
def show_balance():
    print(f"Your Current Balance is: {Balance}")

def Deposit():
    global Balance
    try:
        depo = int(input("How much do you want to deposit: "))
        if depo <= 0:
            print("⚠️ Please enter a positive amount.")
            return
        Balance += depo
        transactions.append(f"Deposited: {depo}")
        print("✅ Deposit successful.")
    except ValueError:
        print("⚠️ Enter a valid number.")

def Withdraw():
    global Balance
    try:
        if Balance > 0:
            wit = int(input("How much do you want to withdraw: "))
            if wit <= 0:
                print("⚠️ Enter a positive amount.")
            elif wit > Balance:
                show_balance()
                print("❌ You can't withdraw more than your balance.")
            else:
                Balance -= wit
                transactions.append(f"Withdrew: {wit}")
                print("✅ Withdrawal successful.")
        else:
            print("❌ Your balance is 0, bro!")
    except ValueError:
        print("⚠️ Enter a valid number.")

def show_transactions():
    if transactions:
        print("\n---- 📜 Transaction History ----")
        for t in transactions:
            print(t)
    else:
        print("\nNo transactions yet.")


while is_running:
    print("\nWelcome to the Banking Program")
    print("Select an Option:")
    print("1. Deposit")
    print("2. Show Balance")
    print("3. Withdraw")
    print("4. Show Transaction History")
    print("Q. Quit")
    
    choice = input("Your Option: ").strip()

    if choice == "1":
        Deposit()
    elif choice == "2":
        show_balance()
    elif choice == "3":
        Withdraw()
    elif choice == "4":
        show_transactions()
    elif choice.lower() == "q":
        is_running = False
        print("Thank you for using our banking system!")
    else:
        print("Invalid option. Try again.")
