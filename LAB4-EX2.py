# reading 5 times in a list
# Methord-1:
list_1=[None]*5
i=0
while i<5:
	a=input("Enter the List Items %d:"%i)
	list_1[i]=a
	i=i+1
print("The List 1 is ",list_1)

# Methord-2:
list_2=[]
i=0
while i<5:
	b=input("Enter list Items %d:"%i)
	list_2.append(b)
	i=i+1
print("The List 2 is ",list_2)

# Methord-3:
list_3=[]
for i in range(5):
	c=input("The list Items %d:"%i)
	list_3.append(c)
print("The List 3 is ",list_3)
