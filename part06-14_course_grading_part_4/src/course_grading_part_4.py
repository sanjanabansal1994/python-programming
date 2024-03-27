# tee ratkaisu tänne
# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    Course_information= input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    Course_information= "course1.txt"

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

course_d={}
with open(Course_information) as course:
    for line in course:
        part= line.split(":")
        course_d[part[0]]= part[1]

def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i


with open("results.txt",'w') as result:
    str1= (f'{course_d["name"].strip()},{course_d["study credits"]} credits')
    result.write(str1+"\n")
    str2=f'{"="*38}'
    result.write(str2+"\n")
    str3= (f'name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade')
    result.write(str3+"\n")
    for ids, name in students.items():
        exercise[ids].append(exercise[ids][0]//4)
        str4= (f'{name:28}  {exercise[ids][0]:<8}  {exercise[ids][1]:<8}  {exam_d[ids]:<8}  {exercise[ids][1]+exam_d[ids]:<8}  {grade(exercise[ids][1]+exam_d[ids]):<8}')
        result.write(str4+"\n")


with open("results.csv", 'w') as csv_result:
    for ids, name in students.items():
        exercise[ids].append(exercise[ids][0]//4)
        str4= (f'{ids};{name};{grade(exercise[ids][1]+exam_d[ids]):<8}')
        csv_result.write(str4+"\n")
print("Results written to files results.txt and results.csv")