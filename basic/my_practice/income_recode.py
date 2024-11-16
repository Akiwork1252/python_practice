from income_recode_func import user_month, data_dict, display, check_menu, data_fixes, add_data

# データを記録する期間を確認する user_month() => 開始月、停止月、期間を返す
f_month, l_month, period = user_month()
# データをdictionaryで保存する　data_dict() => dictionaryを返す
month_dict = data_dict(f_month, l_month, period)

menu = """
・データの再確認　＞＞＞　r 
・データの変更　＞＞＞　c
・データの追加　＞＞＞　a
"""
# 操作を繰り返す
while True:
    y_n = input('保存したデータの確認、変更または追加を行いますか (y/n)')
    # 再操作を行う
    if y_n == 'y':
        while True:
            print('\n**希望する操作を以下から選択して入力してください**')
            print('<操作メニュー>\n', menu)
            choice = input('user :')
            # データの再確認を行う
            if choice == 'r':
                check_menu(month_dict, f_month, l_month)
                break
            # データの変更を行う
            elif choice == 'c':
                month_dict = data_fixes(month_dict)
                break
            # データの追加を行う
            elif choice == 'a':
                new_data = add_data(month_dict)
                break
            # ユーザー入力ミス
            else:
                print('!入力が正しくありません。メニューから選択して下さい')
    # 操作を終了する
    elif y_n == 'n':
        print('ご利用ありがとうございました。')
        print('またのご利用をお待ちしております')
        break
    # ユーザー入力ミス
    else:
        print('入力が正しくありません。')