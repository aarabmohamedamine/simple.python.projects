# CLI To-Do List Application

A multi-user command-line interface (CLI) to-do list application built in Python using SQLite for persistent data storage.

## 📌 Features

* **User Authentication**:

  * Sign up with unique username validation and password length checks ($\ge 6$ characters).

  * Secure login handling with up to 3 password retry attempts.

* **Personalized Task Management**:

  * Each user's tasks are strictly separated by account.

  * Add tasks with automated duplicate prevention per user.

  * View tasks formatted cleanly in aligned columns with dynamic statuses and timestamps.

  * Mark pending tasks as completed (`Done`), updating the last modified timestamp.

  * Delete tasks safely with case-insensitive matching.

* **SQLite Persistence**:

  * Automatic database and table creation for both accounts and task lists.

## 📁 Project Structure

```
to_do_list/
│
├── accounts.py       # User registration, authentication, and user table setup
├── app.py            # Main interactive CLI application entrypoint & menus
├── operations.py     # Task CRUD operations (add, view, mark done, delete)
├── data/
│   ├── users.db      # SQLite database storing user credentials
│   └── tasks.db      # SQLite database storing tasks and statuses
└── README.md

```

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher installed on your machine.

* No third-party packages required (uses built-in standard libraries: `sqlite3`, `datetime`).

### Installation & Setup

1. **Clone or download** the project folder.

2. Ensure the directory structure matches the path layout, particularly creating the `data` folder inside `to_do_list`:

   ```
   mkdir -p to_do_list/data
   
   ```

### Running the Application

Execute the application from the root directory or directly run `app.py`:

```
python to_do_list/app.py

```

## 🖥️ Usage Guide

### 1. Account Menu

When running the script, choose:

* `1. Sign In (Create Account)`: Register with a new username and a password.

* `2. Log In`: Log into an existing profile.

* `3. Exit`: Exit the application.

### 2. Task Dashboard

Once authenticated, manage your personal task list:

* `1. Add Task`: Enter a task title (default status: `Pending`).

* `2. View Tasks`: Display all current tasks in formatted columns.

* `3. Mark Done`: Set a chosen task's status to `Done`.

* `4. Delete Task`: Remove a task from the database.

* `5. Log Out`: Return to the main authentication menu.

## 🗄️ Database Schemas

### `users.db` (`users` Table)

| Field | Type | Description | 
 | ----- | ----- | ----- | 
| `name` | `TEXT` | Username (unique check in code) | 
| `password` | `TEXT` | User password | 
| `time` | `TEXT` | Registration time (`HH:MM`) | 

### `tasks.db` (`task_list` Table)

| Field | Type | Description | 
 | ----- | ----- | ----- | 
| `id_user` | `INTEGER` | Primary key with auto-increment | 
| `user_name` | `TEXT` | Owner of the task | 
| `task` | `TEXT` | Description/title of the task | 
| `status` | `TEXT` | Task state (`Pending` or `Done`) | 
| `date` | `TEXT` | Time of creation or last update (`HH:MM`) | 

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)

