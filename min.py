# '''veg=['brinjal','tomato','carrot']
# quantity=[10,20,15]
# price=[15,10,20]
# owner_username='sunil'
# while True:
#     item=input('what do you want:')
#     if item in veg:
#         qty=float(input('enter how much quntity do want:'))
#         idx=veg.index(item)
#         if qty<=quantity[idx]:
#             amount=qty*price[idx]
#             print('plese pay amount',amount)
#             quantity[idx]=quantity[idx]-qty
#         else:
#             print('out of stock')
#     else:
#         print('item is not avaliable')
#     ch=input('do you want to close the shop(yes/no):')
#     if ch=='yes':
#         print('closed..')
#         print('*'*10,'REPORT','*'*10)
#         for it in zip(veg,quantity):
#             print(it[0],'--->',it[1],'kgs')
            
#         break'''
# '''veg = ['brinjal', 'tomato', 'carrot']
# quantity = [10, 20, 15]
# price = [15, 10, 20]
# cost_price = [12, 8, 15]  # Cost prices added
# owner_username = 'sunil'
# owner_password = 'password123'

# # Owner login
# while True:
#     username = input('Enter owner username: ')
#     password = input('Enter owner password: ')
#     if username == owner_username and password == owner_password:
#         print('Login successful')
#         break
#     else:
#         print('Invalid credentials!')

# customer_details = []
# item_profit_loss = {veg[i]: 0 for i in range(len(veg))}

# while True:
#     customer_name = input('Enter customer name: ')
#     while True:
#         customer_phone = input('Enter customer phone number: ')  # Phone number input
#         if customer_phone.isdigit() and len(customer_phone) == 10:
#             break
#         else:
#             print('Invalid phone number! Please enter a valid 10-digit phone number.')

#     item = input('What do you want: ')
#     if item in veg:
#         qty = float(input('Enter how much quantity do you want: '))
#         idx = veg.index(item)
#         if qty <= quantity[idx]:
#             amount = qty * price[idx]
#             print('Please pay amount:', amount)
#             quantity[idx] -= qty
#             profit = amount - (qty * cost_price[idx])  # Calculate profit
#             customer_details.append((customer_name, customer_phone, item, qty, amount, profit))  # Added phone and profit
#             item_profit_loss[item] += profit  # Track itemized profit/loss
#         else:
#             print('Out of stock')
#     else:
#         print('Item is not available')

#     ch = input('Do you want to close the shop (yes/no): ')
#     if ch.lower() == 'yes':
#         print('Closed..')
#         print('*' * 10, 'REPORT', '*' * 10)
#         for it in zip(veg, quantity):
#             print(it[0], '--->', it[1], 'kgs')

#         print('*' * 10, 'CUSTOMER DETAILS', '*' * 10)
#         for detail in customer_details:
#             print('Name:', detail[0], '---> Phone:', detail[1], '---> Item:', detail[2], '---> Quantity:', detail[3], 'kgs ---> Amount:', detail[4], '---> Profit:', detail[5])

#         total_profit = sum(item_profit_loss.values())
#         print('*' * 10, 'ITEMIZED PROFIT/LOSS', '*' * 10)
#         for item, profit_loss in item_profit_loss.items():
#             print(f'{item}: {profit_loss}')
#         print(f'Total Profit/Loss: {total_profit}')
#         break'''


veg = ['brinjal', 'tomato', 'carrot']
quantity = [10, 20, 15]
price = [15, 10, 20]
cost_price = [12, 8, 15]  # Cost prices added
owner_username = 'sunil'
owner_password = 'password123'

user_cart = {}
customer_details = []
item_profit_loss = {veg[i]: 0 for i in range(len(veg))}

while True:
    print("\n1. Owner Login")
    print("2. User Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter owner username: ")
        password = input("Enter owner password: ")
        if username == owner_username and password == owner_password:
            while True:
                print("\nOwner Menu")
                print("1. Add Items to Inventory")
                print("2. Remove Item")
                print("3. Update Item")
                print("4. View Inventory")
                print("5. View User Details")
                print("6. View Report")
                print("7. Total Revenue and Itemized Profit")
                print("8. Exit")
                owner_choice = int(input("Enter your choice: "))
                if owner_choice == 8:
                    break

                if owner_choice == 1:
                    item = input("Enter item name: ")
                    qty = int(input("Enter quantity: "))
                    prc = int(input("Enter price: "))
                    cp = int(input("Enter cost price: "))
                    if item in veg:
                        idx = veg.index(item)
                        quantity[idx] += qty
                        price[idx] = prc
                        cost_price[idx] = cp
                    else:
                        veg.append(item)
                        quantity.append(qty)
                        price.append(prc)
                        cost_price.append(cp)
                if owner_choice == 2:
                    item = input("Enter item name to remove: ")
                    if item in veg:
                        idx = veg.index(item)
                        veg.pop(idx)
                        quantity.pop(idx)
                        price.pop(idx)
                        cost_price.pop(idx)
                    else:
                        print("Item not found")
                if owner_choice == 3:
                    item = input("Enter item name to update: ")
                    if item in veg:
                        idx = veg.index(item)
                        qty = int(input("Enter new quantity: "))
                        prc = int(input("Enter new price: "))
                        cp = int(input("Enter new cost price: "))
                        quantity[idx] = qty
                        price[idx] = prc
                        cost_price[idx] = cp
                    else:
                        print("Item not found")
                if owner_choice == 4:
                    for item, qty in zip(veg, quantity):
                        print(f"{item} ---> {qty} kgs")
                if owner_choice == 5:
                    print("User Cart Details:")
                    for item, qty in user_cart.items():
                        print(f"{item}: {qty} kgs")
                if owner_choice == 6:
                    for item, qty in zip(veg, quantity):
                        print(f"{item} ---> {qty} kgs")
                    print("\nCustomer Details:")
                    for detail in customer_details:
                        print(f"Name: {detail[0]}, Phone: {detail[1]}, Item: {detail[2]}, Quantity: {detail[3]}, Amount: {detail[4]}, Profit: {detail[5]}")
                if owner_choice == 7:
                    total_profit = sum(item_profit_loss.values())
                    print("\nItemized Profit/Loss:")
                    for item, profit_loss in item_profit_loss.items():
                        print(f"{item}: {profit_loss}")
                    print(f"Total Profit/Loss: {total_profit}")

    elif choice == 2:
        customer_name = input('Enter customer name: ')
        while True:
            customer_phone = input('Enter customer phone number: ')
            if customer_phone.isdigit() and len(customer_phone) == 10:
                break
            else:
                print('Invalid phone number! Please enter a valid 10-digit phone number.')

        while True:
            print("\nUser Menu")
            print("1. Add to Cart")
            print("2. Remove from Cart")
            print("3. Modify Cart")
            print("4. View Cart")
            print("5. Billing")
            print("6. Exit")
            user_choice = int(input("Enter your choice: "))
            if user_choice == 6:
                break

            if user_choice == 1:
                item = input("Enter item name: ")
                qty = int(input("Enter quantity: "))
                if item in veg:
                    if item in user_cart:
                        user_cart[item] += qty
                    else:
                        user_cart[item] = qty
                else:
                    print("Item not available")
            if user_choice == 2:
                item = input("Enter item name to remove: ")
                if item in user_cart:
                    user_cart.pop(item)
                else:
                    print("Item not in cart")
            if user_choice == 3:
                item = input("Enter item name to modify: ")
                if item in user_cart:
                    qty = int(input("Enter new quantity: "))
                    user_cart[item] = qty
                else:
                    print("Item not in cart")
            if user_choice == 4:
                print("Cart Details:")
                for item, qty in user_cart.items():
                    print(f"{item}: {qty} kgs")
            if user_choice == 5:
                total = 0
                for item, qty in user_cart.items():
                    if item in veg:
                        idx = veg.index(item)
                        total += qty * price[idx]
                        item_profit_loss[item] += qty * (price[idx] - cost_price[idx])
                print(f"Please pay amount: {total}")
                customer_details.append((customer_name, customer_phone, item, qty, total, item_profit_loss[item]))
                user_cart.clear()

    elif choice == 3:
        break

























    
