# Write your solution here
def new_person(name: str, age: int):
    if name=='' or len(name)>40 or len(name.split(" "))<2 or 0>age or age>150:
        raise ValueError()
    else:
        return name,age
