import random


class CoinCase:

    def __init__(self):
        self.quarters = random.randrange(0, 11)
        self.dimes = random.randrange(0, 11)
        self.nickels = random.randrange(0, 11)
        self.pennies = random.randrange(0, 11)

        self.qtotal = self.quarters * 25
        self.dtotal = self.dimes * 10
        self.ntotal = self.nickels * 5
        self.ptotal = self.pennies * 1

        self.total = self.qtotal + self.dtotal + self.ntotal + self.ptotal

        self.withdraw = random.randint(0, 100)
        self.mod5 = self.withdraw % 5
        self.mod10 = self.withdraw % 10
        self.mod25 = self.withdraw % 25

    def removeCoin(self, coin):
        if coin == 'quarter':
            self.quarters -= 1
            self.qtotal = self.quarters * 25
        elif coin == 'dime':
            self.dimes -= 1
            self.dtotal = self.dimes * 10
        elif coin == 'nickel':
            self.nickels -= 1
            self.ntotal = self.nickels * 10
        elif coin == 'penny':
            self.pennies -= 1
            self.ptotal = self.pennies * 10

    def caseContains(self):
        print('Quarters: ' + str(self.quarters) + ' ,Dimes: ' + str(self.dimes) +
              ' ,Nickels: ' + str(self.nickels) + ' ,Pennies: ' + str(self.pennies) + ' ,Total: ' + str(self.total))

    def getMod(self, amount):
        self.mod5 = amount % 5
        self.mod10 = amount % 10
        self.mod25 = amount % 25
