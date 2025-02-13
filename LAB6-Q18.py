''' Write a python script to receive a list mentioned in Qu. 16 without using eval command. 
Sample Input: [1, 2, 3, 4, 5] 
Sample Output: list of length 5 
[1, 2, 3, 4, 5] '''
strings = input("Enter a list: ")
lists = list(map(int,strings.strip("[]").split(", ")))
print(f"List of length {len(lists)}")
print(f"List is {lists}")
