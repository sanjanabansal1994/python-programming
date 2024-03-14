# Write your solution here
pnts=[]
exercises=[]
user= input("Exam points and exercises completed: ")
while True:
    pnts.append(int((user.split(" "))[0]))
    exercise_pnts= int((user.split(" "))[-1])//10
    exercises.append(exercise_pnts)
    user= input("Exam points and exercises completed: ")
    if user=='':
        break

total= []
for i in range(0,len(pnts)):
    total.append(pnts[i]+exercises[i])

grade= total.copy()

for i in range(0,len(pnts)):
    if pnts[i] < 10:
        grade[i] = 0
    elif pnts[i]>=10 and total[i]<=14:
        grade[i]=0
    elif pnts[i]>=10 and total[i]<=17:
        grade[i]=1
    elif pnts[i]>=10 and total[i]<=20:
        grade[i]=2
    elif pnts[i]>=10 and total[i]<=23:
        grade[i]=3
    elif pnts[i]>=10 and total[i]<=27:
        grade[i]=4
    else:
        grade[i] = 5

# print(total)
# print(grade)

average= sum(total)/len(total)
Pass_percentage= (len(grade)-grade.count(0))*100/len(grade)

print("Statistics:")
print(f'Points average: {average:.1f}' )
print(f"Pass percentage: {Pass_percentage:.1f}")
print("Grade distribution:")
print(" 5:","*"*grade.count(5))
print(" 4:","*"*grade.count(4))
print(" 3:","*"*grade.count(3))
print(" 2:","*"*grade.count(2))
print(" 1:","*"*grade.count(1))
print(" 0:","*"*grade.count(0))



def exam_and_exercise_completed(inpt):
    space = inpt.find(" ")
    exam = int(inpt[:space])
    exercise = int(inpt[space+1:])
    return [exam, exercise]
 
def exercise_points(amount):
    return amount // 10
 
def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i
 
def mean(points):
    return sum(points) / len(points)
 
def main():
    points = []
    grades = [0] * 6
    while True:
        inpt = input("Exam points and exercises completed: ")
        if len(inpt) == 0:
            break
 
        exam_and_exercises = exam_and_exercise_completed(inpt)
        exercise_pnts = exercise_points(exam_and_exercises[1])
        total_points = exam_and_exercises[0] + exercise_pnts
 
        points.append(total_points)
        grd = grade(total_points)
        if exam_and_exercises[0] < 10:
            grd = 0
        grades[grd] += 1
 
    pass_pros = 100 * (len(points) - grades[0]) / len(points)
 
    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_pros:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")
 
main()