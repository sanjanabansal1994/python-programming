# Write your solution here
def search_by_name(filename: str, word: str):
    with open(filename) as file:
        file_copy=[]
        for line in file:
            file_copy.append(line.strip())
        
        recipe={}
        spaces=[]
        for i in range(0, len(file_copy)):
            if file_copy[i]=="":
                spaces.append(i)
        for i in range(0, len(file_copy)):
            if i in spaces:
                s=i+1
                recipe[file_copy[s]]=[]
            elif i==0:
                s=i
                recipe[file_copy[s]]=[]
            elif file_copy[s]!= file_copy[i]:
                recipe[file_copy[s]].append(file_copy[i])
            else:
                continue
    found_list=[]
    print(recipe.keys())
    for keys in recipe.keys():
        print(keys)
        if word.lower() in keys.lower():
            found_list.append(keys)
    return found_list
# found_recipes = search_by_name("recipes1.txt", "cake")

# for item in found_recipes:
#     print(item)

def search_by_time(filename: str, prep_time: int):
    with open(filename) as file:
        file_copy=[]
        for line in file:
            file_copy.append(line.strip())
    recipe=[]
    for i in range(0,len(file_copy)):
        if file_copy[i].isdigit():
            if prep_time > int(file_copy[i]):
                recipe.append(f'{file_copy[i-1]}, preparation time {file_copy[i]} min')
    return recipe

# found_recipes = search_by_time("recipes1.txt", 20)

# for recipe in found_recipes:
#     print(recipe)

def search_by_ingredient(filename: str, ingredient: str):
    with open(filename) as file:
        file_copy=[]
        for line in file:
            file_copy.append(line.strip())
        recipe={}
        spaces=[]
        for i in range(0, len(file_copy)):
            if file_copy[i]=="":
                spaces.append(i)
        for i in range(0, len(file_copy)):
            if i in spaces:
                s=i+1
                recipe[file_copy[s]]=[]
            elif i==0:
                s=i
                recipe[file_copy[s]]=[]
            elif file_copy[s]!= file_copy[i]:
                recipe[file_copy[s]].append(file_copy[i])
            else:
                continue
    found_list=[]
    for keys, values in recipe.items():
        if ingredient in values:
            string= f'{keys}, preparation time {values[0]} min'
            found_list.append(string)
    return found_list
    
# found_recipes = search_by_ingredient("recipes1.txt", "eggs")

# for recipe in found_recipes:
#     print(recipe)