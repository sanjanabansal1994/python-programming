# Write your solution here
from difflib import get_close_matches
# print(help(get_close_matches))
word_list=[]
with open("wordlist.txt") as file:
    for line in file:
        word_list.append(line.strip())

string= input("write text:")
parts= string.split(" ")
res=[]
incorr=[]
for part in parts:
    if part.strip().lower() in word_list:
        res.append(part.strip())
    else:
        incorr.append(part.strip())
        res.append(f'*{part.strip()}*')
result= " ".join(res)
print(result)
print("suggestions:")
for word in incorr:
    print(f'{word}: {", ".join(get_close_matches(word,word_list))}')

