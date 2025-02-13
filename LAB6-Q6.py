''' Write a script to input a string form the user and output the first non repeating character. '''
def repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None
