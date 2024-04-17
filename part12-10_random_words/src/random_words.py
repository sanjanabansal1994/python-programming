# Write your solution here:
from random import choice

# help(choice)
def word_generator(characters: str, length: int, amount: int):
    word= ("".join([choice(characters) for i in range(0,length)]) for i in range(0, amount))
    return word

# wordgen = word_generator("abcdefg", 3, 5)
# for word in wordgen:
#     print(word)