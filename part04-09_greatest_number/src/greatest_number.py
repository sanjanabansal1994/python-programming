# Write your solution here
def greatest_number(x,y,z):
    if x>=y:
        if x>=z:
            return x
        else:
            return z
    else:
        if y>=z:
            return y
        else:
            return z
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)