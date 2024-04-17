from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts:list):
    return reduce(lambda reduced_sum, x: x.credits+reduced_sum, attempts,0)

def sum_of_passed_credits(attempts:list):
    return reduce(lambda reduced_sum, x: x.credits+reduced_sum, filter(lambda x: x.grade>0,attempts),0)

def average(attempts:list):
    passed= list(filter(lambda x: x.grade>0,attempts))
    total= reduce(lambda reduced_avg, x: x.grade+reduced_avg, passed, 0)
    return total/len(passed)

# Model Solution

from functools import reduce
 
class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits
 
    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"
 
def credit_summer(cr_sum, attempt):
    return cr_sum + attempt.credits
 
def sum_of_all_credits(attempts: list):
    return reduce(credit_summer, attempts, 0)
 
def sum_of_passed_credits(attempts: list):
    accepted = filter(lambda s: s.grade > 0, attempts)
    return reduce(credit_summer, accepted, 0)
 
def average(attempts: list):
    def grade_summer(cr_sum, attempt):
        return cr_sum + attempt.grade 
 
    accepted = list(filter(lambda s: s.grade > 0, attempts))
    sum_of_grades = reduce(grade_summer, accepted, 0)
 
    return sum_of_grades / len(accepted)