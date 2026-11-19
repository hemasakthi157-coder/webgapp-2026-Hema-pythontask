
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    @property
    def balance(self):
        return self.__balance
acc = BankAccount("HEMA", 3000)
acc.deposit(500)
acc.withdraw(2000)
print(acc.balance)
