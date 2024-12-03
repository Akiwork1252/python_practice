import random
from hokuto import lottery, lottery_bonus

# =================================================
# パチンコ店のクラス　（インスタンス作成、入場制限、設置機種の表示、機種スペックの表示、マネーをパチンコ玉に変換、パチンコの共通機能）
class Store:
    # コンストラクタ
    def __init__(self, name, age, money=0):
        self.name = name
        self.age = age
        self.money = money
        self.ball = 0

    # エントランス(20歳未満/所持金500円未満お断り）
    def entrance(self):
        min_age = 20
        min_money = 500
        if self.age < min_age:
            print(f'パチンコは{min_age}歳からです。')
        elif self.money < min_money:
            print(f'パチンコで遊ぶには{min_money}円以上必要です。')
        else:
            print('いらっしゃいませ')
            return self.age

    # 選択機種の表示
    def display(self):
        # 設置機種
        game = {
            'H': 'CR北斗の拳 (1/349)',
            'E': 'CRエヴァンゲリオン (1/319)',
            'M': 'CR魔法少女まどかマギカ (1/199)',
            '#': 'スペック詳細'
        }

        while True:
            print('遊技したい機種を下記メニューから選択して、対応するキーを入力してください。また"#"を入力すると各機種のスペックが表示されます。')
            print('-'*10, 'メニュー', '-'*10)
            for k, v in game.items():
                print(f'{v} >>> キー：{k}')
            print('-'*20)
            choice = input('user: ')
            if choice == '#':
                Store.display_spec()
            elif (choice in game) and (choice != '#'):
                print(f'あなたは{game[choice]}を選びました。')
                break
            else:
                print('入力されたキーが正しくありません。')

        return choice

    # 機種スペックの表示
    @staticmethod
    def display_spec():
        # ゲームスペック　[通常時大当り確率、初当たり出玉、RUSH突入率、RUSH時の大当り確率、RASH時の出玉振り分け]
        spec = {
            'CR北斗の拳': ['1/349', '+300(4/5) or +1500(1/5)', '100%', '当たり:1/40, 転落:1/150', '+300(1/4) or +1500(3/4)'],
            'CRエヴァンゲリオン': ['1/319', '+450(4/5) or +1500(1/5)', '70%', '1/90: 170回転', 'ALL+1500'],
            'CR魔法少女まどかマギカ': ['1/199', '+450', '40%', '1/70: 160回転', 'ALL+1500'],
        }
        print('各機種のスペックは以下になります。')
        print('*'*20, 'スペック一覧', '*'*20)
        for k, v in spec.items():
            print(f"""
            {k}:
            (通常時の大当り確率): {v[0]}, (初当たり出玉): {v[1]}, 
            (確率変動突入率): {v[2]}, (確率変動時の大当り確率): {v[3]},
            (確率変動時の出玉振り分け): {v[4]},
            """)
        print('*'*50)

    # パチンコ玉に変換する
    def lend(self):
        while True:
            print('500円＞＞＞125玉')
            choice = input('変換しますか？(y/n): ')
            if choice == 'n':
                break
            elif choice == 'y':
                self.money -= 500  # ユーザーの残金から５００円を引く
                self.ball += 125  # パチンコ玉１２５玉
                return self.ball
            else:
                print('入力が正しくありません。')

    # パチンコ玉をヘソに入れる（通常時）　ヘソに入る確率：１４分の１　＞＞　１０００円２５０玉で平均１７回転
    @staticmethod
    def ball_goes_in(ball):
        ball -= 1
        n = random.randint(1, 14)
        # ７でヘソに入賞
        if n == 7:
            ball += 1
            return n
        else:
            return None

    # パチンコ玉をヘソに入れる（確率変動時）　ヘソに入る確率：１０分の９
    @staticmethod
    def ball_goes_in_bonus(ball):
        ball -= 1
        n = random.randint(1, 10)
        # ７以外でヘソに入賞
        if n != 7:
            ball += 1
            return n
        else:
            return None

    # 大当り終了時の結果を表示
    @staticmethod
    def result(count, total):
        print('・・・結果・・・')
        print(f'ボーナス：{count}回')
        print(f'総獲得出玉：{total}')
        print('・'*10)

    # 回転数の表示
    @staticmethod
    def count(count):
        print(f'回転数：{count}', end=' ')


# =================================================
# パチンコ台のクラス　（各機種のスペック）
class Pachinko(Store):
    count = 0  # 回転数
    count_b = 0  # 確率変動時の回転数
    bonus_num = 0  # ボーナス数のカウント
    bonus_list = []  # ボーナスを記録
# =================================================
# スペック:CR北斗の拳:
# (通常時の大当り確率): 1/349, (初当たり出玉): +300(4/5) or +1500(1/5),
# (確率変動突入率): 100%, (確率変動時の大当り確率): 当たり:1/40, 転落:1/150,
# (確率変動時の出玉振り分け): +300(1/4) or +1500(3/4)
    def hokuto(self):
        print('CR北斗の拳で遊びます。')
        while True:
            ball = Store.lend(self)  # lend() >>> 戻り値:ball +125
            if ball is None:
                print('遊技を終了します。')
                break
            else:
                while ball > 0:
                    navel = Store.ball_goes_in(ball)  # ball_goes_in() >>> 戻り値{None:消化、n:ヘソ入賞}
                    # 玉の入賞判定 (通常時１４分の１で入賞)
                    if navel is None:
                        ball -= 1  # 所持玉が減る
                        continue
                    else:
                        Pachinko.count += 1 # 回転数
                        jackpot = lottery()  # lottery() >>> 戻り値{None:ハズレ、int型:当たり}
                        # 大当りの抽選判定
                        if jackpot is None:
                            continue
                        # 確率変動突入 大当り(1/40)転落(1/150)どちらか引くまで確率変動ループ
                        else:
                            Pachinko.bonus_num += 1
                            Pachinko.bonus_list.append(jackpot)
                            while True:
                                n = Store.ball_goes_in_bonus(ball)  # ball_goes_in_bonus() >>> 戻り値{n:ヘソ入賞、None:消化}
                                # 玉の入賞判定　(確率変動時１０分の９で入賞)
                                if n is None:
                                    ball -= 1  # 所持玉が減る
                                    continue
                                else:
                                    Pachinko.count_b += 1  # 回転数
                                    jackpot_b = lottery_bonus()  # lottery_bonus() >>> 戻り値{None:回転、int型:大当り、str型:転落}
                                    # 大当りor転落の抽選判定
                                    if jackpot_b is None:
                                        Pachinko.count_b += 1  # ボーナス時の回転数
                                        continue
                                    elif type(jackpot_b) is int:
                                        Pachinko.bonus_num += 1
                                        Store.count(Pachinko.count_b)
                                        Pachinko.bonus_list.append(jackpot_b)
                                        Pachinko.count_b = 0  # 回転数を初期化
                                        continue
                                    elif type(jackpot_b) is str:
                                        total = sum(Pachinko.bonus_list)  # 総獲得pt
                                        print('ボーナス終了です。')
                                        Store.result(Pachinko.bonus_num, total)


    def eva(self):
        print('CRエヴァンゲリオンで遊びます。')

    def madomagi(self):
        print('CR魔法少女まどかマギカで遊びます。')


