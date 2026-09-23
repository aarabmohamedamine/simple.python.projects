# CLI Smart Shop

A Python command-line shopping-cart application for storing products and calculating their combined price with JSON persistence.

## 📌 Features

- **Product Entry**: Add a product name and a positive whole-number price.
- **Price Validation**: Retry non-numeric, zero, and negative prices.
- **Cart Overview**: View products and calculate the cart total.
- **JSON Persistence**: Reload the cart at startup and save after each addition.

## 📁 Project Structure

```text
smart_shop/
├── main.py          # Application loop and cart loading
├── operation.py     # Menu, validation, and product operations
├── storage.py       # JSON loading and saving
├── smart.json       # Created on the first save
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
python smart_shop/main.py
```

If your system uses `python3`, replace `python` with `python3` in these commands.

## 🖥️ Usage Guide

1. **Add product**: Enter its name and a positive integer price.
2. **View products**: Display all products as dictionaries.
3. **View total**: Sum the prices in the cart.
4. **Exit**: Close the application.

## 🗄️ Data Storage

### `smart.json`

The file contains a JSON array of product objects. A missing file starts an empty cart; adding a product writes the complete list.

| Field | Type | Description |
|---|---|---|
| `Product name` | `string` | Product label; key includes a space |
| `Price` | `integer` | Positive whole-number price |

```json
[
  {"Product name": "Notebook", "Price": 25}
]
```

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)
