from store import Store
from hokuto import Hokuto
from eva import eva
from madomagi import madomagi


class Main:
    # 機種の関数ディクショナリー
    func_dict = {
        'H': Hokuto.hokuto,
        'E': eva,
        'M': madomagi,
    }

    @staticmethod
    def account_create():
        print('アカウントを作成してください')
        name = input('名前: ')
        age = int(input('年齢： '))
        money = int(input('所持金: '))

        char = Store(name, age, money)
        print('-'*20)
        print('アカウントを作成しました。')
        print(f'名前： {char.name}')
        print(f'年齢： {char.age}')
        print(f'所持金： {char.money}')
        print('-'*20)

        return char

    @staticmethod
    def main():
        char = Main.account_create()
        judge = char.entrance()
        if judge is None:
            print('またのご来店をお待ちしております。')
        else:
            choice = char.display()
            Main.func_dict[choice](char.money)

Main.main()
