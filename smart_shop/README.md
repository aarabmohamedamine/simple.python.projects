# Smart Shop

A small Python command-line shopping-cart application that stores products and calculates their combined price.

## Features

- Add a product with a name and price
- Reject non-numeric and non-positive prices
- View all products in the cart
- Calculate the total price
- Save the cart between sessions in JSON format

## Architecture

- `main.py` loads the cart and controls the menu loop.
- `operation.py` handles menu input, price validation, product operations, and total calculation.
- `storage.py` reads and writes the product list with Python's `json` module.
- `smart.json` is generated automatically inside this directory when the first product is saved.

## Run

From the repository root:

```bash
python smart_shop/main.py
```

No third-party packages are required.

## Author

**Mohamed Amine Aarab**

- Computer Engineering Student at ENSAH
- [LinkedIn](https://www.linkedin.com/in/aarabmedamine/)
- [GitHub](https://github.com/aarabmohamedamine)
