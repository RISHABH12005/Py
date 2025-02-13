''' Write a python script to receive a tuple in input in single line input. Use eval command to 
convert string input to tuple. 
Sample Input: (10, 12, 33, 45, 50,60) 
Sample Output: tuple of length 6 
Tuple is (10, 12, 33, 45, 50,60) 
Sample Input: (10, 12,( 33, 45), 50,60) 
Sample Output: tuple of length 5 
Tuple is (10, 12, (33, 45), 50,60) '''
inputs = eval(input("Enter a tuple: "))
print(f"Tuple of length {len(inputs)}")
print(f"Tuple is {inputs}")