# Write your solution here
def sum_of_positives(l:list):
    sum=0
    for i in l:
        if i>0:
            sum+=i
    return sum