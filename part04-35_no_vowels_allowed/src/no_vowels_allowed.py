# Write your solution here
def no_vowels(my_string):
    new=''
    for char in my_string:
        if char not in ['a','e','i','o','u']:
            new+=char
    return new
