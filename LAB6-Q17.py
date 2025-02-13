  ''' Write a python script to receive a tuple mentioned in Qu. 15 without using eval command. 
Sample Input: (1, 2, 3, 4, 5) 
Sample Output: tuple of length 5 
(1, 2, 3, 4, 5) '''
strings = input("Enter a tuple: ")
tuples = tuple(map(int,strings.strip("()").split(", ")))
print(f"Tuple of length {len(tuples)}")
print(f"Tuple is {tuples}")
