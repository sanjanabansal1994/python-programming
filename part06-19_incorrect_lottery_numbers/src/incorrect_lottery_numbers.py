# Write your solution here
def filter_incorrect():
    with open("lottery_numbers.csv") as lottery_file:
        lottery={}
        for line in lottery_file:
            part= line.split(";")
            part[0]= part[0].strip()
            part[0]= tuple(part[0].split(" "))
            lottery[part[0]]=part[1].strip().split(",")
    correct={}   
    for key , value in lottery.items():
        try:
            flag=0
            if key[0].strip()== "week" and 0<=int(key[1].strip())<=52:
                flag=1
                chk=[]
            for i in value:
                chk.append(int(i.strip()))
                if 1<=int(i.strip())<=39 and len(value)==7 and chk.count(int(i.strip()))<2:
                    flag+=1
            if flag==8:
                correct[key]= value
        except:
            continue
    with open("correct_numbers.csv",'w') as corr:
        string=''
        for key, value in correct.items():
            string+= f'{key[0]} {key[1]};{value[0]},{value[1]},{value[2]},{value[3]},{value[4]},{value[5]},{value[6]}'+"\n"
        corr.write(string)
        



# filter_incorrect()