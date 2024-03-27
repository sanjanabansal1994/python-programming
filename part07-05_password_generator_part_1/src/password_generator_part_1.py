# Write your solution here
from random import sample
from string import ascii_lowercase

def generate_password(length:int):
    password=''
    p= sample(ascii_lowercase,length)
    for char in p:
        password+=char

    return password

# print(generate_password(2))