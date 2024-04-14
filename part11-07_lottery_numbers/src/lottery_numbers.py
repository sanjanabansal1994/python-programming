# WRITE YOUR SOLUTION HERE:

class LotteryNumbers:
    def __init__(self, week, numbers):
        self.week= week
        self.numbers= numbers

    def number_of_hits(self, numbers: list):
        return sum([1 if num in self.numbers else 0 for num in numbers])

    def hits_in_place(self,numbers):
        return [num if num in self.numbers else -1 for num in numbers]