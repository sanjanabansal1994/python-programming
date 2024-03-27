# Write your solution here
import json
def print_persons(filename:str):
    with open(filename) as my_file:
        data = my_file.read()
        persons = json.loads(data)
    for person in persons:
        string=''
        for key in person.keys():
            if key=="name":
                string+= f'{person["name"]} '
            if key=="age":
                string+=f'{person["age"]} years '
            if key=="hobbies":
                string+=f"("
                i=0
                for hobby in person["hobbies"]:
                    # print(len(person['hobbies']))
                    string+=f'{hobby}'
                    i+=1
                    if i < len(person['hobbies']):
                        string+=f', '
                    
                string= string+")"
        print(string)

print_persons(filename="file4.json")