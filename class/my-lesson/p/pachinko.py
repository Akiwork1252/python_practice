import random

class Pachinko:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.ball = 0

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
    def ball_goes_in(self):
        self.ball -= 1
        n = random.randint(1, 14)
        if n == 7:
            return n
        else:
            return None


    # 抽選を行う（通常時）
    def lottery(self):
        n = random.randrange(1, 319)
        user = random.randrange(1, 319)
        if n == user:
            print('大当り')
        else:
            print('-')



luffy = Pachinko('Luffy', 10000)
luffy.lend()
print(f'ルフィの残金：{luffy.money}')
print(f'ルフィの貯玉：{luffy.ball}')


while luffy.ball > 0:
    n = luffy.ball_goes_in()
    if n is None:
        continue
    else:
        luffy.lottery()

