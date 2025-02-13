# Write a program to find LCM of two numbers.
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)
n1 = int(input("Enter the 1 no.: "))
n2 = int(input("Enter the 2 no.: "))
lcm = find_lcm(n1, n2)
print(f"The LCM of {n1} & {n2} is: {lcm}")
