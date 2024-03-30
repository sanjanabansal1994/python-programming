# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    avg1=0
    for key in person1:
        if key!='name':
            avg1+=person1[key]
    avg2=0
    for key in person2:
        if key!='name':
            avg2+=person2[key]
    avg3=0
    for key in person3:
        if key!='name':
            avg3+=person3[key]
    if avg1<avg2 and avg1< avg3:
        res= person1
    elif avg2<avg3 and avg2<avg3:
        res= person2
    else:
        res= person3
    return res
    