# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(str1:str):
    str2=""
    for i in range(1,len(str1)+1):
        str2+=str1[-i]
    return str1==str2


while True:
    word= input("Please type in a palindrome: ")
    if (palindromes(word)):
        print(word,"is a palindrome!")
        break
    print("that wasn't a palindrome")
    