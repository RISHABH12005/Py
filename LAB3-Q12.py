# Compute the volume of a rectangular prism, when its all sides are given
def volume(l, w, h):
    volume = l * w * h
    return volume
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
volume = volume(l, w, h)
print(f"The volume of the rectangular prism is: {volume:.2f} cubic units")
