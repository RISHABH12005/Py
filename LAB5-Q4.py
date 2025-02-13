''' Execute the program triangle.py available in the folder.
The program triangle.py is written to display "*" as per the expected output given below.
But the code is having logical errors, debug the program and correct it.

# debug the below code
counter1=0
counter2=5
while counter1<5:
	start=''
	while counter2>counter1:
		start=start+ "*"
		counter2-=1
	print(start)
	counter1+=1 

Output:
*****
Expected Output:
*****
****
***
**
*    '''
counter1 = 0
while counter1 < 5:
    start = ''
    counter2 = 5
    while counter2 > counter1:
        start += "*"
        counter2 -= 1
    print(start)
    counter1 += 1
