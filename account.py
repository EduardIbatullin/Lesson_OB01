
class Account:

    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Вы пополнили счет на {amount} руб. Сумма на счёте: {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Вы сняли со счета {amount} руб. Сумма на счёте: {self.balance}.")
        elif amount < 0:
            print("не корректно введена сумма.")
        else:
            print("Не достаточно средств на счете.")

    def all_balance(self):
        print(f"Сумма на счёте: {self.balance}.")


man = Account(123, 1000)
man.all_balance()
man.withdraw(500)
man.withdraw(600)
man.deposit(23000)
