# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv",'a') as file:
        string= f'{person[0]};{person[1]};{person[2]}'
        file.write(string+"\n")

if __name__ == "__main__":
    person= ("Paul Paulson", 37, 175.5)
    store_personal_data(person)