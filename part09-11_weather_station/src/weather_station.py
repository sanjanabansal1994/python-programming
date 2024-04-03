# WRITE YOUR SOLUTION HERE:

class WeatherStation:

    def __init__(self, station:str):
        self.__station= station
        self.__observations= ['']

    def add_observation(self,observation: str):
        self.__observations.append(observation)

    def latest_observation(self):
        return self.__observations[-1]

    def number_of_observations(self):
        return len(self.__observations)-1

    def __str__(self):
        return f'{self.__station}, {self.number_of_observations()} observations'

