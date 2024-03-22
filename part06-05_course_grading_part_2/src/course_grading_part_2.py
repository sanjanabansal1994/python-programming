# wwite your solution here
# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("exam_points1.csv")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

students={}
with open(student_info) as stud:
    for line in stud:
        part= line.split(";")
        if part[0]=="id":
            continue
        students[part[0]]= part[1].strip()+" "+part[2].strip()

exercise={}
with open(exercise_data) as exer:
    for line in exer:
        part= line.split(";")
        if part[0]=="id":
            continue
        exercise[part[0]]= 0
        for i in range(1, len(part)):
            exercise[part[0]]+= int(part[i])
exam_d={}
with open(exam_data) as exam:
    for line in exam:
        part = line.split(";")
        if part[0]=="id":
            continue
        exam_d[part[0]]= 0
        for i in range(1, len(part)):
            exam_d[part[0]]+= int(part[i])

def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i

for ids, name in students.items():
    exercise[ids]= exercise[ids]//4
    print(f'{name} {grade(exercise[ids]+exam_d[ids])}')

