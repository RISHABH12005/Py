''' Write a python to show  if there exists list, tuple in a given string input. 
Sample Input: [1,2,3,4] 
Sample Output: List 
Sample Input: [1,2,(3,4),5] 
Sample Output: List, tuple 
Sample Input: (1, 2,[3,4],5) 
Sample Output: tuple, list '''
def detect_list(input_string):
    lists = "[" in strings and "]" in strings
    tuples = "(" in strings and ")" in strings
    result = []
    if lists:
        result.append("List")
    if tuples:
        result.append("Tuple")
    return ", ".join(result)
strings = input("Enter a string: ")
print(detect_list(strings))
