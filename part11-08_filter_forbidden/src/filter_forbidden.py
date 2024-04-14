# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    return " ".join(["".join([char for char in word if char not in forbidden ]) for word in string.split(" ")])