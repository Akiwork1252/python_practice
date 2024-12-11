import csv
import datetime
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import re
import seaborn as sns
import pandas as pd


class InformationDisplay:
    # csvファイル作成(出玉推移グラフ用) カラム：回転数、出玉
    # 初期データ(回転数:0, 出玉:0)を入力
    @staticmethod
    def create_csvfile():
        with open('game_data/game_data.csv', mode='w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['num_of_rotations', 'balls'])
            writer.writerow([0, 0])

    # csvファイルに遊技データを追加
    @staticmethod
    def add_data_to_csvfile(count, balls):  # count:回転数、balls:玉数
        with open('game_data/game_data.csv', mode='a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([count, balls])

    # csvファイルからデータフレイム作成
    @staticmethod
    def create_dataframe():
        df = pd.read_csv('game_data/game_data.csv')
        return df

    # 遊技日を取得し、月と日にちを返す(ファイル名とグラフのタイトルに使用)
    @staticmethod
    def date():
        today = datetime.datetime.now()
        return today.month, today.day

    # ユーザーの名前が英字か調べる。
    # 英字であれば最初３文字を遊技データのファイル名に使用。英字でなければをanonymousを使用。
    @staticmethod
    def name_judge(username):
        pt = '^([A-Z]|[a-z]){3}'
        pattern = re.compile(pt)
        res = pattern.search(username)
        if res is not None:
            return username[:3]
        else:
            return 'anonymous'

    # ユーザー名と日付を受け取り、ファイル名を作成
    @staticmethod
    def make_filename(username, month, day):
        date_in_filename = f'{month}{day}'
        file_name = f'{username}_{date_in_filename}.png'
        return file_name

    # 遊技台とユーザー名と日付を受け取り、タイトル用の文字列を作成
    @staticmethod
    def make_title_name(machine, username, month, day):
        graph_title = f'{machine}(user:{username},  date:{month}/{day})'
        return graph_title

    # グラフ作成、表示、グラフの保存(png)
    @staticmethod
    def view_graph(df, title, filename):  # title:遊技台
        # カラム指定
        col_nums = 'num_of_rotations'
        col_balls = 'balls'
        x = df[col_nums]
        y = df[col_balls]
        # グラフの表示
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o')
        ax.set_title(title)
        ax.set_xlabel('回転数')
        ax.set_ylabel('玉数')
        # グラフを保存
        fig.savefig(f'game_data/{filename}')
        # グラフを５秒表示
        while True:
            action = input('Enterキーを押すとグラフが表示されます。グラフは１０秒間表示された後、自動で閉じます。')
            if type(action) is str:
                break
        plt.pause(10)
        plt.close(fig)

    # 統計データ計算、表示
    @staticmethod
    def statistics():
        pass


if __name__ == '__main__':
    InformationDisplay.create_csvfile()
    InformationDisplay.add_data_to_csvfile(173, -5000)
    InformationDisplay.add_data_to_csvfile(252, -3500)
    InformationDisplay.add_data_to_csvfile(276, -7000)
    InformationDisplay.add_data_to_csvfile(281, 500)
    InformationDisplay.add_data_to_csvfile(301, -2000)
    InformationDisplay.add_data_to_csvfile(350, -1500)
    InformationDisplay.add_data_to_csvfile(371, -1000)
    InformationDisplay.add_data_to_csvfile(390, 500)
    InformationDisplay.add_data_to_csvfile(467, 3000)
    InformationDisplay.add_data_to_csvfile(497, 4500)
    InformationDisplay.add_data_to_csvfile(517, 9000)

    df = InformationDisplay.create_dataframe()
    month, day = InformationDisplay.date()
    name = InformationDisplay.name_judge('akinori')
    machine = 'CRエヴァンゲリオン'
    title = InformationDisplay.make_title_name(machine, name, month, day)
    filename = InformationDisplay.make_filename(name, month, day)
    InformationDisplay.view_graph(df, title, filename)