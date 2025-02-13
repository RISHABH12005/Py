# Compute the area of circle, when its diameter is given.
import math
d= 10
def area(d):
    r = d / 2
    return math.pi * r * r
area = area(d)
print(area)
