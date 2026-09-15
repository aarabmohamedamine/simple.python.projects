# To-Do List

A Python command-line application for managing tasks with persistent SQLite storage.

## Features

- Add a task with a default `Pending` status
- Record the task creation time as hours and minutes
- View all tasks
- Mark a task as done
- Delete a task by name
- Clear the entire task list

## Architecture

- `Main.py` displays the interactive menu and controls the application loop.
- `operation.py` creates the database table and implements the task operations.
- `tasks.db` is generated automatically inside this directory when the application runs.

Contact with SQLite uses Python's built-in `sqlite3` module, and query values are supplied through SQL placeholders.

## Run

File names are case-sensitive on Linux. From the repository root, use:

```bash
python to_do_list/Main.py
```

No third-party packages are required.

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)
