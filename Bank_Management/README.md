# Bank Account Management System

A Python command-line educational banking simulation using object-oriented programming, inheritance, method overriding, and SQLite storage.

## 📌 Features

- **Account Creation**: Open savings or checking accounts with a number, holder name, and initial balance.
- **Banking Operations**: Deposit, withdraw, transfer funds, and view account details.
- **Account Rules**: Savings withdrawals use the available balance; checking withdrawals allow a default $500 overdraft.
- **SQLite Storage**: Save account records and rebuild account objects on startup.
- **Input Validation**: Check numeric input, non-empty holder names, and duplicate account numbers in the loaded dictionary.

## 📁 Project Structure

```text
Bank_Management/
├── main.py          # CLI menus and operation handlers
├── models.py        # Bank_Account, SavingsAccount, CheckingAccount
├── bank.py          # Account dictionary, creation, lookup, transfers
├── storage.py       # SQLite persistence and object reconstruction
├── data/
│   └── bank.db      # Created after the data directory exists
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher with the standard library modules `sqlite3`.
- No third-party packages required.

### Installation & Setup

1. Clone the repository and enter its root directory:

   ```bash
   git clone https://github.com/aarabmohamedamine/simple.python.projects.git
   cd simple.python.projects
   ```

2. Create the database directory before using the application:

   ```bash
   python -c "from pathlib import Path; Path('Bank_Management/data').mkdir(parents=True, exist_ok=True)"
   ```

### Running the Application

Run from the **repository root**, because storage paths are relative to the working directory:

```bash
python Bank_Management/main.py
```

If your system uses `python3`, replace `python` with `python3` in these commands.

## 🖥️ Usage Guide

1. **Open New Account**: Enter an integer account number, holder name, non-negative initial deposit, and account type.
2. **Deposit Money**: Enter an existing account number and a positive amount.
3. **Withdraw Money**: Enter an amount allowed by the account's withdrawal rules.
4. **Transfer Funds**: Enter different sender and receiver account numbers and a positive amount.
5. **Check Balance & Details**: Display the balance and account-specific settings.
6. **Exit**: Close the application.

### Account Types

| Class | Withdrawal rule | Additional behavior |
|---|---|---|
| `Bank_Account` | Up to the available balance | Base class; not offered in the creation menu |
| `SavingsAccount` | Inherits the base rule | Default 2% interest; `apply_interest()` is model-only |
| `CheckingAccount` | Up to the balance plus the overdraft limit | Default $500 limit; no overdraft fees |

Interest is not applied automatically or exposed in the CLI. Applying it in code changes memory and requires a separate save. Account balances are public attributes.

## 🗄️ Database Schemas

### `bank.db` (`accounts` Table)

| Field | Type | Description |
|---|---|---|
| `id_user` | `INTEGER` | Primary key with auto-increment |
| `account_number` | `INTEGER` | Account number; no database uniqueness constraint |
| `holder_name` | `TEXT` | Account holder |
| `balance` | `REAL` | Current balance |
| `account_type` | `TEXT` | Savings, Checking, or Standard |
| `interest_rate` | `REAL` | Savings interest rate; otherwise NULL |
| `overdraft_limit` | `REAL` | Checking overdraft limit; otherwise NULL |

Account creation, successful deposits and withdrawals, and transfers trigger saves. The database and table are created at startup after the parent directory exists.

**Storage behavior:** `INSERT OR REPLACE` can append duplicate account rows because `account_number` is not unique and the primary key is omitted. Loading collapses rows into a dictionary without a query ordering guarantee. Transfers save each account in a separate commit, so they are not atomic. Monetary amounts use floating-point values. Transaction history is not implemented.

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)
