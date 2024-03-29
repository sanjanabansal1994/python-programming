# Write your solution here
def run(program):
    i=0
    loc={}
    for j in range(0,len(program)):
        part= program[j].split(" ")
        if ":" in part[0]:
            loc[part[0][:-1]] = j

    variable={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'Y':0,'Z':0}
    res=[]

    while i < len(program):
        part= program[i].split(" ")
        if part[0]=='PRINT':
            if part[1] in variable:
                res.append(variable[part[1].strip()])
            else:
                res.append(int(part[1]))
        elif part[0]=='MOV':
            if part[2] in variable:
                variable[part[1].strip()]= variable[part[2].strip()]                
            else:
                variable[part[1].strip()]= int(part[2])
        elif part[0]=='ADD':
            if part[2] in variable:
                variable[part[1].strip()]= variable[part[1].strip()]+ variable[part[2].strip()]
            else:
                variable[part[1].strip()]= variable[part[1].strip()]+ int(part[2].strip())
        elif part[0]=='SUB':
            if part[2] in variable:
                variable[part[1].strip()]= variable[part[1].strip()]- variable[part[2].strip()]
            else:
                variable[part[1].strip()]= variable[part[1].strip()]- int(part[2].strip())
        elif part[0]=='MUL':
            if part[2] in variable:
                variable[part[1].strip()]= variable[part[1].strip()]* variable[part[2].strip()]
            else:
                variable[part[1].strip()]= variable[part[1].strip()]* int(part[2].strip())
        elif part[0]=='END':
            break
        elif part[0]=="JUMP":
            i = loc[part[1]]-1
        elif part[0]=="IF":
            op= part[2]
            if part[1] in variable:
                v1= variable[part[1]]
            else:
                v1=int(part[1])
            if part[3] in variable:
                v2= variable[part[3]]
            else:
                v2=int(part[3])
            if eval('{}{}{}'.format(v1,op,v2)):
                i = loc[part[-1]]-1
        i+=1
    return res

# program3 = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1', 'IF A <= N JUMP start'] 
# result = run(program3)
# print(result)


# Model Solution
def value(x, data):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x in characters:
        return data[characters.index(x)]
    else:
        return int(x)
 
def condition(a, condition, b):
    if condition == "==":
        return a == b
    if condition == "!=":
        return a != b
    if condition == "<":
        return a < b
    if condition == "<=":
        return a <= b
    if condition == ">":
        return a > b
    if condition == ">=":
        return a >= b
 
def run(program):
    length = len(program)
    row = 0
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    data = [0]*26
    result = []
    while True:
        if row == length:
            break
        parts = program[row].split(" ")
        if parts[0] == "PRINT":
            result.append(value(parts[1], data))
        if parts[0] == "MOV":
            data[characters.index(parts[1])] = value(parts[2], data)
        if parts[0] == "ADD":
            data[characters.index(parts[1])] += value(parts[2], data)
        if parts[0] == "SUB":
            data[characters.index(parts[1])] -= value(parts[2], data)
        if parts[0] == "MUL":
            data[characters.index(parts[1])] *= value(parts[2], data)
        if parts[0] == "JUMP":
            row = program.index(parts[1]+":")
            continue
        if parts[0] == "IF":
            if condition(value(parts[1], data), parts[2], value(parts[3], data)):
                row = program.index(parts[5]+":")
                continue
        if parts[0] == "END":
            break
        row += 1
    return result