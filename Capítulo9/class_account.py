class Account():

    def __init__(self, pin, name, balance):
        self.pin = pin
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withDraw(self, amount):
        if amount > self.balance:
            print("Insuficient funds, insert another value.")
        else:
            self.balance -= amount
            print("Withdraw successful!")
    
    def getBalance(self):
        return self.balance
    
    def getName(self):
        return self.name
    
    def getPin(self):
        return self.pin
    
    def __str__(self):
        return

account1 = Account(1000, "Diogo Minoru Kokubu", 1000)
account2 = Account(1001, "Diogo Minoru Kokubu", 10000)
account3 = Account(1002, "Ariovaldo Silva", 15000)
account4 = Account(1003, "Ariovaldo Silva", 10000)
account5 = Account(1004, "Ariovaldo Silva", 2000)
account6 = Account(1005, "Capelando", 100)
