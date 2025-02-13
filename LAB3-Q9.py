# Compute the area of a cylinder, when its height and diameter is given.
import math
d= 10
h = 15
def area(d,h):
    r = d / 2
    return 2 * math.pi * r * (r + h)
area = area(d,h)
print(area)
