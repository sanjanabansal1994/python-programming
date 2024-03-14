# Write your solution here
def length_of_longest(l:list):
    length=0
    for item in l:
        if length<len(item):
            length= len(item)
    return length