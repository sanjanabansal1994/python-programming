# Write your solution here
from datetime import timedelta, datetime

def cheaters():
    with open("start_times.csv") as file:
        student_start=[]
        for line in file:
            student={}
            part= line.split(";")
            # print(datetime.strptime(str(part[1].strip()),'%H:%M'))
            student[part[0]]= datetime.strptime(part[1].strip(),'%H:%M')
            student_start.append(student)
    with open("submissions.csv") as file:
        student_submission=[]
        for line in file:
            student={}
            part= line.split(";")
            student[part[0]]= part[1].strip(), part[2].strip(), datetime.strptime(part[3].strip(),'%H:%M')
            # print(student)
            student_submission.append(student)
    name=[]
    for test in student_start:
        for key, value in test.items():
            for submission in student_submission:
                if key in submission and submission[key][2] > value +timedelta(hours=3):
                    name.append(key)
    return (list(set(name)))


# cheaters()