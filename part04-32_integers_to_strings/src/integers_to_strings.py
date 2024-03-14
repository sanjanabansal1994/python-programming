# Write your solution here
def formatted(my_list: list):
    newl=[]
    for i in my_list:
        newl.append(f'{i:.2f}')
    return newl