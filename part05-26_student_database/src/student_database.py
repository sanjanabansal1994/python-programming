# Write your solution here
def add_student(db:dict,name:str):
    db[name]=[]

def print_student(db:dict,name:str):
    if name in db:
        number= len(db[name])
        print(name+":")
        if number==0:
            print(f" no completed courses ")
        if number>0:
            course={}
            for i in db[name]:
                if i[0] in course and i[1]>0:
                    if course[i[0]]<i[1]:
                        course[i[0]]=i[1]
                elif i[1]>0:
                    course[i[0]]=i[1]
            number=len(course.keys())
            if number>0:
                print(f" {number} completed courses:")
                total=0
                for key, value in course.items():
                    total+=value
                    print(f'  { key} {value}')
                avg= total/number
                
                print(f' average grade {avg}')
            else:
                print(f" no completed courses ")
    else:
        print(f'{name}: no such person in the database')


def add_course(db:dict,name:str,tup:tuple):
    if name in db:
        db[name].append(tup)

def summary(db:dict):
    stats={}
    courses=0 
    max_avg=0
    for student in db:
        number= len(db[student])
        if number>0:
            course={}
            for tup in db[student]:
                if tup[0] in course:
                    if course[tup[0]]<tup[1]:
                        course[tup[0]]=tup[1]
                elif tup[0] not in course and tup[1]>0:
                    course[tup[0]]=tup[1]
                else:
                    number=0
            number=len(course.keys())
        if number>0:
            total= sum(course.values())
            avg= total/number
            stats[student]= [number,avg]
        if number==0:
            stats[student]= [0,0]
        if number > (courses):
            str1= f"most courses completed {number} {student}"
            courses = number
        if avg > (max_avg):
            str2= f"best average grade {avg} {student}"
            max_avg=avg
    print(f'students {len(db.keys())}')
    # print(stats.values())
    print(str1)
    print(str2)




# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Introduction to Programming", 0))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# print(students)
# summary(students)