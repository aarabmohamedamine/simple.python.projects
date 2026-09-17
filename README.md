# Python CLI Projects

A collection of small command-line applications built while learning Python and software-engineering fundamentals. The projects practise modular design, object-oriented programming, input validation, JSON file handling, SQLite databases, and CRUD-style operations.

## Projects

| Project | What it does | Storage | Main concepts |
|---|---|---|---|
| [To-Do List](./to_do_list/) | Adds, lists, completes, deletes, and clears tasks | SQLite | CRUD operations, SQL, timestamps, modules |
| [Expense Tracker](./expense_tracker/) | Records expenses, lists them, and calculates the total | JSON | File persistence, dictionaries, aggregation |
| [Contact Manager](./contact_manager/) | Adds, lists, searches, updates, and deletes contacts | SQLite | OOP, parameterized SQL, CRUD operations |
| [Smart Shop](./smart_shop/) | Adds products, lists them, and calculates the cart total | JSON | Input validation, persistence, modular design |
| [Bank Management](./Bank_Management/) | Opens accounts, handles deposits, withdrawals and transfers, and displays balances | SQLite | Inheritance, polymorphism, account rules, persistence |

## Requirements

- Python 3
- No third-party packages are required

## Getting Started

Clone the repository and enter its root directory:

```bash
git clone https://github.com/aarabmohamedamine/simple.python.projects.git
cd simple.python.projects
```

Run a project from the repository root:

```bash
python to_do_list/Main.py
python expense_tracker/main.py
python contact_manager/main.py
python smart_shop/main.py
```

To run Bank Management, first create its database directory, then launch it from the repository root:

```bash
python -c "from pathlib import Path; Path('Bank_Management/data').mkdir(parents=True, exist_ok=True)"
python Bank_Management/main.py
```

Each application presents an interactive terminal menu. Data is stored in a local SQLite database or JSON file. Bank Management requires the parent directory shown above; SQLite creates its database at startup.

See the [Bank Management README](./Bank_Management/README.md) for account rules, architecture, and current persistence limitations.

## Repository Structure

```text
simple.python.projects/
├── Bank_Management/
├── contact_manager/
├── expense_tracker/
├── smart_shop/
└── to_do_list/
```

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)
