# Write your solution here
def everything_reversed(l:list):
    nl=[]
    for i in range(1, (len(l)+1)):
        word= l[-i]
        nword=''
        for j in range(1,(len(word)+1)):
            nword+=word[-j]
        nl.append(nword)
    return nl

#second solution

def everything_reversed(my_list: list):
    new_list = []
    for my_string in my_list:
        new_list.append(my_string[::-1])
    return new_list[::-1]