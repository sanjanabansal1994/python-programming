# Write your solution here
import json

class Player:
    def __init__(self, player:dict):
        self.name= player["name"]
        self.country= player["nationality"]
        self.assists= player["assists"]
        self.goals= player["goals"]
        self.penalties= player["penalties"]
        self.team = player["team"]
        self.games= player["games"]
        self.points= int(player["assists"]) + int(player["goals"])
    
    def __str__(self):
        p= f'{self.name:21}{self.team}{self.goals:>4} +{self.assists:>3} = {self.assists+self.goals:>3}'
        return p

class HockeyStats:
    def __init__(self):
        self.players= []
        self.all_countries= []
        self.all_teams=[]

    def add_player(self, player:dict):
        self.players.append(player)

    def search_for_player(self):
        name= input("name: ")
        for p in self.players:
            if name == p["name"]:
                print(Player(p))
    
    def help(self):
        help_str = """commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals"""
        print(help_str)

    def add_teams(self):
        for p in self.players:
            if not p["team"] in self.all_teams:
                self.all_teams.append(p["team"])
        for p in sorted(self.all_teams):
            print(p)    
    
    def add_countries(self):
        for p in self.players:
            if not p["nationality"] in self.all_countries:
                self.all_countries.append(p["nationality"])
        for p in sorted(self.all_countries):
            print(p)

    def player_in_team(self):
        team = input("team: ")
        team_p = list(filter(lambda p: p["team"]==team, self.players))
        sorted_team = sorted((team_p), key= (lambda p: Player(p).points), reverse= True)
        [print(Player(player)) for player in sorted_team]

    def player_from_country(self):
        country = input("country: ")
        team_p = list(filter(lambda p: p["nationality"]==country, self.players))
        sorted_team = sorted((team_p), key= (lambda p:Player(p).points), reverse= True)
        [print(Player(player)) for player in sorted_team]
    
    def most_points(self):
        n= input("how many:")
        most_point= sorted(self.players, key= lambda player: (Player(player).points, Player(player).goals), reverse= True)
        i=0    
        while i<int(n):
            print(Player(most_point[i]))
            i+=1
    
    def most_goals(self):
        n= input("how many:")
        most_goals = sorted(self.players, key= lambda player: (Player(player).goals, -Player(player).games), reverse= True)
        i=0    
        while i<int(n):
            print(Player(most_goals[i]))
            i+=1

    def execute(self):
        filename= input("file name: ")
        with open(filename) as file:
            content= file.read()
            data= json.loads(content)
        for p in data:
            self.add_player(p)
        
        print(f'read the data of {len(data)} players')
        self.help()
        while True:
            command= input("commands: ")
            if command == '0':
                break
            if command=="1":
                self.search_for_player()
            if command == "2":
                self.add_teams()
            if command == "3":
                self.add_countries()
            if command == "4":
                self.player_in_team()
            if command == "5":
                self.player_from_country()
            if command == "6":
                self.most_points()
            if command == "7":
                self.most_goals()



app= HockeyStats()
app.execute()
