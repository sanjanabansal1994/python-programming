# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self, owner:str, acc_number:str,balance:float):
        self.__owner= owner
        self.__acc_number= acc_number
        self.__balance= balance

    def __service_charge(self):
        self.__balance= 0.99* self.__balance
    
    def deposit(self,amount: float):
        if amount>0:
            self.__balance+=amount
            self.__service_charge()

    def withdraw(self, amount: float):
        if amount<= self.balance:
            self.balance-=amount
            self.__service_charge()

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,balance:float):
        self.__balance= balance


# account = BankAccount("Randy Riches", "12345-6789", 1000)
# account.withdraw(100)
# print(account.balance)
# account.deposit(100)
# print(account.balance)