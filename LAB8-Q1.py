''' Write a Python class which has two methods get_String and print_String.
get_String accept a string from the user and print_String print the string in upper case. '''
class methord:
    def __init__(self):
        self.inputs = ""
    def get_String(self):
        self.inputs = input("Enter a string: ")
    def print_String(self):
        print(self.inputs.upper())
processor = methord()
processor.get_String()
processor.print_String()
