# Budget App - freeCodeCamp Certification Project

This repository contains my solution for the "Budget App" project, a requirement for the freeCodeCamp "Scientific Computing with Python" certification.

## Project Overview

This project is an object-oriented budget application built in Python. It features a `Category` class to manage different budget categories like food, clothing, and entertainment. The application allows for depositing, withdrawing, and transferring funds between categories.

A key feature of this project is the `create_spend_chart` function, which generates a bar chart that visually represents the percentage of spending for each category.

---

## Key Features & Skills Demonstrated

### 1. Object-Oriented Programming (OOP )
*   **Class-Based Design:** The core logic is encapsulated within a `Category` class, managing its own state (name, ledger) and behaviors (deposit, withdraw, transfer).
*   **Object Interaction:** The `transfer` method demonstrates how objects of the same class can interact with each other, a fundamental concept in OOP.

### 2. Advanced String Formatting & Manipulation
*   **`__str__` Method:** A custom `__str__` method is implemented to provide a clean, formatted, and human-readable representation of a budget category's ledger, including a title, itemized transactions, and a running total.
*   **Chart Generation:** The `create_spend_chart` function involves complex string manipulation to build a visual bar chart from calculated data, including aligned labels, bars made of characters, and vertically printed category names.

### 3. Algorithmic Logic
*   **Data Processing:** The application processes transaction data to calculate total spending per category and overall spending percentages.
*   **Conditional Logic:** Robust `check_funds` logic is implemented to prevent overdrafts, ensuring data integrity.

---

## How to Use

The project is designed to be used by instantiating `Category` objects and calling their methods.

```python
# Example Usage
food = Category("Food")
clothing = Category("Clothing")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.transfer(50, clothing)

# Print the food category ledger
print(food)

# Generate and print the spending chart
print(create_spend_chart([food, clothing]))
