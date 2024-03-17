# Write your solution here
def dict_of_numbers():
    d={}
    ones_d={0:"zero",1:"one", 2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    # key_d={2:"twent",3:"thirt",4:"fort",5:"fift",6:"sixt",7:"sevent",8:"eight",9:"nint"}
    tens_d={1:"ten",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
    teen_d={1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifteen",6:"sixteen",7:"seventeen", 8:"eighteen",9:"nineteen"}
    for i in range(0,100):
        tens=i//10
        ones=i%10
        if tens==0:
            d[i] = ones_d[ones]
        elif tens==1 and ones!=0:
            d[i]= teen_d[ones]
        elif tens not in [0,1] and ones!=0:
            d[i]=tens_d[tens]+"-"+ones_d[ones]
        elif tens!=0 and ones== 0:
            if tens==1:
                d[i]="ten"
            else:
                d[i]= tens_d[tens]      
    return d

# numbers = dict_of_numbers()
# print(numbers[2])
# print(numbers[11])
# print(numbers[45])
# print(numbers[99])
# print(numbers[0])