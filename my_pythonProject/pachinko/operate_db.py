import sqlite3


class DB:
    # テーブル作成(初回のみ）
    @staticmethod
    def create_table():
        # <pachinko.db>
        # userテーブル(名前、年齢、所持金)
        # historyテーブル(日付、名前、年齢、遊技台、収支)
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
        count = 0
        con = sqlite3.connect('pachinko.db')  # userTABLE(name, age, money)
        cursor = con.cursor()
        itr = cursor.execute('SELECT * FROM user WHERE (name=(?)) and (age=(?))', [name, age])
        for i in itr:
            count += 1
        # WHEREでデータがヒットしない
        if count == 0:
            print('初めてのご来店ですね。所持金を入力してください。')
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
            while True:
                user = input(f'来店履歴が確認できました。前回の所持金{i[2]}円を使用して遊技ができます。Enterキーを押してください。')
                if type(user) is str:
                    break
            return i[2]

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

    # 遊技終了後のデータをテーブル(history)に追加する　{日付、名前、年齢、遊技台、収支}
    @staticmethod
    def save_when_exit(date, name, age, machine, income):
        con = sqlite3.connect('pachinko.db')
        cursor = con.cursor()
        cursor.execute('INSERT INTO history VALUES(?, ?, ?, ?, ?)', [date, name, age, machine, income])
        con.commit()


# DB.del_table()
