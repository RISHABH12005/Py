''' Write a python script to receive a list in input in single line input.
Use eval command to convert string input to list. 
(sample input out similar as above) '''
lists = eval(input("Enter a list: "))
print(f"List of length {len(lists)}")
print(f"List is {lists}")
