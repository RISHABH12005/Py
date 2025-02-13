# Calculate compound interest.
p= 1000
r= 0.05
n= 4
t= 3
def CI(p,r,n,t):
    return p* ((1 + r/ n) ** (n * t)) - p
CI=CI(p,r,n,t)
print(CI)
