# Write your solution here
def prime_numbers():
    n=2
    while True:
        flag=0
        for i in range(2,n):
            if n%i == 0:
                flag = 1
        if flag == 0:
            yield n
        n+=1
            

# numbers = prime_numbers()
# for i in range(18):
#     print(next(numbers))