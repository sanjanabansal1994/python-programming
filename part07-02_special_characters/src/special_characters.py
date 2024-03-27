# Write your solution here
import string

# print(dir(string))
# print(string.ascii_letters)

def separate_characters(my_string: str):
    part=['','','']
    for char in my_string:
        if char in string.ascii_letters:
            part[0]+=char
        elif char in string.punctuation:
            part[1]+=char
        else:
            part[2]+=char
    return part[0],part[1],part[2]