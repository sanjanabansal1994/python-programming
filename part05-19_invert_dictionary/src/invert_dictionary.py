# Write your solution here
def invert(dictionary: dict):
    key_list= list(dictionary.keys())
    values= list(dictionary.values())
    dictionary.clear()
    for i in range(0,len(values)):
        dictionary[values[i]]=key_list[i]
