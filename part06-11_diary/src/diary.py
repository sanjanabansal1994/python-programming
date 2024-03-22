# Write your solution here
while True:
    cmd= input("1 - add an entry, 2 - read entries, 0 - quit\nFunction: ")
    if cmd=='0':
        print("Bye now!")
        break
    elif cmd=='1':
        entry= input("Diary entry: ")
        with open("diary.txt",'a') as file:
            file.write(entry+"\n")
        print("Diary saved\n")
    elif cmd=='2':
        print("Entries:")
        with open("diary.txt") as file:
            diary= (file.read())
            print(diary)