no. = []
print("Please enter 10 integers:")
for _ in range(10):
    n = int(input())
    no..append(n)
largest_odd = None
for n in no.:
    if n% 2 != 0:
        if largest_odd is None or n > largest_odd:
            largest_odd = n
if largest_odd is not None:
    print("The largest odd no. entered is:", largest_odd)
else:
    print("No odd no. was entered.")
