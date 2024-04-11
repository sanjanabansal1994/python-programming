# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    @property
    def __money(self):
        m= self.__euros + (self.__cents*0.01)
        return m

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __eq__(self, another):
        return self.__money == another.__money

    def __gt__(self, another):
        return self.__money > another.__money
    
    def __lt__(self, another):
        return self.__money < another.__money

    def __ne__(self, another):
        return self.__money != another.__money

    def __add__(self, another):
        return f'{(self.__money + another.__money):0.2f} eur'

    def __sub__(self, another):
        s = self.__money - another.__money
        if s<0:
            raise ValueError(f"a negative result is not allowed")
        else:
            return f'{s:0.2f} eur'

