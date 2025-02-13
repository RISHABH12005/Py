''' 20. Write a script to print selected details of the student, asking user to keyin student’s name. 
21. Write a script to print all details of the student, asking user to keyin student’s Enrollment.
22. Write a script to print all details of the student, asking user to keyin student’s name. '''
def name(name):
    for enrolment, n in D1.items():
        if n == name:
            return {key: d[enrolment] for key, d in zip(["name", "city", "mobile", "state", "marks", "email"], [D1, D2, D3, D4, D5, D6])}
def enrolment(enrolment):
    return {key: d[enrolment] for key, d in zip(["name", "city", "mobile", "state", "marks", "email"], [D1, D2, D3, D4, D5, D6])}
name = input("Enter student name: ")
print(name(name))
enrolment = input("Enter enrolment no: ")
print(enrolment(enrolment))
