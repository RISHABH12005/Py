# Write a program to find HCF (GCD) of two numbers.
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n1 = int(input("Enter the 1 no.: "))
n2 = int(input("Enter the 2 no.: "))
gcd = find_gcd(n1, n2)
print(f"The HCF (GCD) of {n1} & {n2} is: {gcd}")
