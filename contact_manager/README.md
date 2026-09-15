# Contact Manager Project

## Introduction
A CLI (Command Line Interface) application built with Python. It allows users to efficiently track and manage their contacts, featuring a search functionality and persistent storage using a relational database (SQLite).

## Project Architecture
The project follows the Separation of Concerns principle, dividing the codebase into functional modules:

* **`operations.py`**: Contains the core logic for the application. It handles the database connection (SQLite) and manages all CRUD operations (Add, View, Update, Delete) as well as the Search functionality.
* **`main.py`**: The entry point of the application. It handles the user interface (CLI menu) and the main application loop.

## Architecture

- `main.py` displays the menu, creates one `ContactManager` instance, and controls the application loop.
- `operations.py` contains input handling and the `ContactManager` class, which creates the database table and performs the contact operations.
- `contact.db` is generated automatically inside this directory when the application runs.

SQL values are passed with placeholders rather than being inserted directly into query strings.

## Run

From the repository root:

```bash
python contact_manager/main.py
```

* No third-party packages are required.

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)

