
def balanced_brackets(my_string: str):
    return balanced_brackets_rec(my_string, 0, (len(my_string)))

def balanced_brackets_rec(my_string: str, start:int, end:int):
    d = {'(':')','[':']'}
    if start > end:
        return False
    flag = True
    for i in range(start, end):
        if my_string[i]=='(' or my_string[i]=='[' or my_string[i]==']' or my_string[i]==')':
            flag=False
            break
    if flag==True:
        return True

    i= start
    j= end

    openingBracket = False
    for i in range(start, end):
        if my_string[i]=='(' or my_string[i]=='[':
            openingBracket = True
            break
    new_i = i

    closingBracket = False
    for j in range(end-1,start,-1):
        if my_string[j]==')' or my_string[j]==']':
            closingBracket = True
            break
    new_j = j
    if openingBracket==False or closingBracket==False:
        return False

    if not d[my_string[new_i]] == my_string[new_j]:
        return False
    
    return balanced_brackets_rec(my_string, (new_i)+1, new_j)


# Model Solution

def balanced_brackets(mj: str):
    # string is empty, so it is ok
    if len(mj) == 0:
        return True
 
    # if first character is not any bracket, let's eat it away
    if not mj[0] in "()[]":
        return balanced_brackets(mj[1:])
 
    # if last is not any bracket, let's eat it away
    if not mj[-1] in "()[]":
        return balanced_brackets(mj[:-1])
    
    # now is known that first and last characters are brackets
    # check if they are a pair
    if mj[0]=="(" and mj[-1]==")":
        return balanced_brackets(mj[1:-1])
    if mj[0]=="[" and mj[-1]=="]":
        return balanced_brackets(mj[1:-1])
 
    # were not, so this string is not ok
    return False