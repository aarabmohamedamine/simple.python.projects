# CLI Contact Manager

A Python command-line contact manager built around a `ContactManager` class and SQLite persistence.

## 📌 Features

- **Contact Management**: Add, view, search, update, and delete contacts.
- **Contact Details**: Store a name, phone number, and email address.
- **Name Lookup**: Search by a full name using case-insensitive matching.
- **SQLite Persistence**: Create the database table automatically and commit changes using parameterized SQL.

## 📁 Project Structure

```text
contact_manager/
├── main.py          # CLI menu and application loop
├── operations.py    # ContactManager class and database operations
├── contact.db       # SQLite database created on startup
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher with the standard library modules `sqlite3`.
- No third-party packages required.

### Installation & Setup

1. Clone the repository and enter its root directory:

   ```bash
   git clone https://github.com/aarabmohamedamine/simple.python.projects.git
   cd simple.python.projects
   ```

### Running the Application

Run from the **repository root**, because storage paths are relative to the working directory:

```bash
python contact_manager/main.py
```

If your system uses `python3`, replace `python` with `python3` in these commands.

## 🖥️ Usage Guide

1. **Add contact**: Enter the name, phone number, and email address.
2. **View all contacts**: Display the stored database rows.
3. **Search for a contact**: Enter the full name; matching ignores letter case.
4. **Delete a contact**: Delete contacts matching the supplied name.
5. **Update contact**: Find contacts by name, then choose `1` to change the phone number or `2` to change the email.
6. **Exit**: Close the application.

Names are not unique. Updating or deleting by name affects every matching row. Phone numbers and email addresses are stored as entered without format validation.

## 🗄️ Database Schemas

### `contact.db` (`contact_list` Table)

| Field | Type | Description |
|---|---|---|
| `id_user` | `INTEGER` | Primary key with auto-increment |
| `user_name` | `TEXT` | Contact name, stripped and title-cased when added |
| `phone` | `TEXT` | Phone number |
| `email` | `TEXT` | Email address |


## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)
