# Bank Account Management System

A Python command-line application that simulates basic banking operations. This learning project explores object-oriented programming, inheritance, method overriding, modular design, and SQLite persistence.

## Features

- Open savings or checking accounts with an account number, holder name, and initial balance.
- Deposit money and withdraw funds using account-specific rules.
- Transfer funds between two existing accounts.
- View account details, balance, and account type.
- Save account data to SQLite and load it when the application starts.
- Validate menu choices, numeric input, empty names, and duplicate account numbers in the loaded account dictionary.

## Account Types

| Account type | Withdrawal rules | Additional behavior |
|---|---|---|
| `Bank_Account` | Positive withdrawals up to the available balance | Base class with deposits and balance lookup; not offered in the account-creation menu |
| `SavingsAccount` | Inherits the base withdrawal rules | Default interest rate of 2%; `apply_interest()` exists in the model but is not available in the CLI |
| `CheckingAccount` | Positive withdrawals up to the balance plus the overdraft limit | Default overdraft limit of $500 |

Interest is not applied automatically. Checking accounts do not currently charge overdraft fees.

## Project Architecture

| File | Responsibility |
|---|---|
| [`main.py`](./main.py) | Terminal menu, user input, operation handlers, and application loop |
| [`models.py`](./models.py) | Account classes, deposits, withdrawals, interest, and overdraft rules |
| [`bank.py`](./bank.py) | `Bank` class, account lookup and creation, and transfers |
| [`storage.py`](./storage.py) | `DataBase` class, SQLite table creation, saving, and rebuilding account objects |

The `Bank` class stores loaded accounts in a dictionary keyed by account number. Both account subclasses inherit shared behavior from `Bank_Account`. `CheckingAccount` overrides `withdraw()`, so the same withdrawal call applies different rules depending on the account object.

The balance is currently a public `balance` attribute; access is not restricted through a protected or private field.

## Requirements

- Python 3 with SQLite support
- No third-party packages

## Run

Clone the repository and enter its root directory:

```bash
git clone https://github.com/aarabmohamedamine/simple.python.projects.git
cd simple.python.projects
```

Create the database directory once, then launch the application:

```bash
python -c "from pathlib import Path; Path('Bank_Management/data').mkdir(parents=True, exist_ok=True)"
python Bank_Management/main.py
```

Run these commands from the **repository root**. The database path in `storage.py` is relative to the working directory. SQLite creates `Bank_Management/data/bank.db` and its `accounts` table at startup, but the code does not create the parent directory.

On systems that use `python3`, replace `python` in the commands above with `python3`.

## Usage

Choose an option from the terminal menu:

1. **Open New Account** — enter an integer account number, a holder name, a non-negative initial deposit, and the account type.
2. **Deposit Money** — enter an existing account number and a positive amount.
3. **Withdraw Money** — enter an existing account number and an amount allowed by its account rules.
4. **Transfer Funds** — enter different sender and receiver account numbers and a positive amount.
5. **Check Balance & Details** — display the balance and savings interest rate or checking overdraft limit.
6. **Exit** — leave the application.

For example, create two accounts, deposit into the first, transfer part of its balance to the second, and use option 5 to inspect both balances.

## Data Storage

The `accounts` table stores an internal row ID, account number, holder name, balance, account type, interest rate, and overdraft limit. SQL values are passed using placeholders.

Account creation, successful CLI deposits and withdrawals, and transfers trigger database saves. At startup, stored rows are converted back into savings, checking, or base account objects.

## Current Limitations

- **Repeated saves can create duplicate rows.** `save_account()` uses `INSERT OR REPLACE`, but `account_number` has no unique constraint and the auto-generated primary key is omitted from inserts. Reloading collapses rows into a dictionary, but the query has no ordering guarantee for selecting the latest balance.
- **Transfers use separate commits.** The two account saves are not wrapped in one atomic database transaction.
- **Interest is model-only.** Calling `apply_interest()` changes the in-memory balance; a separate save is needed to persist it.
- Transaction history, authentication, account deletion, and overdraft fees are not implemented.
- Monetary values use floating-point numbers, and input validation does not explicitly reject non-finite values such as infinity.

These are areas for future improvement in this educational simulation.

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)

[Back to the repository overview](../README.md)
