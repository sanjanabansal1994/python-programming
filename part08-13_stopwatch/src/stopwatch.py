# Write your solution here:
from datetime import datetime, timedelta
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.time= datetime.strptime(f'{self.minutes}:{self.seconds}','%M:%S')

    def tick(self):
        self.time= self.time + timedelta(seconds=1)
        # self.seconds+=1
        # if self.seconds%60==0:
        #     self.minutes+=1
        #     self.seconds=0
    
    def __str__(self):
        return f"{datetime.strftime(self.time,'%M:%S')}"
        

# watch = Stopwatch()
# for i in range(360):
#     print(watch)
#     watch.tick()