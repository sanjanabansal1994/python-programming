# Copy here code of line function from previous exercise and use it in your solution
def line(times,string):
    if len(string)>0:
        print(string[0]*times)
    else:
        print("*"*times)
        
def shape(h1,char1,h2,char2):
    h=1
    while h<=h1:
        line(h,char1)
        h+=1
    h=1
    while h<=h2:
        line(h1,char2)
        h+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")