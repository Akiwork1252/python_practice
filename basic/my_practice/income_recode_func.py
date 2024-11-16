def user_month():
    print('月々の収入を記録できます。記録する月を半角英数字で入力してください。')
    while True:  # 正しい値が入力されるまで繰り返す
        first_month = int(input('何月から＞＞＞＞'))
        last_month = int(input('何月まで＞＞＞＞'))
        if 0 < first_month < 13 and 0 < last_month < 13:  # 入力値が１〜１２であることを確認する
            if first_month < last_month:  # 開始月　＜　停止月
                months = last_month - first_month + 1
                print(f'{first_month}月から{last_month}月までの{months}ヶ月間の収入を記録します。')
                break
            else:
                months = (13-first_month) + last_month
                print(f'{first_month}月から翌年{last_month}月までの{months}ヶ月間の収入を記録します。')
                break
        else:
            print('入力された値が正しくありません')
    return first_month, last_month, months


# データをdictionaryで保存する
def data_dict(f_month=1, l_month=12, period=12): # 開始月、停止月、期間を引数として受け取る
    print('データは全て半角英数字で入力してください。')
    month_dict = {}
    f = f_month
    l = l_month
    p = period

    for _ in range(period):  # 期間分繰り返す
        if f_month == 13:  # 12月まで行ったら1月に戻る
            f_month = 1
            print('***翌年***')
            month = int(input(f'{f_month}月＞＞＞〇〇万円：'))
            month_dict[f'{f_month}月'] = f'{month}万円'
            f_month += 1
        else:
            month = int(input(f'{f_month}月＞＞＞〇〇万円：')) # valueErrorへの対策を検討
            month_dict[f'{f_month}月'] = f'{month}万円'
            f_month += 1
    print(f'{f}月〜{l}月までの{p}ヶ月間のデータを保存しました!!!!')
    display(month_dict)  # 保存データを表示する display(dictionary)
    return month_dict


# 現在の保持データを表示する
def display(user_dict):  # dictionaryを引数に受け取る
    print('\n現在保存しているデータです。')
    print('*'*30)
    print(user_dict)
    print('*'*30)
    print()


# 保存データの詳細を表示する
def _statistics(user_dict, f_month, l_month):
    # 最高月給、最低月給を出す
    max_month, max_amount = max(user_dict.items(), key=lambda x:x[1])
    min_month, min_amount = min(user_dict.items(), key=lambda x:x[1])
    # 平均月給を求める
    total = 0
    for d in user_dict.items():
        num = d[1].split('万')
        total += int(num[0])
    average = total / len(user_dict)

    print('*'*30)
    print(f'''{f_month}月〜{l_month}月\n
          最高月給:{max_month}の{max_amount}
          最低月給:{min_month}の{min_amount}
          平均月給:{average}万円です''')
    print('*'*30)


# Userが確認したいデータを確認する
def check_menu(month_dict, f_month, l_month):
    menu2 = """
    ・全てのデータを確認する　＞＞＞　a(all)
    ・個別のデータを確認する　＞＞＞　c(choice)
    ・統計データを表示する　　＞＞＞　s(statistics)
    """
    # 確認するデータの確認
    print('下記より実行したいメニューを選択してください。')
    print(menu2)
    user_choice = input('user :')
    # 全てのデータを確認する
    if user_choice == 'all' or user_choice == 'a':
        display(month_dict)
    # 指定した月のデータのみ確認する
    elif user_choice == 'choice' or user_choice == 'c':
        _check_data(month_dict)
    elif user_choice == 'statistics' or user_choice == 's':
        _statistics(month_dict, f_month, l_month)
    # 入力ミス
    else:
        print('入力が正しくありません。')


# 指定した月のデータ確認
def _check_data(month_dict):
    print('確認したい月を半角英数字で入力してください。')
    choice_month = int(input('〇〇月　＞＞＞:'))
    month = f'{choice_month}月'

    # 入力された月のデータが存在するかを判定する
    if month in month_dict:
        print(f'{choice_month}月の収入は{month_dict[month]}です。\n')
    else:
        print(f'{month}のデータは存在しません。')
        print('データを追加したい場合は、＜操作メニュー＞から”データの追加”を選択してください。\n')


# 既存データの変更を行う
def data_fixes(month_dict):
    while True:  # 正しい値が入力されるまで繰り返す
        print('修正したい月を半角英数字で入力してください。前のメニューに戻りたい場合は"0"を入力してください')
        choice_month = int(input('〇〇月　＞＞＞:'))
        # 入力が1月〜12月であるか判定する
        if 1 <= choice_month < 13:
            month = f'{choice_month}月'
            # 入力された月のデータが保存されているか判定する
            if month in month_dict:
                r_amount = int(input('新たな値を半角英数字で入力してください。〇〇万円　＞＞＞'))
                month_dict[month] = f'{r_amount}万円'
                print(f'\n＞＞＞＞{month}の収入を{r_amount}万円に変更しました。')
                display(month_dict)
                break
            else:
                print(f'{month}のデータは存在しません。')
                print('データを追加したい場合は、＜操作メニュー＞から”データの追加”を選択してください。\n')
        # 前画面に戻りたい場合
        elif choice_month == 0:
            break
        else:
            print('入力された値が正しくありません')
    return month_dict


# データの追加を行う
def add_data(month_dict):
    # 追加の操作を繰り返す。
    while True:
        print('追加したい月を半角英数字で入力してください。')
        choice_month = int(input('〇〇月　＞＞＞:'))
        add_month = f'{choice_month}月'
        # 入力された月のデータが存在するか判定する
        if add_month in month_dict:
            print(f'{add_month}のデータはすでに存在します。')
            print('データを変更したい場合は、＜操作メニュー＞から”データの変更”を選択してください。\n')
            break
        else:
            add_amount = int(input('〇〇万円　＞＞＞'))
            month_dict[f'{add_month}'] = f'{add_amount}万円'
            y_n = input('操作を繰り返しますか。(y/n)')

            # 操作を繰り返すか判定する
            if y_n == 'y':
                continue
            else:
                print('データを追加しました。')
                display(month_dict)
                print('操作を終了します。')
                break
    return month_dict,

