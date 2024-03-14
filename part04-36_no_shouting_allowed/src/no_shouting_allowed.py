# Write your solution here
def no_shouting(my_list):
    new=[]
    for i in my_list:
        if not i.isupper():
            new.append(i)

    return new
