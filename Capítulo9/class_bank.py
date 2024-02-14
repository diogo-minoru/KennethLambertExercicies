from class_account import Account

class Bank():
    def __init__(self):
        self.accounts = {}

    def __str__(self):
        return '\n'.join(map(str, self.accounts.values()))
    
    def makeKey(self, name, pin):
        return name + "/" + pin
    
    def add(self, account):
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        key = self.makeKey(name, pin)
        self.accounts.pop(key, None)

    def get(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)
    