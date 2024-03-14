# If the index of the item is known, you can use the method 'pop'.
# If the contents of the item are known, you can use the method 'remove'.
# Write your solution here

l=[]
print(f'The list is now {l}')
inp= input("a(d)d, (r)emove or e(x)it:")
while inp != 'x':
    if inp=='d':
        if len(l)>0:
            l.append((l[-1]+1))
        else:
            l.append(1)
        print(f'The list is now {l}')
        inp= input("a(d)d, (r)emove or e(x)it:")
    elif inp=='r':
        l.pop(-1)
        print(f'The list is now {l}')
        inp= input("a(d)d, (r)emove or e(x)it:")

print("Bye!")
