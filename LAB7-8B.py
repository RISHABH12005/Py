'''  Write a python script to print name and enrolment number of the student  by receiving email id at run time. '''
def email(email):
    for enrolment, e in D6.items():
        if e == email:
            return D1[enrolment], enrolment
    return None
email = input("Enter email: ")
print(email(email))
