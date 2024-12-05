from store import Store
from store import Pachinko


class Main:
    # 各機種の関数ディクショナリー
    func_dict = {
        'H': Pachinko.hokuto,
        'E': Pachinko.eva,
        'M': Pachinko.madomagi,
    }
    play_dict = {}
    user_info_list = []
    @staticmethod
    def account_create():
        print('名前,年齢,所持金を入力してください。')
        name = input('名前: ')
        age = int(input('年齢： '))
        money = int(input('所持金: '))
        Main.user_info_list.append(age)
        Main.user_info_list.append(money)
        Main.play_dict[name] = Main.user_info_list
        # char:インスタンス作成
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
            while True:
                choice = char.display()
                if choice is None:
                    print('またのご来店をお待ちしております。')
                    break
                else:
                    ex = Main.func_dict[choice](char)
                    if ex == 'y':
                        break

Main.main()
# Main.account_create()
