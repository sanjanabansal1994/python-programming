# write your solution here
def read_fruits():
    with open("fruits.csv") as file:
        fruit_d={}
        for line in file:
            line= line.replace("\n","")
            parts= line.split(";")
            fruit_d[parts[0]]= float(parts[1])
        return fruit_d

