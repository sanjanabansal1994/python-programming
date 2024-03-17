# Write your solution here
pb={}
while True:
    comm= int(input("command (1 search, 2 add, 3 quit):"))
    if comm==1:
        name=input("name:")
        if name in pb:
            print(pb[name])
        else:
            print("no number")
    elif comm==2:
        name=input("name: ")
        number= input('number: ')
        pb[name]= number
        print("ok!")
    elif comm==3:
        print("quitting...")
        break
    else:
        break


    def search(persons):
    name = input("name: ")
    if name in persons:
        print(persons[name])
    else:
        print("no number")
 

# Model Solution
def add(persons):
    name = input("name: ")
    number = input("number: ")
    persons[name] = number
    print("ok!")
 
def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")
 
main()