#Remember the difference between the two: sort changes the order of the original list in place, whereas sorted creates a new, ordered copy of the list. With sorted we can preserve the original order of the list:
# Write your solution here
l=[]
n= int(input("New item:"))
while True:
    if n==0:
        print("Bye!")
        break
    l.append(n)
    print("The list now:",l)
    print("The list in order:",sorted(l))
    n= int(input("New item:"))
