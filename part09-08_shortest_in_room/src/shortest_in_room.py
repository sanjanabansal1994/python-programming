# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)
    
    def is_empty(self):
        return len(self.people)==0

    def print_contents(self):
        for person in self.people:
            print(f'{person.name} ({person.height} cm)')
    
    def shortest(self):
        if len(self.people)>0:
            height= self.people[0].height
            res= self.people[0]
            for person in self.people:
                if person.height < height:
                    res= person
                    height= person.height 
            return res
        else:
            return None

    def remove_shortest(self):
        if Room.is_empty(self):
            return None
        else:
            res= Room.shortest(self)
            self.people.remove(res)
            return res
        

# room = Room()

# room.add(Person("Lea", 183))
# room.add(Person("Kenya", 172))
# room.add(Person("Nina", 162))
# room.add(Person("Ally", 166))
# room.print_contents()

# print()

# removed = room.remove_shortest()
# print(f"Removed from room: {removed.name}")

# print()

# room.print_contents()