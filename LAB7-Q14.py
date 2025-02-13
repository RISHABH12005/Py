''' Write a python script to display students’ details who scored highest marks in Maths among all. '''
def maths():
    return max(students, key=lambda s: s["Maths"])
print("Highest in Mathematics:",maths())
