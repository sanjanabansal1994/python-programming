# Write your solution here
from random import choice

def roll(die:str):
    A=[3,3,3,3,3,6]
    B=[2,2,2,5,5,5]
    C=[1,4,4,4,4,4]
    if die=='A':
        res= choice(A)
    if die=='B':
        res= choice(B)
    if die=='C':
        res= choice(C)
    return res

def play(die1: str, die2: str, times: int):
    die1_win=0
    die2_win=0
    tie=0
    for i in range(0,times):
        i1 = roll(die1)
        i2 = roll(die2)
        if i1>i2:
            die1_win+=1
        elif i1<i2:
            die2_win+=1
        else:
            tie+=1
    return die1_win,die2_win,tie

# print(play("A", "B", 100))