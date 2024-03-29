# Write your solution here
def change_case(orig_string: str):
    res=''
    for char in orig_string:
        if char.islower():
            res+=char.upper()
        else:
            res+=char.lower()
    return res
def split_in_half(orig_string: str):
    length= len(orig_string)
    res= orig_string[0:length//2],orig_string[length//2:]
    return res

def remove_special_characters(orig_string: str):
    res=''
    for char in orig_string:
        if char.lower() in '1234567890qwertyuiopasdfghjklzxcvbnm ':
            res+=char
    return res
