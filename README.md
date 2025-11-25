# E-shopping-with-product-catalog-
E-ShopLite lets users browse a product catalog, search and filter products, add items to a shopping cart, and simulate checkout. Admin interface allows adding/editing products. Data stored in SQLite. The project demonstrates modular design (routes, models, templates), basic algorithms (search with substring matching, category filter, sorting.

🛒 Project: Simple E-Shopping Program (Console Based)

This project is a simple, menu-driven e-shopping application built entirely in Python.
It allows users to:

View a Product Catalog

Add items to a Shopping Cart

Generate a Final Bill with GST (18%)

Exit the program

It does not use frontend, backend, frameworks, or external libraries—only core Python.

PROJECT STRUCTURE:

e_shopping_python/
│
├── main.py          # Complete E-Shopping Program
├── README.md        # Project documentation

⚙ Technologies Used

This project uses only basic Python features:

✔ Python (Core Language Features)

Variables and data types

Dictionaries for product catalog

Loops and conditionals

Functions

Error handling with try-except

Simple arithmetic operations

Console input/output

✔ No External Libraries Needed

This is a pure Python implementation—
No Flask, Django, HTML, CSS, JSON files, or databases are used.

✔ Suitable For

Beginners learning Python

Students preparing for assignments

Simple console-based billing & shopping logic

🧾 Features
1. Product Catalog

Displays products with ID, name, and price

Stored in a Python dictionary

Clean table-like format

2. Add Items to Cart

Enter Product ID

Enter quantity

Supports multiple items and repeated additions

Handles invalid input

3. Generate Final Bill

Shows:

Product name

Quantity

Price

Total per item

Computes:

Subtotal

GST (18%)

Grand Total

Well-formatted invoice display

4. User-Friendly Menu

Loop-based menu for navigation

Program exits after bill is generated

▶ How to Run the Program
Prerequisites

Python 3 installed

Run the Program

Open terminal in project folder and run:

python main.py


Menu will appear:

===== E-SHOPPING MENU =====
1. Show Catalog
2. Add to Cart
3. Generate Bill
4. Exit

🧪 Testing Instructions

Follow these test cases to verify the program works as expected:

✅ Test Case 1: Display Catalog

Steps:

Run program

Select option 1

Expected:
Shows list of all products.

✓ Test Case 2: Add Valid Product

Steps:

Select 2

Enter product ID (e.g., 3)

Enter quantity (e.g., 2)

Expected:
✔ Item added to cart!

❌ Test Case 3: Add Invalid Product ID

Steps:

Select option 2

Enter ID: 10

Expected:
❌ Invalid product ID!

❌ Test Case 4: Invalid Quantity

Steps:

Select option 2

Enter ID 1

Enter quantity: 0 or -2

Expected:
❌ Invalid quantity!

✓ Test Case 5: Generate Bill

Steps:

Add a few items

Select option 3

Expected:

Detailed invoice

Subtotal

GST (18%)

Grand Total

Program exits automatically afterward.

❌ Test Case 6: Bill With Empty Cart

Steps:

Start program

Select option 3

Expected:
❌ Your cart is empty!

📝 Notes

The project uses "₹" (Indian Rupees). You can change the currency anytime.

Very easy to expand—just add more items to the catalog dictionary.

Ideal for demonstrating Python logic, loops, functions, and basic billing systems.


Screenshots 
<img width="926" height="758" alt="image" src="https://github.com/user-attachments/assets/dba69d21-e5d0-4bcf-912b-bd57053b8e66" />
<img width="1080" height="544" alt="Screenshot 2025-11-25 174632" src="https://github.com/user-attachments/assets/83232ab9-a397-4967-b000-3721d2693360" />
