# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

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

for ids, name in students.items():
    if ids in exercise:
        print(f'{students[ids]} {exercise[ids]}')
