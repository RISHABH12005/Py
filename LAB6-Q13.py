'''Write a python script to take two values as string and convert it into a multiple lists which appears like matrix.
(See sample input and output) 
Sample string input: 3 5 
Sample O/P: 
[0, 0, 0, 0, 0] 
[0, 1, 2, 3, 4] 
[0, 2, 4, 6, 8] 
Sample string input: 5 5 
Sample O/P: 
[0, 0, 0, 0, 0 ] 
[0, 1, 2, 3, 4 ] 
[0, 2, 4, 6, 8 ] 
[0, 3, 6, 9, 12] 
[0, 4, 8, 12, 16] '''
def matrix(row, col):
    return [[i * j for j in range(col)] for i in range(row)]
row, col = map(int, input("Enter rows & cols: ").split())
matrix = matrix(row, col)
for row in matrix:
    print(row)
