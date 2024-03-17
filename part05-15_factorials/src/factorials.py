# Write your solution here
def factorials(n: int):
    fact={}
    for i in range(1,(n+1)):
        fact[i]=1
        for j in range(1,(i+1)):
            fact[i]=j*fact[i]
    
    return fact

