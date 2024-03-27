# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    l=[]
    for i in range(0,amount):
        l.append(Fraction(1,amount))
    return l

# for p in fractionate(3):
#     print(p)

# print()

# print(fractionate(5))
