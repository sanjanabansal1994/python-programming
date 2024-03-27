# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int):
    pool= list(range(lower,upper+1))
    weekly_draw= random.sample(pool,amount)
    weekly_draw.sort()
    return weekly_draw