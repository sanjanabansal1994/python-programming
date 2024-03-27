# Write your solution here
from random import sample

def words(n: int, beginning: str):
    word_list=[]
    with open("words.txt") as file:
        for line in file:
            word_list.append(line.strip())
    res=[]
    for word in word_list:
        if word.startswith(beginning) and word not in res:
            res.append(word)
    if len(res)<n:
        raise ValueError
    else:
        res= sample(res,n)
    return res

# word_list = words(3, "candle")
# for word in word_list:
#     print(word)