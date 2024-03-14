# Write your solution here
def longest_series_of_neighbours(my_list):
    l1=[]
    cnt=1
    for i in range(1,len(my_list)):
        if abs(my_list[i]-my_list[i-1])==1:
            cnt+=1
        else:
            l1.append(cnt)
            cnt=1
    l1.append(cnt)
    return max(l1)

# my_list = [5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]
# print(longest_series_of_neighbours(my_list))