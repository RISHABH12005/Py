''' Write a python program to solve a classic ancient Chinese puzzle.
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits
and how many chickens do we have?
Sample Input                Expected Output
heads-150 legs-400          100 50
heads-3 legs-11             No solution
heads-3 legs-12             0 3
heads-5 legs-10             5 0 '''
def puzzle(heads, legs):
    rabbits = (legs - 2 * heads) // 2
    chickens = heads - rabbits
    if rabbits >= 0 and chickens >= 0 and (legs == 2 * chickens + 4 * rabbits):
        return chickens, rabbits
    else:
        return "No solution"
heads = int(input("Enter No. of heads: "))
legs = int(input("Enter No. of legs: "))
result = puzzle(heads, legs)
if isinstance(result, tuple):
    print(f"{result[0]} chickens &{result[1]} rabbits")
else:
    print(result)
