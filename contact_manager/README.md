# Contact Manager

A Python command-line application for managing contacts in a local SQLite database.

## Features

- Add a contact with a name, phone number, and email
- View all saved contacts
- Search for a contact by name, case-insensitively
- Update a contact's phone number or email
- Delete contacts by name
- Keep data between sessions with SQLite

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
