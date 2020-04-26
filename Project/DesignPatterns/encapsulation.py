class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, balance):
        if balance > 0:
            self.__balance += balance

    def withDraw(self, balance):
        if balance > 0:
            self.__balance -= balance

    #def setBalance(self, balance):
    #    if balance > 0:
    #        self.__balance = balance

    def getBalance(self):
        return self.__balance


accountA = Account()

accountA.deposit(1000)
accountA.withDraw(200)
print(accountA.getBalance())
