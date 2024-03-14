# Write your solution here
def most_common_character(string):
    cnt1= string.count(string[0])
    result=string[0]
    for char in string:
        cnt= string.count(char)
        if cnt>cnt1:
            cnt1= cnt
            result= char
    return result

# first_string = "abcdbde"
# print(most_common_character(first_string))