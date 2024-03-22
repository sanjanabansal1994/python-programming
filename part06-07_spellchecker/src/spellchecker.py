# write your solution here
def spell_check(string:str):
    with open("wordlist.txt") as file:
        file_copy=[]
        for line in file:
            file_copy.append(line.strip())
    # print(file_copy)
        res=""
    for word in string.split(" "):
        if word.lower() in file_copy:
            res= res+ " "+word
        else:
            res = res+" *"+word+"*"
    print(res)

text= input("Write text:")

spell_check(text)


# spell_check("This is acually a good and usefull program")