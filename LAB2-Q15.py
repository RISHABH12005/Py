n = input("Enter a 5-digit no.: ")
if len(no.) != 5 or not no..isdigit():
    print("Please enter a valid 5-digit no.")
else:
    new_no. = ""
    for digit in no:
        new_digit = (int(digit) + 1) % 10
        new_no. += str(new_digit)
    print("The new no. is:", new_no.)