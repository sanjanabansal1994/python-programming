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
        exercise[part[0]]= []
        exercise[part[0]].append(0)
        for i in range(1, len(part)):
            exercise[part[0]][0]+= int(part[i])

# print(exercise)
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

print(f'name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade')
for ids, name in students.items():
    exercise[ids].append(exercise[ids][0]//4)
    print(f'{name:28}  {exercise[ids][0]:<8}  {exercise[ids][1]:<8}  {exam_d[ids]:<8}  {exercise[ids][1]+exam_d[ids]:<8}  {grade(exercise[ids][1]+exam_d[ids]):<8}')
