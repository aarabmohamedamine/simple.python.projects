import sqlite3
from models import SavingsAccount, CheckingAccount, Bank_Account

class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("Bank_Management/data/bank.db")
        cursor = self.connection.cursor()
        

        cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(

        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        account_number INTEGER,
        holder_name TEXT,
        balance REAL,
        account_type TEXT,
        interest_rate REAL,
        overdraft_limit REAL )""")
        self.connection.commit()

    def save_account(self,account):
        cursor = self.connection.cursor()

        if hasattr(account, "interest_rate"):
            account_type = "Savings"
            interest_rate = account.interest_rate
            overdraft_limit = None
        elif hasattr(account, "overdraft_limit"):
            account_type = "Checking"
            interest_rate = None
            overdraft_limit = account.overdraft_limit
        else:
            account_type = "Standard"
            interest_rate = None
            overdraft_limit = None

        data = (
            account.account_number,
            account.holder_name,
            account.balance,
            account_type,
            interest_rate,
            overdraft_limit)

        
        query = """INSERT OR REPLACE INTO accounts(account_number,holder_name,balance,account_type,interest_rate,overdraft_limit) VALUES(?,?,?,?,?,?)"""
        cursor.execute(query, data)
        self.connection.commit()
        
        return True

    def load_accounts(self):

        cursor = self.connection.cursor()
        cursor.execute("SELECT account_number, holder_name, balance, account_type, interest_rate, overdraft_limit FROM accounts")
        rows = cursor.fetchall()

        accounts = {}

        for row in rows:
            acc_num, name, balance, acc_type, interest_rate, overdraft_limit = row

            if acc_type == "Savings":
                account = SavingsAccount(acc_num, name, balance, interest_rate)
            elif acc_type == "Checking":
                account = CheckingAccount(acc_num, name, balance, overdraft_limit)
            else:
                account = Bank_Account(acc_num, name, balance)

            accounts[acc_num] = account

        return accounts

        
        