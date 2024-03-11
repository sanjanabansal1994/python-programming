# Write your solution here
ind= int(input("Index:"))
list1= [1, 2, 3, 4, 5]
while ind!=-1:
    value= int(input("New value:"))
    list1[ind]= value
    print(list1)
    ind= int(input("Index:"))
    