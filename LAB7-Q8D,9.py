''' Q8D Write a python script to display students’ details who are from same hometown.
Q9 Write a python script to display students’ details who are from same State. '''
def city(city):
    return [D1[enrolment] for enrolment, c in D2.items() if c == city]
def state(state):
    return [D1[enrolment] for enrolment, s in D4.items() if s == state]
city = input("Enter hometown: ")
print(city(city))
state = input("Enter state: ")
print(state(state))
