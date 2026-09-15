# Expense Tracker

A simple Python command-line application for recording expenses and calculating how much has been spent.

## Features

- Add an expense with an integer amount, category, and description
- View all recorded expenses
- Calculate the total of all expense amounts
- Save data between sessions in JSON format
- Handle non-numeric amount input without stopping the program

## Architecture

- `main.py` loads saved data, displays the menu, and controls the application loop.
- `operations.py` adds, displays, and totals expenses.
- `storage.py` loads and saves the expense list with Python's `json` module.
- `expenses.json` is generated automatically inside this directory when the first expense is saved.

## Run

From the repository root:

```bash
python expense_tracker/main.py
```

No third-party packages are required.

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)
