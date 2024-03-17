# Write your solution here
def search_func(name:str, pb:dict):
    if name in pb:
        for i in pb[name][:]:
            print(i)
    else:
        print("no number")

def add_func(name:str, number:str, pb:dict):
    if name in pb:
        pb[name].append(number)
    else:
        pb[name]=[number]
    print("ok!")

def main():
    pb={}
    while True:
        comm= int(input("command (1 search, 2 add, 3 quit):"))
        if comm==1:
            name= input("name:")
            search_func(name, pb)
        elif comm==2:
            name= input("name:")
            number= input("number:")
            add_func(name, number, pb)
        elif comm==3:
            print("quitting...")
            break
        else:
            break

main()