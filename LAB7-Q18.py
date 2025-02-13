'''  Write a python script to create a dictionary odd to store first 50 odd numbers, their log2. '''
import math
odd = {i: math.log2(i) for i in range(1, 100) if i % 2 != 0}
print(odd)
