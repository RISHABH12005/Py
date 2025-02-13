# Given a list of integer values. Write a python program to check whether it contains same number in adjacent position. Display the count of such adjacent occurrences.
def occurr(integer):
    c = 0
    for i in range(len(integer) - 1):
        if integer[i] == integer[i + 1]:
            c += 1
    return c
in1 = [1, 1, 5, 100, -20, -20, 6, 0, 0]
in2 = [10, 20, 30, 40, 30, 20]
in3 = [1, 2, 2, 3, 4, 4, 4, 10]
print(occurr(in1))
print(occurr(in2))
print(occurr(in3))
