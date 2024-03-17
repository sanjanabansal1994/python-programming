# Write your solution here
def older_people(people: list, year: int):
    res=[]
    for tup in people:
        if tup[1]< year:
            res.append(tup[0])
    return res

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# older = older_people(people, 1979)
# print(older)