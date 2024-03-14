# Write your solution here
def longest(l:list):
    length=0
    longest= ''
    for item in l:
        if length<len(item):
            length= len(item)
            longest= item
    return longest