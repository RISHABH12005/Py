'''  Write a python script to receive a dictionary in single line input without using eval command. '''
strings = input("Enter a dictionary (e.g., key1:value1, key2:value2): ")
dict_items = strings.split(", ")
input_dict = {k: v for k, v in (item.split(":") for item in dict_items)}
print(f"Dictionary is {input_dict}")
