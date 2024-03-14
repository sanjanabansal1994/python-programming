# Write your solution here
def shortest(l):
    length= len(l[0])
    word= l[0]
    for i in range(1, len(l)):
        if length>len(l[i]):
            word= l[i]
            length= len(l[i])

    return word

