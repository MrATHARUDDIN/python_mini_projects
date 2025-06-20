import random


def spin_row():
   symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
   return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("************************")
    print(" / ".join(row))
    print("************************")
def payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*3
        if row[0] == "🍉":
            return bet*5
        if row[0] == "🍋":
            return bet*10
        if row[0] == "🔔":
            return bet*15
        if row[0] == "⭐":
            return bet*20
    return 0

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
        print_row(row)
        winnings = payout(row, bet)

        if winnings > 0:
            print(f"🎉 You won ${winnings}!")
            balance += winnings
        else:
            print("😢 Sorry, you lost this round.")
    print("💸 Game Over! You ran out of money.")

if __name__ == "__main__":
    main()
