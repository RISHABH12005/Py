''' Write a python script to display students’ details who scored highest average marks in Phy, Chem, and Maths among all. '''
def average():
    return max(students, key=lambda s: (s["Phy"] + s["Chem"] + s["Maths"]) / 3)
print("Highest Average Marks:",average())
