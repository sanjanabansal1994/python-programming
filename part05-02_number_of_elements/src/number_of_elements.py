# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    cnt=0
    for row in my_matrix:
        for i in row:
            if i==element:
                cnt+=1
    return cnt