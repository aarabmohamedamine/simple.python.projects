# Python CLI Projects

A collection of six Python command-line applications built while learning modular design, object-oriented programming, input validation, JSON persistence, SQLite, and CRUD operations.

## 📌 Features

| Project | What it does | Storage | Main concepts |
|---|---|---|---|
| [To-Do List](./to_do_list/README.md) | Registers users and manages their personal tasks | SQLite | Login flow, CRUD, timestamps |
| [Expense Tracker](./expense_tracker/README.md) | Records expenses, lists entries, and calculates totals | JSON | Dictionaries, aggregation, file persistence |
| [Contact Manager](./contact_manager/README.md) | Adds, lists, searches, updates, and deletes contacts | SQLite | Classes, parameterized SQL, CRUD |
| [Smart Shop](./smart_shop/README.md) | Stores products and calculates the cart total | JSON | Input validation, modular design |
| [Bank Management](./Bank_Management/README.md) | Opens accounts and handles deposits, withdrawals, transfers, and balance lookup | SQLite | Inheritance, method overriding, persistence |
| [User Account Manager](./Sign_in/README.md) | Registers users, checks login, changes passwords, and provides admin CRUD | SQLite | Account workflows, generators, CRUD |

## 📁 Project Structure

```text
simple.python.projects/
├── Bank_Management/     # Banking simulation
├── Sign_in/             # User and admin account management
├── contact_manager/     # Contact CRUD and search
├── expense_tracker/     # Expense tracking
├── smart_shop/          # Shopping cart
├── to_do_list/          # Multi-user task management
└── README.md
```

Each project has a README covering features, structure, setup, usage, and its database schema or JSON format.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher with SQLite support.
- No third-party packages required; all projects use the Python standard library.

### Installation & Setup

1. Clone the repository and enter its root directory:

   ```bash
   git clone https://github.com/aarabmohamedamine/simple.python.projects.git
   cd simple.python.projects
   ```

2. Create the parent directories required by the SQLite projects:

   ```bash
   python -c "from pathlib import Path; [Path(p).mkdir(parents=True, exist_ok=True) for p in ('to_do_list/data', 'Bank_Management/data', 'Sign_in/data')]"
   ```

### Running the Applications

Run one application at a time from the **repository root**. Their data paths depend on this working directory.

| Application | Command |
|---|---|
| To-Do List | `python to_do_list/app.py` |
| Expense Tracker | `python expense_tracker/main.py` |
| Contact Manager | `python contact_manager/main.py` |
| Smart Shop | `python smart_shop/main.py` |
| Bank Management | `python Bank_Management/main.py` |
| User Account Manager | `python Sign_in/main.py` |

If your system uses `python3`, replace `python` with `python3`.

## 🖥️ Usage Guide

1. Choose a project and launch it using the command above.
2. Follow its numbered terminal menu to enter or view records.
3. Use its exit option when finished. To-Do List's Log Out option also ends the run.
4. Restart the same project from the repository root to reload saved data.

For To-Do List, create an account and then log in to access the task dashboard. User Account Manager is a separate application with its own accounts and admin menu. The linked project READMEs describe each menu and the current implementation's behavior.

## 🗄️ Data Storage

| Project | File | Format / table |
|---|---|---|
| To-Do List | `to_do_list/data/users.db` | SQLite: `users` |
| To-Do List | `to_do_list/data/tasks.db` | SQLite: `task_list` |
| Expense Tracker | `expense_tracker/expenses.json` | JSON array of expense objects |
| Contact Manager | `contact_manager/contact.db` | SQLite: `contact_list` |
| Smart Shop | `smart_shop/smart.json` | JSON array of product objects |
| Bank Management | `Bank_Management/data/bank.db` | SQLite: `accounts` |
| User Account Manager | `Sign_in/data/users.db` | SQLite: `users` |

JSON files are written when the first item is saved. SQLite files and tables are initialized by the relevant startup or operation code; the parent directories must already exist.

These are educational applications. The account projects store plaintext passwords. Bank Management can save duplicate account rows and uses separate commits for transfers; its README explains those storage behaviors.

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)
