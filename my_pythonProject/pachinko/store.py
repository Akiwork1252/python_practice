import random
from hokuto import h_lottery, h_lottery_bonus
from eva import e_lottery, e_lottery_chance, e_lottery_bonus
from madomagi import m_lottery, m_lottery_bonus, m_lottery_bonus_plus


# ===============================================================
# パチンコ店のクラス　
#  インスタンス作成、入場制限、機種の表示、機種スペックの表示
#  パチンコの共通機能(玉変換、ヘソ入賞判定(通常・確変)、当たり抽選(通常・確変)、回転数表示(通常・確変)、Bonus結果、換金)
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
            # ユーザーがキーを入力するまで待機
            choice = Pachinko.user_action('user_choice')
            # 機種スペックを表示
            if choice == '#':
                Store.display_spec()
            # 退店
            elif choice == '*':
                self.investment_amount = 0  # 退店時に投資額を初期化
                return None

            # 所持金を追加
            elif choice == '$':
                print(f'これまでの投資額：{self.investment_amount}円,  所持金:{self.money}')
                print('お金を追加します。金額を半角英数字で入力してください。')
                money = int(input('(例:5000): '))
                self.money += money  # 所持金を増やす
                input(f'あなたの所持金は{self.money}円になりました。Enterキーを押してください。')
            # ユーザーが機種を選択した場合
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
                       '確率変動:100%', '当:1/25 転落:1/180,  回転数:どちらか引くまで継続',
                       '+300(25%) or +1500(75%)', '88%', 'なし'],
            'CRエヴァンゲリオン': ['1/319', '+450(75%) or +1500(25%)',
                           '確率変動:70%, チャンスタイム{100回転:大当り確率1/170}:30%', '当:1/90 回転数:170回転',
                           'ALL+1500', '85%', 'なし'],
            'CR魔法少女まどかマギカ': ['1/199', '+450(90%) or +1500(10%)',
                             '確率変動:50%, 通常:50%', '当:1/70 回転数:80回転, 当:1/60 回転数:120回転{確率変動<上位>}',
                             'ALL+1500', '68%, 86%{確率変動<上位>}', '確率変動中の当たり1/3で確率変動<上位>に突入'],
        }
        input('\n各機種のスペックを表示します。Enterキーを押してください。')
        print('*'*20, 'スペック一覧', '*'*20)
        for k, v in spec.items():
            print(f"""
            {k}:
            (通常時の大当り確率): {v[0]}, (初当たり出玉): {v[1]}, 
            (初当たり振り分け): {v[2]}, (確率変動時の大当り確率): {v[3]},
            (確率変動時の出玉振り分け): {v[4]}, (継続率): {v[5]}, (補足): {v[6]}, 
            """)
        print('*'*50)
        while True:  # ユーザーの応答を待つ
            enter = input('Enterキーを押すとメニュー画面に戻ります。')
            if type(enter) is str:
                break

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
    def ball_goes_in():
        n = random.randint(1, 14)
        # ７でヘソに入賞
        if n == 7:
            return n
        else:
            return None

    # パチンコ玉をヘソに入れる（確率変動時）　ヘソに入る確率：90%
    @staticmethod
    def ball_goes_in_bonus():
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

    # 確変時の情報表示
    def bonus_info(self, jackpot_b):
        if type(jackpot_b) is str:
            print(f' info:(転落当たり：{Pachinko.count_b+1}回転目)')
        else:
            print(f' info:(大当り獲得：{Pachinko.count_b+1}回転目)')
            print(f'     :(大当り{Pachinko.total_bonus_count}回目獲得! 総出玉:{Pachinko.bonus_pt-jackpot_b}玉 ＋ {jackpot_b}玉)')

    # 大当り終了時の結果を表示
    def result(self):
        print('\n', '='*8, '大当り結果', '='*8)
        print(f'総ボーナス数：{Pachinko.total_bonus_count}回'
              f'(BigBonus:{Pachinko.big_bonus_count}回、Bonus:{Pachinko.small_bonus_count}回)')
        print(f'ボーナス獲得出玉：{Pachinko.bonus_pt}玉')
        print(f'現在の持ち玉：{Pachinko.bonus_balls}玉')
        print('='*26)
        while True:  # ユーザーの応答を待つ
            enter = input('Enterキーを入力してください。')
            if type(enter) is str:
                break

    # 獲得した出玉をお金に変換して結果を表示する。
    def cashing(self):
        income = Pachinko.bonus_balls * 4
        input(f'持ち玉<{Pachinko.bonus_balls}玉>を1玉4円で換金します。Enterキーを押してください。')
        print('\n', '='*8, '換金', '='*8)
        print(f'持ち玉{Pachinko.bonus_balls}玉　>>> {income}円')
        print('='*23)
        Pachinko.bonus_balls = 0  # ボーナス出玉を０にする。
        return income

    # 収益の計算と表示
    def revenue(self, income):
        input('収支を表示します。Enterキーを押してください。')
        before = self.money
        self.money += income  # 出玉を現金換算して加算
        revenue = self.money - self.investment_amount  # 換金後の所持金から総投資額を引いて収益を計算
        print('\n', '='*8, '収支', '='*8)
        print(f'所持金：{before}円　>>> {self.money}円')
        print(f'総投資額:{self.investment_amount}円')
        if revenue > 0:
            print(f'プラス{revenue}円でした。')
            print('='*23)
            print('おめでとうございます。', end='')
        else:
            print(f'マイナス{-revenue}円でした。')
            print('='*23)
            print('残念でしたね。', end='')

    # ユーザーの入力
    @staticmethod
    def user_action(n):
        # ユーザー入力判定
        def input_judge(user):
            if (user != 'y') and (user != 'n'):
                print('入力が正しくありません')
            else:
                return user

        while True:
            if n == 'firing':
                user = input('Enterキーを押すと玉が発射されます。')
            elif n == 'menu':
                user = input('Enterキーを入力すると次の画面に進みます。')
            elif n == 'bonus_start':
                user = input('<確率変動>に突入します。Enterキーを押してください。')
            elif n == 'bonus_end':
                user = input('<確率変動>を終了します。Enterを押すと結果画面が表示されます。\n')
            elif n == 'replay_choice':
                while True:
                    user = input('\n獲得出玉で遊技を続けますか？ (y/n): ')
                    user = input_judge(user)
                    if user is not None:
                        break
            elif n == 'replay':
                while True:
                    user = input('\n持ち玉を使用して遊技を行いますか？(y/n): ')
                    user = input_judge(user)
                    if user is not None:
                        break
            elif n == 'replay_again':
                while True:
                    user = input('持ち玉を使い切りました。現金を使って遊技を継続しますか。(y/n)')
                    user = input_judge(user)
                    if user is not None:
                        break
            elif n == 'finished':
                user = input('お疲れ様でした。Enterキーを押すとメニュー画面が表示されます。')
            elif n == 'user_choice':
                user = input('user:')
            if type(user) is str:
                return user

    # 通常時の値
    def value_noemal(self):
        Pachinko.count = 0

    # 確変終了後の初期化
    def after_bonus(self):
        Pachinko.count_b = 0  # 回転数
        Pachinko.bonus_pt  = 0  # 獲得出玉（ボーナス終了後の結果表示で使用）
        Pachinko.total_bonus_count = 0  # 結果表示で使用
        Pachinko.big_bonus_count = 0  # 結果表示（内訳）で使用
        Pachinko.small_bonus_count = 0  # 結果表示（内訳）で使用

    # 再プレイ時（持ち玉遊技）の値
    def value_re(self):
        Pachinko.replay = 0  # 再プレイ時に使用
        Pachinko.replay_balls = 0  # 持ち玉遊技に使用

# ================================================================================
# パチンコ台のクラス
class Pachinko(Store):
    count_hokuto = 0  # 通常時回転数(北斗)
    count_eva = 0  # 通常時回転数(エヴァ)
    count_madoka = 0  # 通常時回転数(まどか)
    count_b = 0  # 確率変動時の回転数
    total_bonus_count = 0  # ボーナス数のカウント
    big_bonus_count = 0  # ボーナス内訳
    small_bonus_count = 0  # ボーナス内訳
    bonus_balls = 0  # ボーナス時の純増出玉（確変時の抽選で使用するため減少する）
    bonus_pt = 0  # ボーナスでの獲得出玉（ボーナスで獲得した出玉量。確変終了後の結果表示で使用する）
    before_bonus_balls = 0  # 持ち玉遊技時に使用した玉数の計算で使用
    replay = 0  # 大当り終了後に再プレイするときに使用
    replay_balls = 0  # 持ち玉遊技で使用
    bonus_list = []  # ボーナスを記録-
# ==================================================================================================
# スペック:CR北斗の拳:
# (通常時の大当り確率): 1/349, (初当たり出玉): +300(4/5) or +1500(1/5),
# (確率変動突入率): 100%, (確率変動時の大当り確率): 当たり:1/40, 転落:1/150,
# (確率変動時の出玉振り分け): +300(1/4) or +1500(3/4)

    def hokuto(self, ball=0):  # ball:遊戯で獲得したball (self.ballとは別) <= 貯玉での遊技で使用
        print('-'*20)
        print('CR北斗の拳で遊びます。')
        # 遊技準備
        while (self.money >= 500) or (Pachinko.bonus_balls > 0):
            # 再プレイではない場合(持ち玉遊技ではない場合)
            if Pachinko.bonus_balls == 0:
                ball = Store.lend(self)  # lend() >>> self.ball += 125
            # lend()で玉への変換を拒否した場合
            if ball is None:
                input('遊技を終了します。Enterキーを押すとメニュー画面に戻ります。')
                break
            else:
                if Pachinko.bonus_balls == 0:
                    print('交換完了：[現金:500円 ＞＞＞ 持ち玉:125玉]')
                # 再プレイ（持ち玉遊技）
                else:
                    re = 125  # 持ち玉遊技(=125玉)
                    replay_choice = Pachinko.user_action('replay')  # ユーザー：持ち玉を使用して遊技を行いますか？(y/n)
                    if replay_choice == 'y':
                        before = Pachinko.bonus_balls
                        if Pachinko.bonus_balls < re:
                            Pachinko.replay_balls = Pachinko.bonus_balls  #
                            print(f'{Pachinko.replay_balls}玉を払い出します。　[持ち玉:{Pachinko.bonus_balls}玉 >>> 0玉]')
                            Pachinko.bonus_balls = 0
                        else:
                            Pachinko.bonus_balls -= re  # 持ち玉から125玉引く
                            Pachinko.replay_balls += re  # 遊技玉に125玉追加する
                            print(f'{re}玉を払い出します。　＜持ち玉:{before}玉 >>> {Pachinko.bonus_balls}玉＞')
                    elif replay_choice == 'n':
                        print('遊技を終了します。')
                        income = Store.cashing(self)  # 戻り値:income(=ball*4)
                        Store.revenue(self, income)
                        Pachinko.user_action('finished')
                        Pachinko.replay = 0  # 再プレイを０に戻す。
                        break
                Pachinko.user_action('firing')  # ユーザー：Enterキーを押すと玉が発射されます。
                # 遊技
                while (self.ball > 0) or (Pachinko.replay_balls > 0):
                    if (Pachinko.replay == 0) or (Pachinko.replay_balls > 0):
                        navel = Store.ball_goes_in()  # 戻り値{None:消化、n:ヘソ入賞}
                        # 玉の入賞判定 (通常時7%で入賞) None:ヘソ入賞なし、int型:ヘソ入賞 -> 抽選
                        if navel is None:
                            if Pachinko.replay == 0:
                                self.ball -= 1  # 持ち玉が減る
                                continue
                            # 持ち玉遊技の場合
                            else:
                                Pachinko.replay_balls -= 1  # 持ち玉が減る
                                continue
                        else:
                            Pachinko.count_hokuto += 1 # 回転数
                            jackpot = h_lottery()  # 戻り値{None:ハズレ、int型:当たり}
                            # 大当りの抽選判定
                            if jackpot is None:
                                continue
                            # 大当り！　＞＞＞確率変動突入
                            else:
                                Pachinko.total_bonus_count += 1  # 大当り回数をカウント
                                Pachinko.bonus_balls += jackpot  # 大当り純増出玉(確変突入時の遊技で使用＝減少していく）
                                Pachinko.bonus_pt += jackpot  # 大当りでの獲得出玉
                                if jackpot == 1500:
                                    Pachinko.big_bonus_count += 1
                                elif jackpot == 300:
                                    Pachinko.small_bonus_count += 1
                                Pachinko.bonus_list.append(jackpot)
                                input(f'{Pachinko.count_hokuto}回転目で大当りを引きました。おめでとうございます\n')
                                Pachinko.user_action('bonus_start')
                                print(f'\n*確率変動*: {Pachinko.total_bonus_count}回目')
                                Pachinko.user_action('firing')  # ユーザー：Enterキーを押すと玉が発射されます。
                                Pachinko.count_hokuto = 0  # 大当りを引いたら通常時の回転数を初期化
                                # 大当り(1/40)転落(1/150)どちらか引くまで確率変動ループ
                                while True:
                                    n = Store.ball_goes_in_bonus()  # 戻り値{n:ヘソ入賞、None:消化}
                                    # 玉の入賞判定　(確率変動時90%でヘソ入賞) None:ヘソ入賞なし、int型:ヘソ入賞->抽選
                                    if n is None:
                                        Pachinko.bonus_balls -= 1  # 持ち玉が減る
                                        continue
                                    else:
                                        Pachinko.count_b += 1  # 回転数
                                        Pachinko.count_b += 1  # ボーナス時の回転数をカウント
                                        jackpot_b = h_lottery_bonus()  # lottery_bonus() 抽選
                                        # 大当りor転落の抽選判定  None:ハズレ、int型:大当り、str型:転落
                                        if jackpot_b is None:
                                            continue
                                        elif type(jackpot_b) is int:
                                            Pachinko.bonus_balls += jackpot_b  # 大当り総獲得出玉
                                            Pachinko.bonus_pt += jackpot_b
                                            if jackpot_b == 1500:
                                                Pachinko.big_bonus_count += 1
                                            elif jackpot_b == 300:
                                                Pachinko.small_bonus_count += 1
                                            Pachinko.total_bonus_count += 1
                                            Store.bonus_info(self, jackpot_b)  # 情報表示
                                            print()
                                            print(f'*確率変動*: {Pachinko.total_bonus_count}回目')
                                            Pachinko.bonus_list.append(jackpot_b)
                                            Pachinko.count_b = 0  # 大当り時の回転数を初期化
                                            input('キーを押すと玉が発射されます。')
                                            continue
                                        elif type(jackpot_b) is str:
                                            Store.bonus_info(self, jackpot_b)  # 情報表示
                                            Pachinko.user_action('bonus_end')  # ユーザー：Enter
                                            if Pachinko.replay == 0:
                                                Pachinko.bonus_balls += self.ball  # 大当り前の持ち玉を獲得出玉に合算
                                                self.ball = 0  # 持ち玉を初期化
                                            else:
                                                Pachinko.bonus_balls += Pachinko.replay_balls  # 大当り前の持ち玉を獲得出玉に合算
                                                Pachinko.replay_balls = 0  # 持ち玉を初期化
                                            Pachinko.before_bonus_balls = Pachinko.bonus_balls  # 再プレイで使用した玉数を計算する時に使用
                                            Store.result(self)
                                            Pachinko.after_bonus(self)  # 確変終了後の初期化
                                            Pachinko.replay += 1  # 一度遊技ループから抜ける
                                            break
                    # ボーナス終了後に一度ループを抜けてユーザーのアクション選択画面(持ち玉遊技をするか)に移行する
                    else:
                        break
                # ボーナス０回(bonus_balls=0)
                if Pachinko.replay == 0:
                    print('持ち玉が無くなりました。', end=' ')
                    Store.num_of_rotations(Pachinko.count_hokuto)
                elif (Pachinko.replay_balls == 0) and (Pachinko.before_bonus_balls != Pachinko.bonus_balls):
                    print('玉が無くなりました。', end=' ')
                    Store.num_of_rotations(Pachinko.count_hokuto)
                    if Pachinko.bonus_balls == 0:
                        choice = Pachinko.user_action('replay_again')  # ユーザー：持ち玉を使い切りました。現金を使って遊技を継続しますか。(y/n)
                        if choice == 'y':
                            Pachinko.replay = 0  # 持ち玉を使い切った場合は０に戻す
                            return Pachinko.hokuto(self)
                        else:
                            input('メニュー画面に戻ります。Enterキーを押してください。')
                            break
                # ボーナスが終了
                elif Pachinko.replay > 0:
                    choice = Pachinko.user_action('replay_choice')  # 獲得出玉で遊技を続けますか？ (y/n):
                    # 遊技継続の場合は再度自身の関数を呼ぶ
                    if choice == 'y':
                        return Pachinko.hokuto(self)  # 再プレイなら自身の関数を呼ぶ
                    else:
                        print('遊技を終了します。')
                        income = Store.cashing(self)  # 戻り値:income(=ball*4)
                        Store.revenue(self, income)
                        Pachinko.replay = 0  # 再プレイを０に戻す。
                        Pachinko.user_action('finished')  # ユーザー：Enter
                        Pachinko.count_hokuto = 0  # 回転数を初期化
                        break

        if self.money == 0:
            print('\nお金が無くなりました。退店したい場合は ”*” を入力してください。')
            print('それ以外のキーを入力するとメニュー画面に戻ります。メニュー画面からお金の追加を行うことができます。')
            exiting = Pachinko.user_action('user_choice')  # ユーザー：退店orメニュー画面選択
            if exiting == '*':
                print('またのご来店をお待ちしております。')
                self.investment_amount = 0  # 投資額の初期化
                Pachinko.count_hokuto = 0  # 回転数を初期化
                return exiting
# ==================================================================================================
# CRエヴァンゲリオン:
# (通常時の大当り確率): 1/319, (初当たり出玉): +450(75%) or +1500(25%),
# (初当たり振り分け): 確率変動:70%, チャンスタイム(100回転:大当り確率1/170):30%, (確率変動時の大当り確率): 当選:1/90 回転数:170回転,
# (確率変動時の出玉振り分け): ALL+1500,

    def eva(self, ball=0):
        print('-'*20)
        print('CRエヴァンゲリオンで遊びます。')
        # 遊技準備
        while (self.money >= 500) or (Pachinko.bonus_balls > 0):
            # 再プレイではない場合(持ち玉遊技ではない場合)
            if Pachinko.bonus_balls == 0:
                ball = Store.lend(self)  # lend() >>> self.ball += 125
            # lend()で玉への変換を拒否した場合
            if ball is None:
                input('遊技を終了します。Enterキーを押すとメニュー画面に戻ります。')
                break
            else:
                if Pachinko.bonus_balls == 0:
                    print('交換完了：[現金:500円 ＞＞＞ 持ち玉:125玉]')
                # 再プレイ（持ち玉遊技）
                else:
                    re = 125  # 持ち玉遊技(=125玉)
                    replay_choice = Pachinko.user_action('replay')  # ユーザー：持ち玉を使用して遊技を行いますか？(y/n)
                    if replay_choice == 'y':
                        before = Pachinko.bonus_balls
                        # 持ち玉＜125玉であれば、持ち玉全てを遊技用に払い出す
                        if Pachinko.bonus_balls < re:
                            Pachinko.replay_balls = Pachinko.bonus_balls  ##################
                            print(f'{Pachinko.replay_balls}玉を払い出します。　[持ち玉:{Pachinko.bonus_balls}玉 >>> 0玉]')
                            Pachinko.bonus_balls = 0
                        else:
                            Pachinko.bonus_balls -= re  # 持ち玉から125玉引く
                            Pachinko.replay_balls += re  # 遊技玉に125玉追加する
                            print(f'{re}玉を払い出します。　＜持ち玉:{before}玉 >>> {Pachinko.bonus_balls}玉＞')
                    elif replay_choice == 'n':
                        print('遊技を終了します。')
                        income = Store.cashing(self)  # cashing_out() >>> 戻り値:income(=ball*4)
                        Store.revenue(self, income)
                        print('お疲れ様でした。Enterキーを押すとメニュー画面に戻ります。。')
                        Pachinko.replay = 0  # 再プレイを０に戻す。
                        break
                Pachinko.user_action('firing')  # ユーザー：Enterキーを押すと玉が発射されます。
                # 遊技開始
                while (self.ball > 0) or (Pachinko.replay_balls > 0):
                    if (Pachinko.replay == 0) or (Pachinko.replay_balls > 0):
                        navel = Store.ball_goes_in()  # 戻り値{None:消化、n:ヘソ入賞}
                        # 玉の入賞判定 (通常時7%で入賞) None:ヘソ入賞なし、int型:ヘソ入賞 -> 抽選
                        if navel is None:
                            if Pachinko.replay == 0:
                                self.ball -= 1  # 持ち玉が減る
                                continue
                            # 持ち玉遊技の場合
                            else:
                                Pachinko.replay_balls -= 1  # 持ち玉が減る
                                continue
                        # 大当りの抽選判定
                        else:
                            Pachinko.count_eva += 1 # 回転数
                            jackpot = e_lottery()  # 戻り値{None:ハズレ、int型:当たり+確変、float型:当たり+チャンスタイム}
                            if jackpot is None:
                                continue
                            # チャンスタイム(100回転)
                            elif type(jackpot) is float:
                                chance_time = 100
                                Pachinko.bonus_balls += int(jackpot)  # 大当り純増出玉(確変突入時の遊技で使用＝減少していく）
                                Pachinko.bonus_pt += jackpot  # 大当りでの獲得出玉
                                Pachinko.total_bonus_count += 1  # 大当り回数をカウント
                                Pachinko.small_bonus_count += 1  # ボーナス内訳をカウント
                                print(f'{Pachinko.count_eva}回転目で小当りを引きました。{chance_time}回転の<チャンスタイム>に突入します。')
                                print('チャンスタイム中に大当りを引くと確率変動に突入します。')
                                Pachinko.user_action('firing')  # ユーザー：Enterキーを押すと玉が発射されます。
                                Pachinko.count_eva = 0  # 通常時の回転数を初期化
                                # チャンスタイム（入賞90%、抽選1/170)
                                while Pachinko.count_b <= 100:
                                    navel = Store.ball_goes_in_bonus()  # 戻り値{None:消化、n:ヘソ入賞}
                                    # 玉の入賞判定 (通常時7%で入賞) None:ヘソ入賞なし、int型:ヘソ入賞 -> 抽選
                                    if navel is None:
                                        Pachinko.bonus_balls -= 1  # 持ち玉が減る
                                        continue
                                    else:
                                        Pachinko.count_b += 1  # ボーナス時の回転数をカウント
                                        jackpot_c = e_lottery_chance()
                                        if jackpot_c is None:
                                            continue
                                        else:
                                            print(f'チャンスタイム{Pachinko.count_b}回転目で大当りを引きました。おめでとうございます。')
                                            Pachinko.user_action('bonus_start')
                                            Pachinko.count_b = 0
                                            # loopを抜けて確変に行くための変数
                                            navel = 7
                                            jackpot = 1500  # 確変(loop外のelse文で持ち玉に加算する）
                                            break

                                # チャンスタイム終了
                                if Pachinko.count_b != 0:
                                    input(f'\nチャンスタイム{chance_time}回中に大当りを引けませんでした。<通常>に戻ります。Enterを押してください。')
                                    Pachinko.bonus_balls += self.ball  # 獲得出玉に小当たり前の持ち玉を足す
                                    self.ball = 0
                                    Pachinko.result(self)  # 結果表示
                                    Pachinko.total_bonus_count = 1  # 大当り回数を初期化
                                    Pachinko.small_bonus_count = 0  # ボーナス内訳を初期化
                                    Pachinko.count_b = 0  # 大当り時の回転数を初期化
                                    Pachinko.replay += 1
                                    break
                            # 確率変動
                            else:
                                bonus_time = 170
                                Pachinko.count_eva = 0  # 通常時の回転数を初期化
                                Pachinko.bonus_balls += int(jackpot)  # 大当り純増出玉(確変突入時の遊技で使用＝減少していく）
                                Pachinko.bonus_pt += jackpot  # 大当りでの獲得出玉
                                Pachinko.total_bonus_count += 1  # 大当り回数をカウント
                                # 大当り内訳をカウント（初回）
                                if jackpot == 1500:
                                    Pachinko.big_bonus_count += 1
                                elif jackpot == 300:
                                    Pachinko.small_bonus_count += 1
                                Pachinko.user_action('bonus_start')
                                print(f'\n*確率変動*: {Pachinko.total_bonus_count}回目')
                                Pachinko.user_action('firing')  # ユーザー：Enterキーを押すと玉が発射されます。
                                while Pachinko.count_b <= 170:
                                    n = Store.ball_goes_in_bonus()  # 戻り値{n:ヘソ入賞、None:消化}
                                    # ヘソ入賞判定
                                    if n is None:
                                        Pachinko.bonus_balls -= 1  # 持ち玉が減る
                                        continue
                                    else:
                                        Pachinko.count_b += 1  # 回転数
                                        jackpot_b = e_lottery_bonus()  # lottery_bonus() 抽選
                                        # 大当りor転落の抽選判定  None:ハズレ、int型:大当り
                                        if jackpot_b is None:
                                            continue
                                        else:
                                            Pachinko.bonus_balls += jackpot_b  # 大当り純増出玉
                                            Pachinko.bonus_pt += jackpot_b  # 大当り獲得出玉
                                            Pachinko.total_bonus_count += 1
                                            Pachinko.big_bonus_count += 1
                                            Store.bonus_info(self, jackpot_b)  # 情報表示
                                            print()
                                            print(f'*確率変動*: {Pachinko.total_bonus_count}回目')
                                            Pachinko.bonus_list.append(jackpot_b)
                                            Pachinko.count_b = 0  # 大当り時の回転数を初期化
                                            input('キーを押すと玉が発射されます。')
                                            continue
                                # 確率変動終了
                                print(f'\n確率変動{bonus_time}回転中に大当りを引く事ができませんでした。')
                                Pachinko.user_action('bonus_end')  # ユーザー：Enter
                                if Pachinko.replay == 0:
                                    Pachinko.bonus_balls += self.ball  # 大当り前の持ち玉を獲得出玉に合算
                                    self.ball = 0  # 持ち玉を初期化
                                else:
                                    Pachinko.bonus_balls += Pachinko.replay_balls  # 大当り前の持ち玉を獲得出玉に合算
                                    Pachinko.replay_balls = 0  # 持ち玉を初期化
                                Pachinko.before_bonus_balls = Pachinko.bonus_balls  # 再プレイで使用した玉数を計算する時に使用
                                Store.result(self)
                                Pachinko.after_bonus(self)  # 確変終了後の初期化
                                Pachinko.replay += 1
                                break
                    # ボーナス終了後ループから抜ける
                    else:
                        break
                # ボーナス０回(bonus_balls=0)
                if Pachinko.replay == 0:
                    print('持ち玉が無くなりました。', end=' ')
                    Store.num_of_rotations(Pachinko.count_eva)
                elif (Pachinko.replay_balls == 0) and (Pachinko.before_bonus_balls != Pachinko.bonus_balls):
                    print('玉が無くなりました。', end=' ')
                    Store.num_of_rotations(Pachinko.count_eva)
                    if Pachinko.bonus_balls == 0:
                        choice = Pachinko.user_action('replay_again')  # ユーザー：持ち玉を使い切りました。現金を使って遊技を継続しますか。(y/n)
                        if choice == 'y':
                            Pachinko.replay = 0  # 持ち玉を使い切った場合は０に戻す
                            return Pachinko.eva(self)
                        else:
                            input('メニュー画面に戻ります。Enterキーを押してください。')
                            break
                # ボーナスが終了
                elif Pachinko.replay > 0:
                    choice = Pachinko.user_action('replay_choice')  # ユーザー：獲得出玉で遊技を続けますか？ (y/n):
                    # 遊技継続の場合は再度自身の関数を呼ぶ
                    if choice == 'y':
                        return Pachinko.eva(self)  # 再プレイなら自身の関数を呼ぶ
                    else:
                        print('遊技を終了します。')
                        income = Store.cashing(self)  # 戻り値:income(=ball*4)
                        Store.revenue(self, income)
                        Pachinko.replay = 0  # 再プレイを初期化。
                        Pachinko.count_eva = 0  # 回転数を初期化
                        Pachinko.user_action('finished')  # ユーザー：Enter
                        break

        if self.money == 0:
            print('\nお金が無くなりました。退店したい場合は ”*” を入力してください。')
            print('それ以外のキーを入力するとメニュー画面に戻ります。メニュー画面からお金の追加を行うことができます。')
            exiting = Pachinko.user_action('user_choice')  # ユーザー：退店orメニュー画面選択
            if exiting == '*':
                print('またのご来店をお待ちしております。')
                self.investment_amount = 0  # 投資額の初期化
                Pachinko.count_eva = 0
                return exiting
# ==================================================================================================
# CR魔法少女まどかマギカ:
# (通常時の大当り確率): 1/199, (初当たり出玉): +450(90%) or +1500(10%),
# (初当たり振り分け): 確率変動:50%, 通常:50%, (確率変動時の大当り確率): 1/70 回転数:70回転, (確率変動<上位>時の確率): 1/60: 回転数:120回転,
# (確率変動時の出玉振り分け): ALL+1500,

    def madomagi(self, ball=0):
        print('-'*20)
        print('CR魔法少女まどかマギカで遊びます。')
        # 遊技準備
        while (self.money >= 500) or (Pachinko.bonus_balls > 0):
            # 再プレイではない場合(持ち玉遊技ではない場合)
            if Pachinko.bonus_balls == 0:
                ball = Store.lend(self)  # lend() >>> self.ball += 125
            # lend()で玉への変換を拒否した場合
            if ball is None:
                input('遊技を終了します。Enterキーを押すとメニュー画面に戻ります。')
                break
            else:
                if Pachinko.bonus_balls == 0:
                    print('交換完了：[現金:500円 ＞＞＞ 持ち玉:125玉]')
                # 再プレイ（持ち玉遊技）
                else:
                    re = 125  # 持ち玉遊技(=125玉)
                    replay_choice = Pachinko.user_action('replay')  # ユーザー：持ち玉を使用して遊技を行いますか？(y/n)
                    if replay_choice == 'y':
                        before = Pachinko.bonus_balls
                        # 持ち玉＜125玉であれば、持ち玉全てを遊技用に払い出す
                        if Pachinko.bonus_balls < re:
                            Pachinko.replay_balls = Pachinko.bonus_balls
                            print(f'{Pachinko.replay_balls}玉を払い出します。　[持ち玉:{Pachinko.bonus_balls}玉 >>> 0玉]')
                            Pachinko.bonus_balls = 0
                        else:
                            Pachinko.bonus_balls -= re  # 持ち玉から125玉引く
                            Pachinko.replay_balls += re  # 遊技玉に125玉追加する
                            print(f'{re}玉を払い出します。　＜持ち玉:{before}玉 >>> {Pachinko.bonus_balls}玉＞')
                    elif replay_choice == 'n':
                        print('遊技を終了します。')
                        income = Store.cashing(self)  # cashing_out() >>> 戻り値:income(=ball*4)
                        Store.revenue(self, income)
                        Pachinko.user_action('finished')
                        Pachinko.replay = 0  # 再プレイを０に戻す。
                        break
                Pachinko.user_action('firing')  # ユーザー：Enterキーを押すと玉が発射されます。
                # 遊技
                while (self.ball > 0) or (Pachinko.replay_balls > 0):
                    if (Pachinko.replay == 0) or (Pachinko.replay_balls > 0):
                        navel = Store.ball_goes_in()  # 戻り値{None:消化、n:ヘソ入賞}
                        # 玉の入賞判定 (通常時7%で入賞) None:ヘソ入賞なし、int型:ヘソ入賞 -> 抽選
                        if navel is None:
                            if Pachinko.replay == 0:
                                self.ball -= 1  # 持ち玉が減る
                                continue
                            # 持ち玉遊技の場合
                            else:
                                Pachinko.replay_balls -= 1  # 持ち玉が減る
                                continue
                        # 大当りの抽選判定
                        else:
                            Pachinko.count_madoka += 1 # 回転数
                            jackpot = m_lottery()  # 戻り値{None:ハズレ、int型:当たり+確変、float型:当たり+通常}
                            if jackpot is None:
                                continue
                            # bonus(+450玉) >>> 通常
                            elif type(jackpot) is float:
                                Pachinko.bonus_balls += int(jackpot)  # 大当り純増出玉(確変突入時の遊技で使用＝減少していく）
                                Pachinko.bonus_pt += jackpot  # 大当りでの獲得出玉
                                Pachinko.total_bonus_count += 1  # 大当り回数をカウント
                                Pachinko.small_bonus_count += 1  # ボーナス内訳をカウント
                                Pachinko.count_madoka = 0  # 通常時の回転数を初期化
                                Pachinko.bonus_balls += self.ball  # 獲得出玉に小当たり前の持ち玉を足す
                                self.ball = 0
                                Pachinko.bonus_balls = int(Pachinko.bonus_balls)  # 結果をfloatで表示しないため
                                Pachinko.result(self)  # 結果表示
                                Pachinko.total_bonus_count = 0  # 大当り回数を初期化
                                Pachinko.small_bonus_count = 0  # ボーナス内訳を初期化
                                Pachinko.count_madoka = 0  # 通常時の回転数を初期化
                                Pachinko.count_b = 0  # 大当り時の回転数を初期化
                                Pachinko.bonus_pt = 0  # 大当りでの獲得出玉を初期化
                                Pachinko.before_bonus_balls = Pachinko.bonus_balls  # 再プレイ（持ち玉遊技）の判定で使用
                                Pachinko.replay += 1

                                break
                            # 確率変動
                            else:
                                bonus_time = 80
                                Pachinko.count_madoka = 0  # 通常時の回転数を初期化
                                Pachinko.bonus_balls += jackpot  # 大当り純増出玉(確変突入時の遊技で使用＝減少していく）
                                Pachinko.bonus_pt += jackpot  # 大当りでの獲得出玉
                                Pachinko.total_bonus_count += 1  # 大当り回数をカウント
                                # ボーナス内訳をカウント
                                if jackpot == 1500:
                                    Pachinko.big_bonus_count += 1
                                elif jackpot == 450:
                                    Pachinko.small_bonus_count += 1
                                Pachinko.user_action('bonus_start')
                                print(f'\n*確率変動*: {Pachinko.total_bonus_count}回目')
                                Pachinko.user_action('firing')  # ユーザー：Enterキーを押すと玉が発射されます。
                                while Pachinko.count_b <= 80:
                                    n = Store.ball_goes_in_bonus()  # 戻り値{n:ヘソ入賞、None:消化}
                                    # ヘソ入賞判定
                                    if n is None:
                                        Pachinko.bonus_balls -= 1  # 持ち玉が減る
                                        continue
                                    else:
                                        Pachinko.count_b += 1  # 回転数
                                        jackpot_b = m_lottery_bonus()  # lottery_bonus() 抽選
                                        # 大当りor転落の抽選判定  None:ハズレ、int型:大当り、float型:大当り+確変上位突入
                                        if jackpot_b is None:
                                            continue
                                        # 確変当たり
                                        elif type(jackpot_b) is int:
                                            Pachinko.bonus_balls += jackpot_b  # 大当り純増出玉
                                            Pachinko.bonus_pt += jackpot_b  # 大当り獲得出玉
                                            Pachinko.total_bonus_count += 1
                                            Pachinko.big_bonus_count += 1
                                            Store.bonus_info(self, jackpot_b)  # 情報表示
                                            print()
                                            print(f'*確率変動*: {Pachinko.total_bonus_count}回目')
                                            Pachinko.bonus_list.append(jackpot_b)
                                            Pachinko.count_b = 0  # 大当り時の回転数を初期化
                                            Pachinko.user_action('firing')
                                            continue
                                        # 確変当たり＋確率変動<上位>に突入
                                        elif type(jackpot_b) is float:
                                            bonus_time = 120
                                            Pachinko.bonus_balls += jackpot_b  # 大当り純増出玉(確変突入時の遊技で使用＝減少していく）
                                            Pachinko.bonus_pt += jackpot_b  # 大当りでの獲得出玉
                                            Pachinko.total_bonus_count += 1  # 大当り回数をカウント
                                            Pachinko.big_bonus_count += 1  # 大当り内訳をカウント
                                            big_bonus_plus_count = 0  # 大当り内訳（まどマギ上位用）
                                            Store.bonus_info(self, jackpot_b)  # 情報表示
                                            print()
                                            print('おめでとうございます。上位突入大当りを引いたので、確率変動<上位>に突入します。')
                                            print('確率：1/70 -> 1/60、　回転数：80回転　-> 120回転')
                                            input('<確率変動(上位)>に突入します。Enterキーを押すと玉が発射されます。')
                                            while Pachinko.count_b <= 120:
                                                n = Store.ball_goes_in_bonus()  # 戻り値{n:ヘソ入賞、None:消化}
                                                # ヘソ入賞判定
                                                if n is None:
                                                    Pachinko.bonus_balls -= 1  # 持ち玉が減る
                                                    continue
                                                else:
                                                    Pachinko.count_b += 1  # 回転数
                                                    jackpot_b_plus = m_lottery_bonus_plus()  # lottery_bonus() 抽選
                                                    # 大当りor転落の抽選判定  None:ハズレ、int型:大当り
                                                    if jackpot_b is None:
                                                        continue
                                                    elif type(jackpot_b_plus) is int:
                                                        Pachinko.bonus_balls += jackpot_b  # 大当り純増出玉
                                                        Pachinko.bonus_pt += jackpot_b  # 大当り獲得出玉
                                                        Pachinko.total_bonus_count += 1
                                                        big_bonus_plus_count += 1
                                                        Store.bonus_info(self, jackpot_b)  # 情報表示
                                                        print()
                                                        print(f'*確率変動<上位>*: {big_bonus_plus_count}回目')
                                                        Pachinko.bonus_list.append(jackpot_b_plus)
                                                        Pachinko.count_b = 0  # 大当り時の回転数を初期化
                                                        input('キーを押すと玉が発射されます。')
                                                        continue
                                            # 確変<上位>転落　>>> 通常
                                            print(f'\n確率変動<上位>{bonus_time}回転中に大当りを引く事ができませんでした。')
                                            Pachinko.user_action('bonus_end')  # ユーザー：Enter
                                            # 持ち玉を初期化
                                            if Pachinko.replay == 0:
                                                Pachinko.bonus_balls += self.ball  # 大当り前の持ち玉を獲得出玉に合算
                                                self.ball = 0
                                            else:
                                                Pachinko.bonus_balls += Pachinko.replay_balls  # 大当り前の持ち玉を獲得出玉に合算
                                                Pachinko.replay_balls = 0
                                            Pachinko.before_bonus_balls = Pachinko.bonus_balls  # 再プレイで使用した玉数を計算する時に使用
                                            Pachinko.bonus_balls = int(Pachinko.bonus_balls)  # 結果をfloatで表示しないため
                                            Store.result(self)
                                            Pachinko.after_bonus(self)  # 確変終了後の初期化
                                            Pachinko.replay += 1
                                            break
                                # 確変転落　>>> 転落
                                if Pachinko.replay == 0:
                                    bonus_time = 80
                                    print(f'\n確率変動{bonus_time}回転中に大当りを引く事ができませんでした。')
                                    Pachinko.user_action('bonus_end')  # ユーザー：Enter
                                    # 持ち玉を初期化
                                    if Pachinko.replay == 0:
                                        Pachinko.bonus_balls += self.ball  # 大当り前の持ち玉を獲得出玉に合算
                                        self.ball = 0
                                    else:
                                        Pachinko.bonus_balls += Pachinko.replay_balls  # 大当り前の持ち玉を獲得出玉に合算
                                        Pachinko.replay_balls = 0
                                    Pachinko.before_bonus_balls = Pachinko.bonus_balls  # 再プレイで使用した玉数を計算する時に使用
                                    Pachinko.bonus_balls = int(Pachinko.bonus_balls)  # 結果をfloatで表示しないため
                                    Store.result(self)
                                    Pachinko.after_bonus(self)  # 確変終了後の初期化
                                    Pachinko.replay += 1
                                    break
                # ボーナス０回(bonus_balls=0)
                if Pachinko.replay == 0:
                    print('持ち玉が無くなりました。', end=' ')
                    Store.num_of_rotations(Pachinko.count_madoka)
                elif (Pachinko.replay_balls == 0) and (Pachinko.before_bonus_balls != Pachinko.bonus_balls):
                    print('玉が無くなりました。', end=' ')
                    Store.num_of_rotations(Pachinko.count_madoka)
                    if Pachinko.bonus_balls == 0:
                        choice = Pachinko.user_action('replay_again')  # ユーザー：持ち玉を使い切りました。現金を使って遊技を継続しますか。(y/n)
                        if choice == 'y':
                            Pachinko.replay = 0  # 持ち玉を使い切った場合は０に戻す
                            return Pachinko.madomagi(self)
                        else:
                            input('メニュー画面に戻ります。Enterキーを押してください。')
                            break
                # ボーナスが終了
                elif Pachinko.replay > 0:
                    choice = Pachinko.user_action('replay_choice')  # ユーザー：獲得出玉で遊技を続けますか？ (y/n):
                    # 遊技継続の場合は再度自身の関数を呼ぶ
                    if choice == 'y':
                        return Pachinko.madomagi(self)  # 再プレイなら自身の関数を呼ぶ
                    else:
                        print('遊技を終了します。')
                        income = Store.cashing(self)  # 戻り値:income(=ball*4)
                        Store.revenue(self, income)
                        Pachinko.replay = 0  # 再プレイを初期化。
                        Pachinko.count_eva = 0  # 回転数を初期化
                        Pachinko.user_action('finished')  # ユーザー：Enter
                        break

        if self.money == 0:
            print('\nお金が無くなりました。退店したい場合は ”*” を入力してください。')
            print('それ以外のキーを入力するとメニュー画面に戻ります。メニュー画面からお金の追加を行うことができます。')
            exiting = Pachinko.user_action('user_choice')  # ユーザー：退店orメニュー画面選択
            if exiting == '*':
                print('またのご来店をお待ちしております。')
                self.investment_amount = 0  # 投資額の初期化
                Pachinko.count_eva = 0
                return exiting