''' Write a Python class to implement function pow(x, n) '''
class Power:
    def pow(self, x, n):
        result = 1
        for _ in range(abs(n)):
            result *= x
        if n < 0:
            result = 1 / result
        return result
x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
power = Power()
print(f"{x} is to the power {n} is: {power.pow(x, n)}")
