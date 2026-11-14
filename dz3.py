import math
class BankAccount:
    def __init__(self, name, n, balance):
        self.name = name
        self.balance = balance
        self.n = n
class Bank:
    def __init__(self, add, take, send):
        self.add = add
        self.take = take
        self.send = send
    def add(self):
        self.BankAccount += self.add
    def take(self):
        self.BankAccount -= self.take
    def send(self):
        self.BankAccount -= self.send
BankAccount = BankAccount("User",10763452,5000)
add_money = Bank(int(input('add the desired ammount of money')))
take_money = Bank(int(input('take out the desired ammount of money')))
BankAccount.balance = Bank.balance - take_money
BankAccount.balance = Bank.balance + add_money
