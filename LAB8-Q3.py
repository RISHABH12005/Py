''' Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. '''
import math
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * (self.r ** 2)
    def perimeter(self):
        return 2 * math.pi * self.r
r = float(input("Enter the radius: "))
circle = Circle(r)
print(f"The area is: {circle.area():.2f}")
print(f"The perimeter is: {circle.perimeter():.2f}")
