import random

class Person:
    account_count = 0
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        self.__step_count = 0
        Person.account_count += 1

    def walk(self):
        count = random.randint(1, 6)
        self.__step_count += count
        print(f'{self.__name}はサイコロで{count}を出しました。')
        print(f'＞＞＞スタート値から{self.__step_count}歩進みました。')
        print()

    def difference(self, partner):
        difference = self.__step_count - partner.__step_count
        if difference < 0:
            print(f'  現在の{self.__name}と{partner.__name}との差は{-difference}歩です\n')
        else:
            print(f'  現在の{self.__name}の{partner.__name}との差は{difference}歩です\n')


aki = Person('Aki', 37)
tom = Person('Tom', 22)
john = Person('John', 19)

def func():
    while True:
        yield aki
        yield tom
        yield john


goal = 30
print(f'{Person.account_count}人で勝負します')
for i in func():
    i.walk()
    if i._Person__step_count >= goal:
        print(f'{i._Person__name}がゴールしました。')
        print('プログラムを終了します。')
        break