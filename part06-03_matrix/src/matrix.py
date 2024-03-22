# write your solution here
def row_sums():
    with open("matrix.txt") as new:
        sum_list=[]
        for line in new:
            num=0
            parts= line.split(",")
            for i in parts:
                num+=(int(i))
            sum_list.append(num)

    return sum_list


def matrix_sum():
    sum_list= row_sums()
    total= sum(sum_list)
    return total

def matrix_max():
    maximum=0
    with open("matrix.txt") as new:
        for line in new:
            parts= line.split(",")
            for i in parts:
                if int(i)>maximum:
                    maximum = int(i)
    return maximum
    
# print(row_sums())
# print(sum(row_sums()))
# print(matrix_sum())
# print(matrix_max())
