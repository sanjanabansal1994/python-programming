# Write your solution here

def spruce(size):
    c= size
    h=1
    print("a spruce!")
    while h<=size:
        print(" "*(size-h)+"*"*((2*h)-1))
        h+=1
    print(" "*(size-1)+"*")
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)