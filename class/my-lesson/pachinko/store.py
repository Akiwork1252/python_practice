import random
from hokuto import lottery, lottery_bonus

# ===============================================================
# パチンコ店のクラス　
# （インスタンス作成、入場制限、機種の表示、機種スペックの表示、パチンコの共通機能）
class Store:
    # コンストラクタ
    def __init__(self, name, age, money=0):
        self.name = name
        self.age = age  # 入店時のみ使用
        self.money = money
        self.ball = 0
        self.investment_amount = 0  # 総投資額を計算する

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

    # 選択機種の表示  (戻り値：choice)
    def display(self):
        # 設置機種
        game = {
            'H': '・CR北斗の拳 (1/349)',
            'E': '・CRエヴァンゲリオン (1/319)',
            'M': '・CR魔法少女まどかマギカ (1/199)',
            '#': '・各機種のスペックを一覧表示する。',
            '$': '・お金を追加する。',
            '*': '・店を出る。',
        }
        while True:
            print('下記メニューから遊技台の選択、もしくはその他アクションを選択して、対応キーを入力してください。')
            print('-'*10, 'メニュー', '-'*10)
            for k, v in game.items():
                if k == 'H':
                    print('＜遊技台＞')
                if k == '#':
                    print('＜その他メニュー＞')
                print(f'{v} >>> キー：{k}')
            print('-'*20)
            choice = input('user: ')
            if choice == '#':
                Store.display_spec()
            elif choice == '*':
                self.investment_amount = 0  # 退店時に投資額を初期化
                return None
            elif choice == '$':
                print(f'これまでの投資額：{self.investment_amount}円')
                print('お金を追加します。金額を半角英数字で入力してください。')
                money = int(input('(例:5000): '))
                self.money += money  # 所持金を増やす
                input(f'あなたの所持金は{self.money}円になりました。Enterキーを押してください。')
            elif (choice in game) and (choice != '#') and (choice != '*') and (choice != '$'):
                if self.money < 500:
                    input('お金がないので遊べません。Enterキーを押してください。')
                else:
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
            'CR北斗の拳': ['1/349', '+300(80%) or +1500(20%)',
                       '確率変動:100%', '当選:1/40 転落:1/150,  回転数:∞',
                       '+300(25%) or +1500(75%)'],
            'CRエヴァンゲリオン': ['1/319', '+450(75%) or +1500(25%)',
                           '確率変動:70%, チャンスタイム(100回転:大当り確率1/170):30%', '当選:1/90 回転数:170回転',
                           'ALL+1500'],
            'CR魔法少女まどかマギカ': ['1/199', '+450',
                             '確率変動:50%, 通常:50%', '1/70 回転数:70回転, (確率変動<上位>時の確率): 1/60: 回転数:120回転',
                             'ALL+1500'],
        }
        input('\n各機種のスペックを表示します。Enterキーを押してください。。')
        print('*'*20, 'スペック一覧', '*'*20)
        for k, v in spec.items():
            print(f"""
            {k}:
            (通常時の大当り確率): {v[0]}, (初当たり出玉): {v[1]}, 
            (初当たり振り分け): {v[2]}, (確率変動時の大当り確率): {v[3]},
            (確率変動時の出玉振り分け): {v[4]},
            """)
        print('*'*50)
        input('Enterキーを押すとメニュー画面に戻ります。')

    # パチンコ玉に変換する
    def lend(self):
        while True:
            # print('\n500円で125玉と交換できます。')
            choice = input('\n500円で125玉と交換できます。交換しますか？(y/n): ')
            if choice == 'n':
                return None
            elif choice == 'y':
                self.money -= 500  # ユーザーの残金から５００円を引く
                self.investment_amount += 500  # 総投資額加算
                self.ball += 125  # パチンコ玉１２５玉
                return self.ball
            else:
                print('入力が正しくありません。')

    # パチンコ玉をヘソに入れる（通常時）　ヘソに入る確率：約7%　＞＞　１０００円２５０玉で平均１７回転
    @staticmethod
    def ball_goes_in(ball):
        n = random.randint(1, 14)
        # ７でヘソに入賞
        if n == 7:
            return n
        else:
            return None

    # パチンコ玉をヘソに入れる（確率変動時）　ヘソに入る確率：90%
    @staticmethod
    def ball_goes_in_bonus(ball):
        n = random.randint(1, 10)
        # ７以外でヘソに入賞
        if n != 7:
            return n
        else:
            return None

    # 回転数の表示（通常時）
    @staticmethod
    def num_of_rotations(count):
        print(f'>>> 現在の回転数：{count}回転', end=' ')
        print()

    # 回転数の表示（確変時）
    @staticmethod
    def num_of_rotations_b(count):
        print(f'>>> 回転数：{count}回転', end='')
        print()

    # 大当り終了時の結果を表示
    @staticmethod
    def result(count, balls):
        print('='*8, '大当り結果', '='*8)
        print(f'総ボーナス数：{count}回')
        print(f'総獲得出玉：{balls}玉')
        print('='*20)

    # 獲得した出玉をお金に変換して結果を表示する。
    def cashing_out(self, ball):
        income = (ball * 4) + self.ball  # 引数で受け取った獲得玉と大当り前の残玉(self.ball)を足す
        Pachinko.bonus_balls = 0  # 持ち玉を０にする。
        input(f'総獲得出玉”{ball}玉”を1玉4円で換金します。Enterキーを押してください。')
        print('='*20)
        print(f'獲得出玉{ball}玉　>>> {income}円')
        print('='*20)
        ball = 0  # 出玉をリセット
        return income

    # 収益の計算と表示
    def revenue(self, income):
        input('収益を表示します。Enterキーを押してください。')
        before = self.money
        self.money += income  # 出玉を現金換算して加算
        revenue = self.money - self.investment_amount
        print('='*10)
        print(f'所持金：{before}円　>>> {self.money}円')
        print(f'総投資額:{self.investment_amount}円')
        if revenue > 0:
            print(f'プラス{revenue}円でした。')
            print('='*10)
            print('おめでとうございます。', end='')
        else:
            print(f'マイナス{-revenue}円でした。')
            print('='*10)
            print('残念でしたね。', end='')

# ================================================================================
# パチンコ台のクラス　（各機種のスペック）
class Pachinko(Store):
    count = 0  # 回転数
    count_b = 0  # 確率変動時の回転数
    bonus_num = 0  # ボーナス数のカウント
    bonus_balls = 0  # ボーナス時の出玉のカウント
    replay = 0  # 大当り終了後に再プレイするときに使用
    bonus_list = []  # ボーナスを記録
# =================================================
# スペック:CR北斗の拳:
# (通常時の大当り確率): 1/349, (初当たり出玉): +300(4/5) or +1500(1/5),
# (確率変動突入率): 100%, (確率変動時の大当り確率): 当たり:1/40, 転落:1/150,
# (確率変動時の出玉振り分け): +300(1/4) or +1500(3/4)

    def hokuto(self, ball=0):  # ball:遊戯で獲得したball (self.ballとは別) <= 貯玉での遊技で使用
        print('CR北斗の拳で遊びます。')
        while (self.money >= 500) or (Pachinko.bonus_balls > 0):
            # 持ち玉が無かったら玉を購入
            if Pachinko.bonus_balls == 0:
                ball = Store.lend(self)  # lend() >>> self.ball += 125
            # lend()で玉への変換を拒否した場合。
            if ball is None:
                input('遊技を終了します。Enterキーを押すとメニュー画面に戻ります。')
                break
            else:
                if Pachinko.bonus_balls == 0:
                    print('交換完了：500円 ＞＞＞ 125玉')
                user_action = input('Enterキーを押すと玉が発射されます。')
                while (self.ball > 0) or (Pachinko.bonus_balls > 0):
                    # 持ち玉がない場合
                    if Pachinko.bonus_balls == 0:
                        navel = Store.ball_goes_in(ball)  # ball_goes_in() >>> 戻り値{None:消化、n:ヘソ入賞}
                        # 玉の入賞判定 (通常時7%)
                        if navel is None:
                            self.ball -= 1  # 所持玉が減る
                            continue
                        else:
                            Pachinko.count += 1 # 回転数
                            jackpot = lottery()  # lottery() >>> 戻り値{None:ハズレ、int型:当たり}
                            # 大当りの抽選判定
                            if jackpot is None:
                                continue
                            # 大当り！　＞＞＞確率変動突入
                            else:
                                Pachinko.bonus_num += 1  # 大当り回数をカウント
                                Pachinko.bonus_balls += jackpot  # 大当り総獲得出玉
                                Pachinko.bonus_list.append(jackpot)
                                input(f'{Pachinko.count}回転目で大当りを引きました。おめでとうございます。　Enterを押してください。')
                                print(f'\n*確率変動*: {Pachinko.bonus_num}回目')
                                input('Enterキーを押すと玉が発射されます。')
                                Pachinko.count += 1 # 大当りを引いたら通常時の回転数を初期化
                                # 大当り(1/40)転落(1/150)どちらか引くまで確率変動ループ
                                while True:
                                    n = Store.ball_goes_in_bonus(ball)  # ball_goes_in_bonus() >>> 戻り値{n:ヘソ入賞、None:消化}
                                    # 玉の入賞判定　(確率変動時90%)
                                    if n is None:
                                        ball -= 1  # 所持玉が減る
                                        continue
                                    else:
                                        Pachinko.count_b += 1  # 回転数
                                        jackpot_b = lottery_bonus()  # lottery_bonus() >>> 戻り値{None:回転、int型:大当り、str型:転落}
                                        # 大当りor転落の抽選判定
                                        if jackpot_b is None:
                                            Pachinko.count_b += 1  # ボーナス時の回転数をカウント
                                            continue
                                        elif type(jackpot_b) is int:
                                            Pachinko.bonus_balls += jackpot_b  # 大当り総獲得出玉
                                            Pachinko.bonus_num += 1
                                            Store.num_of_rotations_b(Pachinko.count_b)  # 回転数表示
                                            print(f'>>> 大当り:{Pachinko.bonus_num}回獲得！　総出玉:{Pachinko.bonus_balls}玉')
                                            print()
                                            print(f'*確率変動*: {Pachinko.bonus_num}回目')
                                            Pachinko.bonus_list.append(jackpot_b)
                                            Pachinko.count_b = 0  # 回転数を初期化
                                            input('キーを押すと玉が発射されます。')
                                            continue
                                        elif type(jackpot_b) is str:
                                            Store.num_of_rotations_b(Pachinko.count_b)
                                            input('ボーナスを終了します。Enterキーを押してください。')
                                            Store.result(Pachinko.bonus_num, Pachinko.bonus_balls)
                                            Pachinko.count_b = 0  # 回転数を初期化
                                            break
                    # ボーナスが１回目じゃなければ一度ループを抜ける
                    else:
                        break
                # ボーナス０回(bonus_balls=0)
                if Pachinko.bonus_balls == 0:
                    print('玉が無くなりました。', end=' ')
                    Store.num_of_rotations(Pachinko.count)
                else:
                    print('獲得出玉で遊技を続けますか？ (y/n)')
                    choice = input(': ')
                    # 遊技継続の場合は再度自身の関数を呼ぶ
                    if choice == 'y':
                        Pachinko.replay += 1
                        return Pachinko.hokuto(self)  # 再プレイなら自身の関数を呼ぶ
                    else:
                        print('遊技を終了します。')
                        income = Store.cashing_out(Pachinko.bonus_balls)  # cashing_out(ball) >>> 戻り値:income(=ball*4)
                        Store.revenue(self, income)
                        input('お疲れ様でした。Enterキーを押すとメニュー画面が表示されます。。')
                        break

        if self.money == 0:
            print('\nお金が無くなりました。退店したい場合は”y”を入力してください。')
            print('それ以外のキーを入力するとメニュー画面に戻ります。メニュー画面からお金の補填を行うことができます。')
            exiting = input('user:')
            if exiting == 'y':
                print('またのご来店をお待ちしております。')
                self.investment_amount = 0  # 投資額の初期化
                return exiting

# =================================================
# CRエヴァンゲリオン:
# (通常時の大当り確率): 1/319, (初当たり出玉): +450(75%) or +1500(25%),
# (初当たり振り分け): 確率変動:70%, チャンスタイム(100回転:大当り確率1/170):30%, (確率変動時の大当り確率): 当選:1/90 回転数:170回転,
# (確率変動時の出玉振り分け): ALL+1500,
    def eva(self, ball=0):
        print('CRエヴァンゲリオンで遊びます。')
        while self.money >= 500:
            # ボーナス０回(ball=0)なら玉を購入
            if len(Pachinko.bonus_list) == 0:
                ball = Store.lend(self)  # lend() >>> self.ball += 125
            if ball is None:
                print('遊技を終了します。')
                break
            else:
                print('交換完了：500円 ＞＞＞ 125玉')
                user_action = input('Enterキーを押すと玉が発射されます。')
                while self.ball > 0:
                    if Pachinko.bonus_num == 0:
                        navel = Store.ball_goes_in(ball)  # ball_goes_in() >>> 戻り値{None:消化、n:ヘソ入賞}
                        # 玉の入賞判定 (通常時１４分の１で入賞)
                        if navel is None:
                            self.ball -= 1  # 所持玉が減る
                            continue
                        else:
                            Pachinko.count += 1 # 回転数
                            jackpot = lottery()  # lottery() >>> 戻り値{None:ハズレ、int型:当たり}
                            # 大当りの抽選判定
                            if jackpot is None:
                                continue

    def madomagi(self):
        print('CR魔法少女まどかマギカで遊びます。')


