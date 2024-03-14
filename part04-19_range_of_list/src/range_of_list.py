# Write your solution here
def range_of_list(l:list):
    return max(l)-min(l)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print("The range of the list is",result)