E-Shopping and Billing System Using Simple Python
1. Introduction

The E-Shopping and Billing System is a console-based Python application designed to simulate a simple online shopping experience. It allows users to browse a product catalog, add items to a shopping cart, and generate a final bill with GST included. The system is built entirely using core Python, making it lightweight, easy to understand, and suitable for beginners.
📝 Problem Statement

The goal of this project is to design and implement a simple console-based E-Shopping System using basic Python programming constructs. The system should allow a user to view a list of available products, add selected items to a shopping cart with chosen quantities, and finally generate a detailed bill that includes item totals, subtotal, and GST.

The problem focuses on building a menu-driven, easy-to-use system that mimics a minimal online shopping experience without using any external libraries, databases, web technologies, or graphical interfaces. The emphasis is on demonstrating the effective use of Python data structures, conditional logic, functions, and input validation to create a functional application.

✔ The system must be able to:

Display a product catalog

Each product has an ID, name, and price

Catalog must be shown clearly to the user

Allow the user to add products to a shopping cart

User inputs product ID and quantity

System validates entries

Cart stores selected items and updates quantities

Generate a final bill

Show each item purchased with its quantity, price, and total

Calculate subtotal

Apply 18% GST

Display the grand total

Print a clean invoice

Provide a simple menu-based interface

Show Catalog

Add to Cart

Generate Bill

Exit

Handle invalid user input gracefully

Invalid product IDs

Invalid quantities

Non-numeric input

🎯 Purpose of the Problem

The purpose of this problem is to help learners practice:

How to use Python dictionaries to store catalog data

How to implement a cart system

How to design a loop-based console interface

How to generate bills using arithmetic operations

How to handle user errors safely

How to simulate a basic e-commerce workflow

2. Objective

The primary objectives of this project are:

To demonstrate the use of basic Python programming concepts such as loops, conditionals, functions, and dictionaries.

To create a simple, user-friendly shopping and billing system without frontend or backend frameworks.

To provide a practical example of how data structures and console-based menus can be used to create a real-world application.

3. Scope of the Project

This project covers the following functionalities:

Displaying a product catalog

Adding items to a shopping cart

Validating user inputs

Calculating totals for items purchased

Applying GST (18%)

Generating a clean invoice

Allowing the user to exit anytime

The project does not include:

GUI (Graphical User Interface)

Database storage

User authentication

Online payment processing

The simplicity of the system makes it suitable for academic demonstrations and foundational learning.

4. Technologies Used

This system is implemented purely in Python, using:

Python Core Language

Variables

Dictionaries

Loops

Functions

Exception handling (try-except)

Console I/O (input and print)

No external libraries, web technologies, or frameworks are used.

5. System Requirements

Software: Python 3.x

Hardware: Any basic PC capable of running Python

No additional dependencies or installations required

6. System Design
6.1 Catalog Module

Uses a dictionary to store product ID, name, and price.

Displayed in a table format.

6.2 Shopping Cart

Stores product ID and quantity in a dictionary.

Ensures valid inputs before adding items.

6.3 Billing Module

Calculates:

Item-wise totals

Subtotal

GST at 18%

Final payable amount

Displays an invoice in structured format.

6.4 Menu System

Menu-based navigation allows users to:

View catalog

Add items

Generate invoice

Exit

7. Advantages of the System

Simple and easy to use

No external libraries required

Teaches essential Python concepts

Fast and lightweight

Ideal for beginners and students

8. Conclusion

The E-Shopping and Billing System successfully demonstrates how a simple yet functional shopping program can be developed using only Python fundamentals. It highlights the importance of data structures, input validation, and modular coding practices. This console-based billing system serves as an excellent learning tool for understanding real-world application logic in Python.

9. Future Enhancements

Possible improvements include:

Adding item removal from cart

Applying discounts or promo codes

Using files or databases to save products and bills

Converting the system into a GUI or web application

Adding user accounts and authentication



10.🎯 Target Users

Even though the project is small and console-based, it is still aimed at specific user groups:

1. Students Learning Python

Beginners who want to understand:

Data structures

Functions

Input handling

Menu-driven programs

Basic billing logic

2. Teachers / Instructors

Educators can use this system as:

A demonstration of Python fundamentals

A practical mini-project for assignments

A simple example for teaching loops, dictionaries, and functions

3. Small-scale Shopkeepers (Conceptual)

Although console-based, it models:

Basic product selection

Item-wise billing

GST calculation

Useful for understanding how billing systems work.

4. Beginners Building Portfolio Projects

Those who want:

A simple, clean Python project

No frameworks or external libraries

Easy to extend into GUI or web app later

11.⭐ High-Level Features

These represent the main capabilities of the system:

1. Product Catalog Display

Shows a list of all available products

Includes product ID, name, and price

Structured in readable table format

2. Shopping Cart System

Users can select items using product ID

Add multiple quantities of the same item

Cart automatically updates if item is already added

Handles invalid inputs

3. Billing and Invoice Generation

Calculates item-wise totals

Computes subtotal

Adds 18% GST

Displays final Grand Total

Prints a complete invoice in a professional layout

4. Menu-Driven User Interface

Simple options to:

Show catalog

Add to cart

Generate bill

Exit

Repeats until the user chooses to exit

5. Input Validation

Prevents errors by checking:

Invalid product IDs

Non-numeric input

Negative or zero quantities

Ensures program does not crash

6. Fully Offline, No Dependencies

Runs in any basic Python environment

Does not require internet, database, or frameworks

7. Lightweight and Extendable

Easy to add:

More products

Discounts

Item removal

File-based bill storage

GUI or web version
