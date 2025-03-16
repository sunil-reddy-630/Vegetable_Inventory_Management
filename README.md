# Vegetable Inventory Management System

This is a simple vegetable inventory management system implemented in Python. It allows the owner to manage the inventory and users to purchase items from the inventory.

## Features

- Owner login to manage inventory
- User login to purchase items
- Add, remove, and update items in the inventory
- View inventory and user details
- Generate billing and profit/loss report

## Code Flow

1. **Initialization**:
   - The code initializes the inventory with predefined vegetables, their quantities, prices, and cost prices.
   - It also sets up the owner's username and password.

2. **Main Menu**:
   - The user is presented with a main menu to choose between Owner Login, User Login, or Exit.

3. **Owner Login**:
   - The owner must enter the correct username and password to access the owner menu.
   - The owner menu provides options to:
     - Add items to the inventory
     - Remove items from the inventory
     - Update item details
     - View the current inventory
     - View user details
     - View a detailed report of sales and profits
     - View total revenue and itemized profit/loss.

4. **User Login**:
   - The user must enter their name and a valid 10-digit phone number.
   - The user menu provides options to:
     - Add items to the cart
     - Remove items from the cart
     - Modify the quantity of items in the cart
     - View the cart
     - Proceed to billing

5. **Billing**:
   - The total amount is calculated based on the items in the user's cart.
   - The profit/loss for each item is updated.
   - The user's purchase details are stored, and the cart is cleared.

6. **Exit**:
   - The program exits when the user chooses the exit option from the main menu.

## Sample Output

```
1. Owner Login
2. User Login
3. Exit
Enter your choice: 1
Enter owner username: sunil
Enter owner password: password123

Owner Menu
1. Add Items to Inventory
2. Remove Item
3. Update Item
4. View Inventory
5. View User Details
6. View Report
7. Total Revenue and Itemized Profit
8. Exit
Enter your choice: 4
brinjal ---> 10 kgs
tomato ---> 20 kgs
carrot ---> 15 kgs

1. Owner Login
2. User Login
3. Exit
Enter your choice: 2
Enter customer name: John
Enter customer phone number: 1234567890

User Menu
1. Add to Cart
2. Remove from Cart
3. Modify Cart
4. View Cart
5. Billing
6. Exit
Enter your choice: 1
Enter item name: tomato
Enter quantity: 5

User Menu
1. Add to Cart
2. Remove from Cart
3. Modify Cart
4. View Cart
5. Billing
6. Exit
Enter your choice: 5
Please pay amount: 50
```

This README provides a comprehensive overview of the code, its flow, and sample output to help users understand how the system works.