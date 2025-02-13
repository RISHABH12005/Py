import math
def vol(d, h):
    r = d/ 2
    volume = math.pi * (r ** 2) * h
    return volume
d = float(input("Enter the diameter: "))
h = float(input("Enter the height: "))
volume = vol(d, h)
print(f"The volume of the cylinder is: {volume:.2f} cubic units")
