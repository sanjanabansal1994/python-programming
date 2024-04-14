# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file:
        content= file.read()
        content= ("".join([word for word in content if word not in '.,?'])).split("\n")
        content= " ".join(content).split(" ")

        return {word: content.count(word) for word in set(content) if content.count(word)>=lower_limit}

# Model Solution
from string import punctuation
 
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        content = f.read()
 
        # remove line breaks and punctuation
        content = content.replace("\n", " ")
        for punctuation_mark in punctuation:
            content = content.replace(punctuation_mark, "")
 
        words = content.split(" ")
        return {word: words.count(word) for word in words if words.count(word) >= lower_limit}