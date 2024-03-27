# Write your solution here
def startswith(search_term:str, words:list):
    count= len(search_term)- search_term.count("*")
    matching_list=[]
    for word in words:
        flag= 0
        for i in range(0,count):
            if len(word)>=count and search_term[i]!="*" and word[i]==search_term[i]:
                flag+=1
        if flag==count:
            matching_list.append(word)
    return matching_list

def endswith(search_term:str, words:list):
    count= len(search_term)- search_term.count("*")
    matching_list=[]
    for word in words:
        flag= 0
        for i in range(-count,0,1):
            if len(word)>=count and search_term[i]!="*" and word[i]==search_term[i]:
                flag+=1
        if flag==count:
            matching_list.append(word)
    return matching_list

def find_words(search_term: str):
    word_list=[]
    with open("words.txt") as file:
        for line in file:
            word_list.append(line.strip())
    if search_term[-1]=="*":
        res= startswith(search_term, word_list)
    elif search_term[0]=="*":
        res= endswith(search_term, word_list)
    else:
        res=[]
        count= len(search_term)
        for word in word_list:
            flag=0
            for i in range(0, count):
                if len(word)==count and (word[i]==search_term[i] or search_term[i]=="."):
                    flag+=1
            if flag==count:
                res.append(word)
    return res
