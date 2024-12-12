import sqlite3


class DB:
    # テーブル作成(初回のみ）
    @staticmethod
    def create_table():
        # <pachinko.db>
        # userテーブル(名前、年齢、所持金)
        # historyテーブル(日付、名前、年齢、遊技台、収支(文字列のためsort不可))
        db_instruction = '''
        CREATE TABLE IF NOT EXISTS history(date CHAR(20), name CHAR(20), age INT, machine CHAR(20), income CHAR(10))
        '''
        con = sqlite3.connect('pachinko.db')
        cursor = con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS user(name CHAR(20), age INT, money INT)')
        cursor.execute(db_instruction)
        con.commit()

    # テーブル削除（プログラムの試行でデータが増えた時に使用）
    @staticmethod
    def del_table():
        con = sqlite3.connect('pachinko.db')
        cursor = con.cursor()
        cursor.execute('DROP TABLE user')
        cursor.execute('DROP TABLE history')
        con.commit()

    # 来店時　ユーザー情報を確認、履歴が無ければデータベースに作成
    @staticmethod
    def user_search_and_add(name, age):
        min_age = 20
        count = 0
        money = 0
        con = sqlite3.connect('pachinko.db')  # userTABLE(name, age, money)
        cursor = con.cursor()
        itr = cursor.execute('SELECT * FROM user WHERE (name=(?)) and (age=(?))', [name, age])
        for row in itr:
            name, age, money = row
            count += 1
        # WHEREでデータがヒットしない
        if count == 0:
            if age >= min_age:
                print('初めてのご来店ですね。所持金を入力してください。')
            else:
                pass
            while True:
                try:
                    money = int(input('所持金: '))
                    cursor.execute('INSERT INTO user VALUES(?, ?, ?)', [name, age, money])
                    con.commit()
                except ValueError:
                    print('半角英数字で入力してください。(例:5000)')
                else:
                    break
            return name, age, money
        else:
            if age < min_age:  # データはヒットしたが前回入店できていない
                print('来店できません。')
            else:
                while True:
                    user = input(f'来店履歴が確認できました。前回の所持金{money}円を使用して遊技ができます。Enterキーを押してください。')
                    if type(user) is str:
                        break
            return money

    # ユーザーの遊技履歴を表示する
    @staticmethod
    def check_history(name, age):
        count = 0
        con = sqlite3.connect('pachinko.db')
        cursor = con.cursor()
        itr = cursor.execute('SELECT * FROM history WHERE (name == (?)) and (age == (?))', [name, age])
        for user in itr:
            count += 1
            print(user)
        if count == 0:
            print('遊技履歴が存在しませんでした。')
        con.commit()

    # 遊技終了後のデータをテーブル(history)に追加する　history{日付、名前、年齢、遊技台、収支}
    @staticmethod
    def save_when_exit(date, name, age, machine, income):
        con = sqlite3.connect('pachinko.db')
        cursor = con.cursor()
        cursor.execute('INSERT INTO history VALUES(?, ?, ?, ?, ?)', [date, name, age, machine, income])
        con.commit()

    # 退店時にテーブル(user)の所持金を更新する user(名前、年齢、所持金)
    @staticmethod
    def updating_money(name, age, money, check):
        con = sqlite3.connect('pachinko.db')
        cursor = con.cursor()
        if check != 0:  # 遊技確認
            cursor.execute('UPDATE user SET money = (?) WHERE (name == (?)) and (age == (?))', [money, name, age])
            print('所持金の更新を行いました。次回来店時にご利用できます。')
            while True:
                action = input('Enterキーを押してください。')
                if type(action) is str:
                    break
        con.commit()

    # データベースの確認（管理者用）パスワード必要にする
    @staticmethod
    def check_db(n):  # 引数n:操作メニュー >>> 1:ユーザー情報、 2:遊技履歴
        con = sqlite3.connect('pachinko.db')
        cursor = con.cursor()
        instruction_1 = 'SELECT * FROM user'
        instruction_2 = 'SELECT * FROM history'
        count = 1
        if n == 1:
            itr = cursor.execute(instruction_1)  # user(名前、年齢、所持金)
            for row in itr:
                name, age, money = row
                print(f'ユーザー[{count}]', end=' ')
                print(f'>>> (名前){name}、(年齢){age}、(所持金){money}')
                count += 1
        elif n == 2:
            itr = cursor.execute(instruction_2)  # history{日付、名前、年齢、遊技台、収支}
            for row in itr:
                date, name, age, model, income = row
                print(f'(日付){date}、(名前){name}、(年齢){age}、(遊技台){model}、(収支){income}')
        else:
            print('入力が正しくありません。')
        con.close()

# DB.del_table()
