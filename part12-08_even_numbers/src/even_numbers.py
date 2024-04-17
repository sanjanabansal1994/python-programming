# Write your solution here
def even_numbers(beginning: int, maximum: int):
    n= beginning
    while n<=maximum:
        if n%2 == 0:
            yield n
        n+=1