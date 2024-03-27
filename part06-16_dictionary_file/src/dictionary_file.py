# Write your solution here
def add(fin_word:str, eng_word:str, text_d:dict):
    text_d[fin_word]=eng_word
    with open("dictionary.txt",'a') as file:
        string= f'{fin_word};{eng_word}'
        file.write(string+"\n")


def search(search_term:str,text_d:dict):
    for key, value in text_d.items():
        if search_term in key or search_term in value:
            print(f'{key} - {value}')

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    cmd= int(input("Function: "))
    text_d={}
    with open("dictionary.txt") as new_file:
        for line in new_file:
            part= line.split(";")
            text_d[part[0].strip()]= part[1].strip()
    if cmd==1:
        fin_word= input("The word in Finnish: ")
        eng_word= input("The word in English: ")
        add(fin_word, eng_word,text_d)
        print("Dictionary entry added")
    if cmd==2:
        search_term= input("Search term: ")
        search(search_term, text_d)
    if cmd==3:
        print("Bye!")
        break
