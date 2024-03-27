# Write your solution here
from datetime import datetime
# print(dir(datetime))
# print(dir(datetime.datetime_CAPI))
def is_it_valid(pic:str):
    chck_str= '0123456789ABCDEFHJKLMNPRSTUVWXY'
    try:
        day= int(pic[0:2])
        month= int(pic[2:4])
        if pic[6]=='+':
            year= int(pic[4:6])+1800
        elif pic[6]=='-':
            year= int(pic[4:6])+1900
        elif pic[6]=='A':
            year= int(pic[4:6])+2000
        dat= datetime(year,month,day)
    except:
        return False
    chck_num= int(pic[0:6]+pic[7:10])
    ind= chck_num%31
    last= chck_str[ind]
    if len(pic)==11 and pic[6] in ['+','-','A']and last== pic[-1]:
        return True
    else:
        return False

