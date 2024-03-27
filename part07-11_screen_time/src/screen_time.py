# Write your solution here
from datetime import datetime, timedelta

filename= input("Filename: ")
start= input("Starting date: ")
start_date= datetime.strptime(start,"%d.%m.%Y")
day= int(input("How many days: "))
# filename= "late_june.txt"
# start= "24.6.2020"
# start_date= datetime.strptime(start,"%d.%m.%Y")
# day= 5
print("Please type in screen time in minutes on each day (TV computer mobile):")
minutes=[]
dates=[]
while day>0:
    d=start_date.strftime("%d.%m.%Y")
    dates.append(d)
    time= input(f"Screen time {d}: ")
    part= time.split(" ")
    for i in part:
        minutes.append(int(i))
    start_date= start_date + timedelta(days=1)
    day-=1
with open(filename,'w') as file:
    file.write(f"Time period: {dates[0]}-{dates[-1]}\n")
    file.write(f'Total minutes: {sum(minutes)}\n')
    file.write(f'Average minutes: {sum(minutes)/len(dates)}\n')
    for i in range(0,len(dates)):
        string=f'{dates[i]}: '
        for j in range(3*i,(3*i)+3):
            string+=f'{minutes[j]}/'
        file.write(f'{string[:-1]}\n')
