class Account:
    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.count += 1

    def withdraw(self, amount):
        if self.balance < amount:
            print(f'残高が不足しているため{amount}円は引き出せません：残高{self.balance}')
        else:
            print(f'アカウント名：残高　　{self.name}：{self.balance}')
            self.balance -= amount
            print(f'引き出し額：{amount}円＞＞＞残高：{self.balance}')

    def deposit(self, amount):
        print(f'アカウント名：残高　　{self.name}：{self.balance}')
        self.balance += amount
        print(f'入金額：{amount}円＞＞＞残高：{self.balance}')


aki = Account('Akinori', 1000)
tom = Account('Tom', 500)
aki.withdraw(500)
