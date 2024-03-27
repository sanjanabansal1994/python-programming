# Write your solution here
from string import ascii_lowercase
from random import sample, randint, randrange

def generate_strong_password(length:int,number_fg:bool,schar_fg:bool):
    password=''

    if number_fg and not schar_fg:
        p= sample(ascii_lowercase,1)
        p+= sample('0123456789',1)
        if length>2:
            p+=sample((ascii_lowercase +'1234567890'),length-2)
    elif not number_fg and schar_fg:
        p= sample(ascii_lowercase,1)
        p+= sample('!?=+-()#',1)
        if length>2:
            p+=sample((ascii_lowercase +'!?=+-()#'),length-2)
    elif number_fg and schar_fg:
        p= sample(ascii_lowercase,1)
        p+= sample('!?=+-()#',1)
        p+= sample('0123456789',1)
        if length>3:
            p+=sample((ascii_lowercase +'1234567890'+'!?=+-()#'),length-3)
    else:
        p= sample(ascii_lowercase,length)

    # print(len(p))
    
    for char in p:
        password+=char
    
    return password

# print(generate_strong_password(8,True,True))
# print(generate_strong_password(1,1,0))

# for i in range(10):
#     print(generate_strong_password(8, True, True))
