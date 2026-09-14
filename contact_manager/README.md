# Contact Manager Project

## Introduction
A CLI (Command Line Interface) application built with Python. It allows users to efficiently track and manage their contacts with persistent storage using a relational database (SQLite). The project has been fully refactored using Object-Oriented Programming (OOP) principles for better scalability, performance, and memory management.

## Project Architecture
The project follows Clean Architecture and OOP principles:

* **`ContactManager` Class (in `operations.py`)**: The core object of the application. It encapsulates the SQLite database connection (opening it only once upon instantiation) and handles all CRUD operations (Add, View, Search, Update, Delete). This ensures the DRY (Don't Repeat Yourself) principle is strictly followed.
* **`main.py`**: The entry point of the application. It handles the user interface (CLI menu), instantiates a single `ContactManager` object, and runs the main application loop.

## How to Run
1. Open your terminal in the project folder.
2. Run the following command:
   ```bash
   python main.py
## 👨‍💻 Author

**Mohamed Amine Aarab**
* Computer Engineering Student @ ENSAH
* LinkedIn: [Mohamed Amine Aarab](https://www.linkedin.com/in/aarabmedamine/)
* GitHub: [@aarabmohamedamine](https://github.com/aarabmohamedamine)
