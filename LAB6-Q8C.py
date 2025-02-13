'''  Write a python script to print name and city of the student  by mobile number at run time. '''
def mobile(mobile):
    for enrolment, mob in D3.items():
        if mob == mobile:
            return D1[enrolment], D2[enrolment]
    return None
mobile = input("Enter mobile no: ")
print(mobile(mobile))
