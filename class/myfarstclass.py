class Person:
    num_legs = 2
    count = 0

    def __init__(self, name, age, gender):
        # constructor
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f'{self.num_legs}本の足で{self.name}は歩きました。')

    def run(self):
        print(f'{self.num_legs}本の足で{self.name}は走りました。')


tom = Person('Tom', 12, 'male')
john = Person('John', 32, 'male')
emma = Person('Emma', 27, "female")
print(tom.name)
print(tom.age)
print(tom.gender)
tom.walk()
print('*'*3)
Person.num_legs = 3
tom.run()
tom.num_legs = 4  # クラス変数にはインスタンス変数でアクセスしない。クラス変数を更新する場合はクラス.でアクセスする
print('*'*3)
tom.walk()
emma.walk()
print(f'count: {Person.count}')
luffy = Person('Luffy', 19, 'male')
print('インスタンスLuffyを作った')
print(f'count: {Person.count}')

