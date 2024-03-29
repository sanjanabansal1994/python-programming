# Write your solution here
from datetime import datetime, timedelta
import csv

def final_points():
    start_times={}
    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            start_times[line[0]]= datetime.strptime(line[1], '%H:%M')

    submission={}
    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            task={}
            time= datetime.strptime(line[3], '%H:%M')
            points= int(line[2])
            task[line[1]]= points
            name= line[0]
            if name not in submission and time-start_times[name]<timedelta(hours=3):
                submission[name]= task
            elif line[1] not in submission[name] and time-start_times[name]<timedelta(hours=3):
                submission[name][line[1]]= points
            elif line[1] in submission[name] and submission[name][line[1]]< points and time-start_times[name]<timedelta(hours=3):
                # print(submission[name])
                submission[name][line[1]]= points
    # print(submission)
    grade={}
    for name in start_times:
        grade[name]= sum(list(submission[name].values()))
    
    return (grade)


# print(final_points())