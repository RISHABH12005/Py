''' Read elements into a list and show output by printing each elements
Sample Input           Expected Output 
1,5,7,8,3.14, 4, 5     1 5 7 8 3.14 4 5 
1,[2,3],4,5,6          1 2 3 4 5 6 
1,2,[3,4,5],[6,7]      1 2 3 4 5 6 7 
[(1,2,3)]              1 2 3            '''
def list(input_list):
    for element in input_list:
        if type(element) in [list, tuple]:
            list(element)
        else:
            print(element, end=" ")
    print()
in1 = [1, 5, 7, 8, 3.14, 4, 5]
in2 = [1, [2, 3], 4, 5, 6]
in3 = [1, 2, [3, 4, 5], [6, 7]]
in4 = [(1, 2, 3)]
list(in1)
list(in2)
list(in3)
list(in4)
