
class Bank_Account:
    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self,amount):
        try:
            amount = float(amount)
            if amount>0:
                self.balance += amount
                return True,"Deposit approved"
            else:
                return False , "Deposit amount must be greater than 0."
        except ValueError:
            return False , "Input error"
    def get_balance(self):
        return self.balance


    def withdraw(self,amount):
        try:
            amount = float(amount)
            if 0 < amount <= self.balance :
                self.balance -= amount
                return True,"Successfully withdrew"
            elif amount > self.balance:
                return False , "Transaction failed"
            else:
                return False , "Input error"
                 
        except ValueError:
            return False , "Input error"

class SavingsAccount(Bank_Account):
    def __init__(self,account_number,holder_name,balance,interest_rate=0.02):
        super().__init__(account_number,holder_name,balance)
        self.interest_rate = interest_rate 

    def apply_interest(self):
        interest = self.interest_rate * self.balance
        self.balance += interest
        return True , f"Interest of ${interest:.2f} applied. New balance: ${self.balance:.2f}"    


class CheckingAccount(Bank_Account):
    def __init__(self, account_number, holder_name, balance,overdraft_limit=500.00):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        try:
            amount = float(amount)
            self.balance = float(self.balance)
             
            if amount <= (self.balance + self.overdraft_limit) and amount > 0:
                self.balance -= amount
                return True , f"Successfully withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}"
            elif amount > (self.balance + self.overdraft_limit):
                return False , "Transaction failed: Overdraft limit exceeded"
            else :
                return False , "Input error"
        except ValueError:
                return False , "Input error"

