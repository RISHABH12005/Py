# A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input through the keyboard in tens, hundreds or thousands, find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.
amount = int(input("Enter the amount to be withdrawn: "))
notes_100 = amount // 100
amount %= 100
notes_50 = amount // 50
amount %= 50
notes_10 = amount // 10
print(f"Number of 100 denomination notes: {notes_100}")
print(f"Number of 50 denomination notes: {notes_50}")
print(f"Number of 10 denomination notes: {notes_10}")
