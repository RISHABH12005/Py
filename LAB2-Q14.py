# If the total selling price of 15 items and the total profit earned on them is input through the keyboard, write a python program to find the cost price of one item.
total selling price = float(input("Enter the total selling price of 15 items: "))
total profit = float(input("Enter the total profit earned on 15 items: "))
total cost price = total selling price-total profit
cost price per item = total cost price / 15
print(f"The cost price of 1 item is: {cost price per item}")
