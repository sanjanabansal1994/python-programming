# Write your solution here
import urllib.request
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data= my_request.read()
    data1= json.loads(data)
    enable_courses=[]
    for course in data1:
        if course['enabled']==True:
            fname= course['fullName']
            name= course['name']
            year= course['year']
            total_exer= sum(course['exercises'])
            my_tup= fname,name,year,total_exer
            enable_courses.append(my_tup)
    return enable_courses

# print(retrieve_all())
def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data= my_request.read()
    data1= json.loads(data)
    course={}
    course['weeks']= len(data1)
    list_students=[]
    list_hours=[]
    list_exer=[]
    for d in data1:
        list_students.append(data1[d]['students'])
        list_hours.append(data1[d]['hour_total'])
        list_exer.append(data1[d]['exercise_total'])
    course['students']= max(list_students)
    course['hours']= sum(list_hours)
    course['hours_average']= int(sum(list_hours)/max(list_students))
    course['exercises']= sum(list_exer)
    course['exercises_average']= int(sum(list_exer)/max(list_students))
    return (course)
