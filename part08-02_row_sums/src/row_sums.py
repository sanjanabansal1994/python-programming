# Write your solution here
def add_sum(my_list:list):
    my_list.append(sum(my_list))

def row_sums(my_matrix: list):
    for list in my_matrix:
        add_sum(list)