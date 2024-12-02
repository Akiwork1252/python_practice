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
            'CR北斗の拳': ['1/349', '+300 or +1500', '100%', '当たり:1/40, 転落:1/150', '+300(1/4) or +1500(3/4)'],
            'CRエヴァンゲリオン': ['1/319', '+450 or +1500', '70%', '1/90: 170回転', 'ALL+1500'],
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
                print('遊技を終了します。')
                break
            elif choice == 'y':
                self.money -= 500  # ユーザーの残金から５００円を引く
                self.ball += 125  # パチンコ玉１２５玉
                return self.money, self.ball
            else:
                print('入力が正しくありません。')