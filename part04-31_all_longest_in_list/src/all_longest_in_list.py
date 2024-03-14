# Write your solution here
def all_the_longest(l):
    length= len(l[0])
    nl=[l[0]]
    for i in range(1, len(l)):
        if length<len(l[i]):
            nl = [l[i]]
            length= len(l[i])
        elif length==len(l[i]):
            nl.append(l[i])

    return nl
