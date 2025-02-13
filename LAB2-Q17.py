import math
n = int(input("Enter an integer: "))
cube_root = round(n** (1 / 3))
if cube_root ** 3 == n:
    print(f"The number is a perfect cube. The integer cube root is: {cube_root}")
else:
    print("The number is not a perfect cube.")
