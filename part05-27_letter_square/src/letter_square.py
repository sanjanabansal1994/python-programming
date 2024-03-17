# Write your solution here
n= int(input("Layers:"))

initial= ord("A")
# for i in range(-2,3):
#     for j in range(-2,3):
#         if i==-2 or j==-2 or i==2 or j==2:
#             print(f'{chr(initial+num-1)}', end="")
#         elif i==0 or j==0 :
#             print(f'{chr(initial)}', end="")
#         elif i==-1 or j==-1 or i==1 or j==1:
#             print(f'{chr(initial+num-2)}', end="")
#     print("\n")
        

for i in range(((-n)+1),n):
    string=''
    for j in range(((-n)+1),n):
        string+=f'{chr(initial+max(abs(i), abs(j)))}'
    print(string)