''' Pure Gems Store sells different varieties of gems to its customers.
Emerald, Ivory, Jasper, Ruby, Garnet and their prices are 1760, 2119, 1599, 3920, 3999 respectively.
Write a Python program to calculate the bill amount to be paid by a customer based on the list of gems and quantity purchased. 
Any purchase with a total bill amount above Rs.30000 is entitled for 5% discount. 
If any gem required by the customer is not available in the store, then consider total bill amount to be -1.
Assume that quantity required by the customer for any gem will always be greater than 0.
Perform case-sensitive comparison wherever applicable. '''
store = (
    ("Emerald", 1760),
    ("Ivory", 2119),
    ("Jasper", 1599),
    ("Ruby", 3920),
    ("Garnet", 3999))
def bill(gems, quantities):
    total = 0
    for i in range(len(gems)):
        found = False
        for gem in store:
            if gem[0] == gems[i]:
                total += gem[1] * quantities[i]
                found = True
                break
        if not found:
            return -1
    if total > 30000:
        total *= 0.95
    return total
purchased = ["Emerald", "Ruby"]
quantities = [10, 5]
totals = bill(purchased, quantities)
if totals == -1:
    print("One or more gems are not available.")
else:
    print(f"Total bill amount: ₹{totals:.2f}")
