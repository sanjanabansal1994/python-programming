# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.list= [0]

    def add_number(self, number:int):
        self.numbers+=1
        self.list.append(number)

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return sum(self.list)
    
    def average(self):
        if self.numbers>0:
            avg= sum(self.list)/self.numbers
        else:
            avg=0
        return avg
    

stats= NumberStats()
stats_even= NumberStats()
stats_odd=NumberStats()
n=int(input("Please type in integer numbers:"))
while n>=0:
    stats.add_number(n)
    if n%2==0:
        stats_even.add_number(n)
    else:
        stats_odd.add_number(n)
    n= int(input())
print(f'Sum of numbers: {stats.get_sum()}')
print("Mean of numbers:", stats.average())
print(f'Sum of even numbers: {stats_even.get_sum()}')
print(f'Sum of odd numbers: {stats_odd.get_sum()}')
    

    