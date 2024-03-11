# Copy here code of line function from previous exercise
def line(times,string):
    if len(string)>0:
        print(string[0]*times)
    else:
        print("*"*times)
        
def box_of_hashes(height):
    # You should call function line here with proper parameters
    h=0
    while h<height:
        line(10, "#")
        h+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
