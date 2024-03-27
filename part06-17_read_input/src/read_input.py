# Write your solution here
def read_input(input_str:str, lower_limit:int, upper_limit:int):
    while True:
        try:
            num = input(f"{input_str}")
            number = int(num)
            if lower_limit < number < upper_limit:
                return number
        except ValueError:
            pass # this command doesn't actually do anything

        print(f"You must type in an integer between {lower_limit} and {upper_limit}")

# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)