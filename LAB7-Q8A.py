''' Write a python script to display students’ name and email by receiving enrolment number at run time. '''
def email(enrolment):
    if enrolment in D1 and enrolment in D6:
        return D1[enrolment], D6[enrolment]
    return None
enrolment = input("Enter enrolment no: ")
print(email(enrolment))
