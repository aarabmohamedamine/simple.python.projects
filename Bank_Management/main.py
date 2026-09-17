# main.py
from bank import Bank
from models import Bank_Account, SavingsAccount, CheckingAccount

def display_menu():
    print("\n" + "=" * 35)
    print("    BANK ACCOUNT MANAGEMENT SYSTEM")
    print("=" * 35)
    print("1. Open New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Funds")
    print("5. Check Balance & Details")
    print("6. Exit")
    print("=" * 35)

def get_valid_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            print("[ERROR] Please enter a valid number between 1 and 6.")
        except ValueError:
            print("[ERROR] Invalid input. Numbers only.")

def handle_open_account(bank):
    print("\n--- Open New Account ---")
    try:
        acc_num = int(input("Enter Account Number: "))
    except ValueError:
        print("[ERROR] Account number must be an integer.")
        return

    name = input("Enter Account Holder Name: ").strip()
    if not name:
        print("[ERROR] Name cannot be empty.")
        return

    try:
        initial_balance = float(input("Enter Initial Deposit ($): "))
        if initial_balance < 0:
            print("[ERROR] Initial balance cannot be negative.")
            return
    except ValueError:
        print("[ERROR] Balance must be a valid numerical value.")
        return

    print("Select Account Type:")
    print("1. Savings Account (2% default interest)")
    print("2. Checking Account ($500 overdraft limit)")
    acc_type_choice = input("Enter type (1/2): ").strip()

    if acc_type_choice == "1":
        account = SavingsAccount(acc_num, name, initial_balance)
    elif acc_type_choice == "2":
        account = CheckingAccount(acc_num, name, initial_balance)
    else:
        print("[ERROR] Invalid account type selected.")
        return

    success, message = bank.add_account(account)
    print(message)

def handle_deposit(bank):
    print("\n--- Deposit Funds ---")
    try:
        acc_num = int(input("Enter Account Number: "))
        account = bank.get_account(acc_num)
        if not account:
            print(f"[ERROR] Account #{acc_num} not found.")
            return

        amount = input("Enter Deposit Amount ($): ")
        success, message = account.deposit(amount)
        print(message)
        if success:
            bank.storage.save_account(account)
    except ValueError:
        print("[ERROR] Invalid input.")

def handle_withdraw(bank):
    print("\n--- Withdraw Funds ---")
    try:
        acc_num = int(input("Enter Account Number: "))
        account = bank.get_account(acc_num)
        if not account:
            print(f"[ERROR] Account #{acc_num} not found.")
            return

        amount = input("Enter Withdrawal Amount ($): ")
        success, message = account.withdraw(amount)
        print(message)
        if success:
            bank.storage.save_account(account)
    except ValueError:
        print("[ERROR] Invalid input.")

def handle_transfer(bank):
    print("\n--- Transfer Funds ---")
    try:
        from_acc = int(input("Enter Sender Account Number: "))
        to_acc = int(input("Enter Receiver Account Number: "))
        amount = float(input("Enter Amount to Transfer ($): "))
        
        success, message = bank.transfer(from_acc, to_acc, amount)
        print(message)
    except ValueError:
        print("[ERROR] Invalid numeric input for transfer.")

def handle_view_account(bank):
    print("\n--- Account Details ---")
    try:
        acc_num = int(input("Enter Account Number: "))
        account = bank.get_account(acc_num)
        if not account:
            print(f"[ERROR] Account #{acc_num} not found.")
            return

        print(f"Account Number : #{account.account_number}")
        print(f"Holder Name    : {account.holder_name}")
        print(f"Current Balance: ${account.get_balance():.2f}")
        
        if isinstance(account, SavingsAccount):
            print(f"Account Type   : Savings (Interest Rate: {account.interest_rate * 100:.1f}%)")
        elif isinstance(account, CheckingAccount):
            print(f"Account Type   : Checking (Overdraft Limit: ${account.overdraft_limit:.2f})")
    except ValueError:
        print("[ERROR] Account number must be an integer.")

def main():
    bank = Bank()

    while True:
        display_menu()
        choice = get_valid_choice()

        if choice == 1:
            handle_open_account(bank)
        elif choice == 2:
            handle_deposit(bank)
        elif choice == 3:
            handle_withdraw(bank)
        elif choice == 4:
            handle_transfer(bank)
        elif choice == 5:
            handle_view_account(bank)
        elif choice == 6:
            print("\n[INFO] Thank you for banking with us. Goodbye!")
            break

if __name__ == "__main__":
    main()