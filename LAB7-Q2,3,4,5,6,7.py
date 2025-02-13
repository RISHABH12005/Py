''' 2. Write a python script to create a dictionary D1, enter details of the students in the form of enrolment and name (See details from the file “Std Record.pdf” ). 
3. Write a python script to create a dictionary D2, enter details of the students in the form of enrolment and City (hometown) it belongs to. 
4. Write a python script to create a dictionary D3, enter details of the students in the form of enrolment and mobile. 
5. Write a python script to create a dictionary D4, enter details of the students in the form of enrolment and State it belongs to. 
6. Write a python script to create a dictionary D5, enter details of the students in the form of enrolment and marks in Phy,Chem, and Maths. 
7. Write a python script to create a dictionary D6, enter details of the students in the form of enrolment and email-id.'''
students = [
    {"enrolment": "1001", "name": "Alice", "city": "Delhi", "mobile": "9876543210", "state": "Delhi", 
     "marks": {"Phy": 85, "Chem": 90, "Maths": 88}, "email": "alice@gmail.com"},
    {"enrolment": "1002", "name": "Bob", "city": "Mumbai", "mobile": "9876543222", "state": "Maharashtra", 
     "marks": {"Phy": 95, "Chem": 89, "Maths": 92}, "email": "bob@yahoo.com"},
     ]
D1 = {s["enrolment"]: s["name"] for s in students}
D2 = {s["enrolment"]: s["city"] for s in students}
D3 = {s["enrolment"]: s["mobile"] for s in students}
D4 = {s["enrolment"]: s["state"] for s in students}
D5 = {s["enrolment"]: s["marks"] for s in students}
D6 = {s["enrolment"]: s["email"] for s in students}
print("D1:", D1)
print("D2:", D2)
print("D3:", D3)
print("D4:", D4)
print("D5:", D5)
print("D6:", D6)
