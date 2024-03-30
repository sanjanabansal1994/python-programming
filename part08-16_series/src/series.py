# Write your solution here:
class Series:

    def __init__(self,title:str,seasons:int,genres:list):
        self.title= title
        self.seasons= seasons
        self.genres= genres
        self.rating=[]
    
    def __str__(self):
        string1= f'{self.title} ({self.seasons} seasons)\n'
        string1= string1 + f'genres: {", ".join(self.genres)}\n'

        if len(self.rating)>0:
            string1= string1+ f'{len(self.rating)} ratings, average {(sum(self.rating)/len(self.rating)):.1f} points'
        else:
            string1= string1 + "no ratings"

        return string1
    
    def rate(self,rating: int):
        self.rating.append(rating)




def minimum_grade(rating: float, series_list: list):
    res=[]
    for series in series_list:
        if max(series.rating) >= rating:
            res.append(series)
    return res

def includes_genre(genre: str, series_list: list):
    res=[]
    for series in series_list:
        if genre in series.genres:
            res.append(series)
    return res

