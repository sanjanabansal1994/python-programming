# Write your solution here
def solution_read():
    with open("solutions.csv") as file:
        sol=[]
        for line in file:
            student={}
            part= line.split(";")
            student[part[0]]=part[1].split()+part[2].split()
            sol.append(student)
    return sol

# print(solution_read())

def check_solution(solution:list):
    sol= solution
    corr=[]
    incorr=[]
    for pair in sol:
        if "+" in list(pair.values())[0][0]:
            equation= list(pair.values())[0][0]
            value_part= equation.split("+")
            # print(value_part)
            # print(list(pair.keys())[0])
            if int(value_part[0])+int(value_part[1])==int(list(pair.values())[0][1]):
                corr.append(pair)
            else:
                incorr.append(pair)
        if "-" in list(pair.values())[0][0]:
            equation= list(pair.values())[0][0]
            value_part= equation.split("-")
            # print(value_part)
            if int(value_part[0])-int(value_part[1])==int(list(pair.values())[0][1]):
                corr.append(pair)
            else:
                incorr.append(pair)
    return corr, incorr


# check_solution(solution_read())

def write_files(correct:list,incorrect:list):
    corr= correct
    incorr= incorrect
    with open("correct.csv", 'w') as corr_file:
        for pair in corr:
            string= f'{list(pair.keys())[0]};{list(pair.values())[0][0]};{list(pair.values())[0][1]}'
            corr_file.write(string+"\n")
    with open("incorrect.csv", 'w') as incorr_file:
        for pair in incorr:
            string= f'{list(pair.keys())[0]};{list(pair.values())[0][0]};{list(pair.values())[0][1]}'
            incorr_file.write(string+"\n")
    
def filter_solutions():
    sol= solution_read()
    correct, incorrect= check_solution(sol)
    write_files(correct,incorrect)


# filter_solutions()