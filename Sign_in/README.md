# CLI User Account Manager

A Python command-line learning project for user registration, login, password changes, and administrator-managed accounts using SQLite.

## 📌 Features

- **Account Registration**: Check whether a username exists, then generate a six-digit user ID and a 5–10 character alphanumeric password.
- **Login**: Compare the supplied password with the stored account record, with up to three attempts per call.
- **Password Changes**: Request the current password and a new password of at least six characters.
- **Admin Dashboard**: View, add, delete, and update users after checking the administrator credentials defined in `admin.py`.
- **SQLite Persistence**: Store user records and registration or password-change times.

## 📁 Project Structure

```text
Sign_in/
├── main.py          # Main account menu
├── models.py        # User class, generators, login, password changes
├── admin.py         # Admin credential check and CRUD operations
├── data/
│   └── users.db     # Created when account/admin operations initialize it
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher with the standard library modules `sqlite3`, `random`, `string`, `datetime`.
- No third-party packages required.

### Installation & Setup

1. Clone the repository and enter its root directory:

   ```bash
   git clone https://github.com/aarabmohamedamine/simple.python.projects.git
   cd simple.python.projects
   ```

2. Create the database directory before using the application:

   ```bash
   python -c "from pathlib import Path; Path('Sign_in/data').mkdir(parents=True, exist_ok=True)"
   ```

### Running the Application

Run from the **repository root**, because storage paths are relative to the working directory:

```bash
python Sign_in/main.py
```

If your system uses `python3`, replace `python` with `python3` in these commands.

## 🖥️ Usage Guide

### 1. Account Menu

1. **Create account**: Enter a username and note the generated user ID and password.
2. **Log in**: Enter the username and generated or updated password.
3. **Change password**: Enter the account name, current password, and a new password of at least six characters.
4. **Admin mode**: Use the administrator credentials configured in `admin.py` to open the dashboard.
5. **Exit**: Close the application.

### 2. Admin Dashboard

1. **View users**: Display the full stored rows, including password values.
2. **Delete user**: Remove a user by name.
3. **Update user**: Change a username or password.
4. **Add user**: Supply a name and password; an ID and registration time are generated.
5. **Exit**: Return to the account menu.

Passwords are stored as plaintext, and the administrator credentials are hard-coded. This is a learning exercise, not production authentication. Generated IDs have no uniqueness constraint. The lock message does not persist a lockout, and password changes after an incorrect attempt can fail because the connection is closed.

## 🗄️ Database Schemas

### `users.db` (`users` Table)

| Field | Type | Description |
|---|---|---|
| `id` | `INTEGER` | Primary key with auto-increment |
| `name` | `TEXT` | Username; normal registration checks names without case sensitivity |
| `user_id` | `TEXT` | Generated six-digit identifier |
| `password` | `TEXT` | Plaintext password |
| `last_update` | `TEXT` | Registration or user password-change time (HH:MM) |

Admin edits do not refresh `last_update`; admin additions also bypass the normal registration checks. The table is initialized by account operations or admin mode, not merely by displaying the main menu.

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)
