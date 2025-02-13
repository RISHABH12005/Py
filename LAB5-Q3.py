# Write a python function to check whether three given numbers can form the sides of a triangle.
def triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    else:
        return False
a = float(input("Enter 1 side: "))
b = float(input("Enter 2 side: "))
c = float(input("Enter 3 side: "))
if triangle(a, b, c):
    print("The No. can form a triangle.")
else:
    print("The No. can't form a triangle.")
