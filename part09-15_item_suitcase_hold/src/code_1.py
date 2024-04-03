# Write your solution here:

class Item:
    def __init__(self,name1,weight1):
        self.__name1= name1
        self.__weight1= weight1

    def name(self):
        return self.__name1
    
    def weight(self):
        return self.__weight1
        
    def __str__(self):
        return f'{self.__name1} ({self.__weight1} kg)'


class Suitcase:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__curr_weight = 0
        self.__items = []

    def add_item(self,item:Item):
        available = (self.__max_weight)-(self.__curr_weight)
        if item.weight()< available:
            self.__items.append(item)
            self.__curr_weight+= item.weight()

    def weight(self):
        return self.__curr_weight

    def print_items(self):
        for i in self.__items:
            print(f'{i.name()} ({i.weight()} kg)')

    def heaviest_item(self):
        if len(self.__items)>0:
            weight=0
            for i in self.__items:
                if i.weight()>weight:
                    weight= i.weight()
                    res= i
            return res
        else:
            return None

    def __str__(self):
        if len(self.__items) >1:
            return f'{len(self.__items)} items ({self.__curr_weight} kg)'
        elif len(self.__items)==1:
            return f'{len(self.__items)} item ({self.__curr_weight} kg)'
        else:
            return f'0 items (0 kg)'

class CargoHold:

    def __init__(self,max_weight):
        self.__max_weight= max_weight
        self.__available_weight= max_weight
        self.__suitcases=[]

    def add_suitcase(self, suitcase:Suitcase):
        if suitcase.weight()< self.__available_weight:
            self.__suitcases.append(suitcase)
            self.__available_weight -= suitcase.weight()
    
    def __str__(self):
        if len(self.__suitcases)>1:
            return f'{len(self.__suitcases)} suitcases, space for {self.__available_weight} kg'
        elif len(self.__suitcases)==1:
            return f'1 suitcase, space for {self.__available_weight} kg'
        else:
            return f'0 suitcases, space for {self.__max_weight} kg'

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

