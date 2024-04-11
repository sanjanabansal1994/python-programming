# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day, month, year):
        self.__day= day
        self.__month= month
        self.__year= year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def __eq__(self, another):
        if self.year== another.year and self.month== another.month and self.day== another.day:
            return True
        else:
            return False
    
    def __ne__(self, another):
        if self.year != another.year or self.month != another.month or self.day != another.day:
            return True
        else:
            return False

    def __gt__(self, another):
        self_dt= int(f'{self.year:0004}{self.month:02}{self.day:02}')
        another_dt= int(f'{another.year:0004}{another.month:02}{another.day:02}')
        if self_dt > another_dt:
            return True
        else:
            return False

    def __lt__(self, another):
        self_dt= int(f'{self.year:0004}{self.month:02}{self.day:02}')
        another_dt= int(f'{another.year:0004}{another.month:02}{another.day:02}')
        if self_dt < another_dt:
            return True
        else:
            return False

    def __add__(self, days:int):
        d= (self.day) + (days)%30
        m= self.month+ (days)//30
        y= self.year 
        print(d,m,y)
        if d > 30:
            d= (d)%30
            m+=1
        if m > 12:
            y= self.year + ( m)//12
            m= (m)%12
        print(d,m,y)
        another= SimpleDate(d,m,y)
        return another
        
    def __sub__(self, another):
        y= self.year - another.year
        m= self.month - another.month
        d= self.day - another.day
        diff= (y*360)+(m*30)+d

        return abs(diff)
