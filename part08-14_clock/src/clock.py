# Write your solution here:
from datetime import datetime, timedelta
class Clock():

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hour= hours
        self.minute= minutes
        self.second= seconds
        self.time= datetime.strptime(f'{self.hour}:{self.minute}:{self.second}','%H:%M:%S')

    def tick(self):
        self.time= self.time+timedelta(seconds=1)

    def set(self,hours=0,minutes=0, seconds=0):
        self.time= datetime.strptime(f'{hours}:{minutes}:{seconds}','%H:%M:%S')
    
    def __str__(self):
        time= datetime.strftime(self.time,'%H:%M:%S')
        return time

# clock = Clock(23, 59, 55)
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)

# clock.set(12, 5)
# print(clock)