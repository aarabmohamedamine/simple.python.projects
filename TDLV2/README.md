# TDLV2 — To-Do List with User Accounts

A Python command-line task manager with account registration, login, and SQLite persistence. Each logged-in user can add, view, and complete their own tasks.

This learning project brings together modular programming, authentication flow, parameterized SQL, and persistent data storage.

## Features

- **Account registration:** checks for an existing username and requires a matching password confirmation with at least six characters.
- **Login:** checks credentials and allows up to three password attempts per login call.
- **Personal task lists:** associates tasks with a username and filters task viewing and completion by the logged-in user.
- **Add tasks:** saves new tasks with a `Pending` status.
- **View tasks:** prints the user's saved task records.
- **Mark tasks as done:** matches task names case-insensitively and updates their status to `done`.
- **Persistent storage:** saves accounts and tasks in separate SQLite databases.
- **Menu validation:** handles nonnumeric and out-of-range menu choices.

A **Delete Task** menu option is present, but its database path needs correction before it can work as intended.

## Requirements

- Python 3
- Git, if cloning the repository

No third-party Python packages are required. The application uses the standard-library `sqlite3` and `datetime` modules.

## Getting Started

Clone the repository and enter its root directory:

```bash
git clone https://github.com/aarabmohamedamine/simple.python.projects.git
cd simple.python.projects
```

Ensure the database directory exists, then start the application:

```bash
python -c "from pathlib import Path; Path('TDLV2/data').mkdir(parents=True, exist_ok=True)"
python TDLV2/app.py
```

Use `python3` instead of `python` if that is the Python command on your system.

**Run these commands from the repository root.** Database paths are relative to the current working directory, so running `python app.py` from inside `TDLV2` will not resolve them correctly.

The repository includes database files. If they are absent, SQLite creates them when their corresponding operations run, provided that `TDLV2/data/` exists. Tables are initialized with `CREATE TABLE IF NOT EXISTS`.

## Usage

1. Choose **1. Sign In (Create Account)** to register.
2. Enter a username and a password of at least six characters, then confirm the password.
3. After registration, choose **2. Log In**. Creating an account does not automatically log you in.
4. Use the task menu:

| Option | Action |
|---|---|
| 1. Add Task | Save a task for the current user |
| 2. View Tasks | Display the current user's task records |
| 3. Mark Done | Complete tasks matching the entered name |
| 4. Delete Task | Currently affected by an incorrect database path |
| 5. Log Out | End the session and exit the application |

Task records are displayed as Python tuples in this order:

```text
(task_id, user_name, task, status, time)
```

For example, a newly added task may appear as:

```text
(1, 'demo_user', 'Review Python modules', 'Pending', '14:30')
```

Marking a task as done changes its status to `done` and replaces the stored time with the completion time.

## Project Structure

| Path | Responsibility |
|---|---|
| `app.py` | Entry point, authentication menu, current-user state, and task menu |
| `SL.py` | User-table initialization, username lookup, registration, and login |
| `operations.py` | Task-table initialization, adding, viewing, completing, and deleting tasks |
| `data/users.db` | SQLite account database |
| `data/tasks.db` | SQLite task database |

`app.py` calls functions from `SL.py` to authenticate the user, then passes the logged-in username to functions in `operations.py`.

## Data Model

### Accounts: `users.db` → `users`

| Column | SQL type | Purpose |
|---|---|---|
| `name` | TEXT | Username |
| `password` | TEXT | Password, currently stored as plain text |
| `time` | TEXT | Registration time in `HH:MM` format |

Username duplication is checked by application code; the table does not declare a unique constraint.

### Tasks: `tasks.db` → `task_list`

| Column | SQL type | Purpose |
|---|---|---|
| `id_user` | INTEGER PRIMARY KEY AUTOINCREMENT | Task record ID, despite the column's name |
| `user_name` | TEXT | Username associated with the task |
| `task` | TEXT | Task description |
| `status` | TEXT | `Pending` or `done` |
| `date` | TEXT | Creation time, replaced by completion time when marked done |

Both time fields contain only hours and minutes, without a calendar date. The two databases are linked logically by username, with no database-enforced foreign key.

## Author

**Mohamed Amine Aarab**

[LinkedIn](https://www.linkedin.com/in/aarabmedamine/)

[GitHub](https://github.com/aarabmohamedamine)
