# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        large=0
        for line in new_file:
            num= int(line)
            if num>large:
                large=num

        return large