# Write your solution here
import re

def is_dotw(my_string: str):
    expression= "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.search(expression, my_string):
        return True
    else:
        return False

def all_vowels(my_string: str):
    expression = "[aeiou]"
    if sum([1 for char in my_string if not re.search(expression, char)])==0:
        return True
    else:
        return False

# Model Solution
# def all_vowels(my_string: str):
#     return re.search("^[aeiou]*$", my_string) is not None

def time_of_day(my_string: str):
    expression= "[0-1][0-9]:[0-5][0-9]:[0-5][0-9]|2[0-4]:[0-5][0-9]:[0-5][0-9]"
    if re.search(expression, my_string):
        return True
    else:
        return False

