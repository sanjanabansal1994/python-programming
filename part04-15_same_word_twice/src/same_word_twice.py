# Write your solution here
l=[]
word= input("Word:")
while True:
    if word in l:
        print("You typed in",len(set(l)),"different words")
        break
    else:
        l.append(word)
        word= input("Word:")