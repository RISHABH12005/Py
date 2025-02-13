''' Write a program to find a substring within a string. If found display its starting position. '''
string=input("Enter the string ")
substring=input("Enter te substring ")
locat=string.find(substring)
if locat != -1:
    print(f"The Substring is found{substring}")
else:
    print("The Substring is not found ")
