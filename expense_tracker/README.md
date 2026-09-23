# CLI Expense Tracker

A Python command-line application for recording expenses, viewing saved entries, and calculating their total using JSON persistence.

## 📌 Features

- **Expense Recording**: Add an integer amount, category, and description.
- **Expense Overview**: Display all entries and calculate their combined amount.
- **Input Handling**: Retry when an amount or menu choice is not numeric.
- **JSON Persistence**: Load saved expenses at startup and save after each addition.

## 📁 Project Structure

```text
expense_tracker/
├── main.py          # CLI menu and application loop
├── operations.py    # Add, view, and total expenses
├── storage.py       # JSON loading and saving
├── expenses.json    # Created on the first save
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher with the standard library modules `json`.
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
python expense_tracker/main.py
```

If your system uses `python3`, replace `python` with `python3` in these commands.

## 🖥️ Usage Guide

1. **Add an expense**: Enter a whole-number amount, category, and description.
2. **View all expenses**: Display every saved expense as a dictionary.
3. **Show total expenses**: Sum the amounts of all recorded entries.
4. **Exit**: Close the application.

Amounts are integers; the current input check also accepts zero and negative values.

## 🗄️ Data Storage

### `expenses.json`

The file contains a JSON array of expense objects. A missing file starts an empty list; adding an expense writes the complete list.

| Field | Type | Description |
|---|---|---|
| `amount` | `integer` | Expense amount |
| `category` | `string` | User-entered category |
| `description` | `string` | User-entered description |

```json
[
  {"amount": 50, "category": "Transport", "description": "Bus ticket"}
]
```

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)
