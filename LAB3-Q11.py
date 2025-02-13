# Compute the area of a rectangular prism, when its all sides are given
def area(l, w, h):
    area = 2 * (l * w + l* h + w * h)
    return area
l = float(input("Enter the length: "))
w = float(input("Enter the width: "))
he = float(input("Enter the height: "))
area = area(l, w, h)
print(f"The surface area of the rectangular prism is: {area:.2f} square units")
