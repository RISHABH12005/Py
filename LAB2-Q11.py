# If the marks obtained by a student in five different subjects are input through the keyboard, find out the aggregate marks and percentage marks obtained by the student. Assume that the maximum marks that can be obtained by a student in each subject is 100.
Maths= float(input("Enter marks for Maths: "))
English=float(input("Enter marks for English: "))
Physics=float(input("Enter marks for Physics: "))
Hindi=float(input("Enter marks for Hindi: "))
Chemistry=float(input("Enter marks for Chemistry: "))
Aggregate Marks=Maths+English+Physics+Hindi+Chemistry
Percentage Marks=(Aggregate Marks/100) * 100
print("Aggregate Marks",Aggregate Marks)
print("Percentage Marks",Percentage Marks)
