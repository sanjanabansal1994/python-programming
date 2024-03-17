# Write your solution here
def times_ten(start_index: int, end_index: int):
    d={}
    for i in range(start_index, end_index+1):
        d[i]= 10*i
    return d
