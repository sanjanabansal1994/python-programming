# Write your solution here
def histogram(word:str):
    hist={}
    for char in word:
        if char not in hist:
            hist[char]=""
        hist[char]+="*"
    for key, value in hist.items():
        print(f'{key} {value}')

# (histogram("abba"))