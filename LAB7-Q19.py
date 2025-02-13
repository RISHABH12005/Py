''' Write a python to store prime numbers between 50 and100 along with their digit-sum. '''
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
sums = {n: sum(int(d) for d in str(n)) for n in range(50, 101) if prime(n)}
print(sums)
