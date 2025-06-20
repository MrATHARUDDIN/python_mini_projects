import random



payout_multipliers = {
    "🍒": 2,
    "🍉": 3,
    "🍋": 5,
    "🔔": 10,
    "⭐": 20
}

def spin_row():
   symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
   return [random.choice(symbols) for _ in range(3)]

def print_row():
    pass

def payout():
    pass

def main():
    balance = 100

    print("************************")
    print("🎰 Welcome to Py Slots! 🎰")
    print("Symbols: 🍒  🍉  🍋  🔔  ⭐")
    print("************************")

    while balance > 0:
        print(f"\nCurrent Balance: ${balance}")
        bet_input = input("Enter your bet amount: ")

        if not bet_input.isdigit():
            print("❌ Please enter a valid number.")
            continue

        bet = int(bet_input)

        if bet <= 0:
            print("❌ Bet must be greater than zero.")
            continue
        if bet > balance:
            print("❌ Insufficient balance.")
            continue
        balance -= bet
        row = spin_row()
        print(row)
        
    print("💸 Game Over! You ran out of money.")

if __name__ == "__main__":
    main()
