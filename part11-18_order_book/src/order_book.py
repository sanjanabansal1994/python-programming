# Write your solution here:
class Task:
    instances=0
    def __init__(self,description:str, name:str, hours:int):

        self.description= description
        self.programmer= name
        self.workload= hours
        Task.instances+=1
        self.id = Task.instances
        self.__status = False

    def is_finished(self):
        return self.__status

    def mark_finished(self):
        self.__status = True
    
    def __str__(self):
        if self.__status:
            t= 'FINISHED'
        else:
            t= 'NOT FINISHED'
        return (f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {t}')

class OrderBook:
    def __init__(self):
        self.__orders=[]
        self.__programmers=[]

    def add_order(self, description, programmer, workload):
        t= Task(description, programmer, workload)
        self.__orders.append(t)

    def all_orders(self):
        return self.__orders

    def programmers(self):
        for t in self.__orders:
            self.__programmers.append(t.programmer)
        return list(set(self.__programmers))

    def mark_finished(self, id: int):
        if id not in [t.id for t in self.__orders]:
            raise ValueError(" No such id exist")
        for t in self.__orders:
            if t.id==id:
                t.mark_finished()
    def finished_orders(self):
        return [t for t in self.__orders if (t.is_finished())]

    def unfinished_orders(self):
        return [t for t in self.__orders if not (t.is_finished())]

    def status_of_programmer(self, programmer: str):
        if programmer not in [t.programmer for t in self.__orders]:
            raise ValueError(" No such programmer exist")
        finished= [t.workload for t in self.finished_orders() if (t.programmer == programmer)]
        unfinished = [t.workload for t in self.unfinished_orders() if (t.programmer == programmer)]
        return (len(finished), len(unfinished), sum(finished), sum( unfinished))


# Model Solution

class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id
 
    def __init__(self, description, programmer, workload):
        self.programmer = programmer
        self.description = description
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False
    
    def is_finished(self):
        return self.finished 
 
    def mark_finished(self):
        self.finished = True
 
    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
 
class OrderBook:
    def __init__(self):
        self.__tasks = []
 
    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
 
    def all_orders(self):
        return self.__tasks
 
    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))
 
    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        # not incorrect
        raise ValueError("wrong id")
    
    def unfinished_orders(self):
        return [t for t in self.__tasks if not t.is_finished()]
 
    def finished_orders(self):
        return [t for t in self.__tasks if t.is_finished()]
 
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        
        finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished() ]
        not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished() ]
 
        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)
 
        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)