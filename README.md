# Python CLI Projects

A collection of small command-line applications built while learning Python and software-engineering fundamentals. The projects practise modular design, input validation, JSON file handling, SQLite databases, and CRUD-style operations.

## Projects

| Project | What it does | Storage | Main concepts |
|---|---|---|---|
| [To-Do List](./to_do_list/) | Adds, lists, completes, deletes, and clears tasks | SQLite | CRUD operations, SQL, timestamps, modules |
| [Expense Tracker](./expense_tracker/) | Records expenses, lists them, and calculates the total | JSON | File persistence, dictionaries, aggregation |
| [Contact Manager](./contact_manager/) | Adds, lists, searches, updates, and deletes contacts | SQLite | OOP, parameterized SQL, CRUD operations |
| [Smart Shop](./smart_shop/) | Adds products, lists them, and calculates the cart total | JSON | Input validation, persistence, modular design |

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

Each application presents an interactive terminal menu. Its SQLite database or JSON data file is created automatically after data is first stored.

## Repository Structure

```text
simple.python.projects/
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
