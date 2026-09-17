# bank.py
from storage import DataBase

class Bank:
    def __init__(self):
        self.storage = DataBase()
        
        self.accounts = self.storage.load_accounts()

    def add_account(self, account):
        if account.account_number in self.accounts:
            return False, "[ERROR] Account already exists."
        
        self.accounts[account.account_number] = account
        self.storage.save_account(account)
        return True, f"[SUCCESS] Account #{account.account_number} created successfully."

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.get_account(from_acc_num)
        to_acc = self.get_account(to_acc_num)

        if not from_acc:
            return False, f"[ERROR] Source account #{from_acc_num} not found."
        if not to_acc:
            return False, f"[ERROR] Destination account #{to_acc_num} not found."
        if from_acc_num == to_acc_num:
            return False, "[ERROR] Cannot transfer to the same account."

        success, message = from_acc.withdraw(amount)
        if not success:
            return False, message

        to_acc.deposit(amount)

        self.storage.save_account(from_acc)
        self.storage.save_account(to_acc)

        return True, f"[SUCCESS] Transferred ${amount:.2f} from #{from_acc_num} to #{to_acc_num}."