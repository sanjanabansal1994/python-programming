# Write your solution here
def oldest_person(people: list):
    year=9999
    res=""
    for tup in people:
        if tup[1]<year:
            year= tup[1]
            res= tup[0]
    return res

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# print(oldest_person(people))