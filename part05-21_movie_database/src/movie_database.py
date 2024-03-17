# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new={}
    new["name"]=name
    new["director"]=director
    new["year"]= year
    new["runtime"]= runtime
    database.append(new)

# database = []
# add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
# add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
# print(database)