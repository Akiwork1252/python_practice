import random

from game_hokuto import hokuto
from game_eva import eva
from game_madoka import madoka

# *********メインクラス**********
# ユーザーの行動や表示
class Main:
    # ゲームリスト(表示用)
    game = {
        'H': '北斗の拳(1/349)',
        'E': 'エヴァンゲリオン(1/319)',
        'M': '魔法少女まどかマギカ(1/199)',
    }
    # 機種の関数リスト
    game_list = {
        'H': hokuto,
        'E': eva,
        'M': madoka
    }
    # ============================================
    # コンストラクタ
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.ball = 0  # パチンコ玉

    # ============================================
    # エントランス
    def entrance(self):
        while True:
            print('パチンコで遊びますか（y/n）')
            choice = input(': ')
            if choice == 'n':  # 退店する
                print('またのご来店をお待ちしております。')
                break
            elif choice == 'y':  # 入場する
                # 残金があるか判定する
                if self.money < 500:
                    print(f'お金が不足しています。遊技には５００円必要です。残金：{self.money}')
                    break
                else:
                    self.display()

            else:
                print('入力が正しくありません。')
        return self.money

    # ============================================
    # パチンコ台を表示して、ユーザーが機種を選択する
    def display(self):
        while True:
            print('下記から遊技したいゲームを選んで、対応するキーを入力してください。')
            for k, v in Main.game.items():
                print(f'・{v} >>> キー:{k}')
            choice = input('user: ')
            if choice in Main.game:
                print(f'"CR{Main.game[choice]}"で遊びます。')
                Main.game_list[choice](self.money)
                break
            else:
                print('入力されたキーが正しくありません。もう一度やり直してください!!!')
                print('*'*20)


# *********パチンコクラス**********
class Pachinko:
    # パチンコ玉に変換する
    def lend(self):
        while True:
            print('500円＞＞＞125玉')
            choice = input('変換しますか？(y/n): ')
            if choice == 'n':
                print('遊技を終了します。')
                break
            elif choice == 'y':
                self.money -= 500  # ユーザーの残金から５００円を引く
                self.ball += 125  # パチンコ玉１２５玉
                return self.money, self.ball
            else:
                print('入力が正しくありません。')

    # パチンコ玉をヘソに入れる（通常時）
    # ヘソに玉が入る確率：１４分の１　＞＞＞　２５０玉（１０００円）で平均１７回転
    def ball_goes_in(self, ball):
        while ball > 0:
            n = random.randint(1, 14)
            if n == 7:
                return n

