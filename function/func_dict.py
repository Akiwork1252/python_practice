def add(fruits):
    print(f'変更前のリスト： {fruits}')
    add = input('追加するフルーツを選択してください')
    if add in fruits:
        print(f'{add}はすでにリストに存在します')
    else:
        fruits.append(add)
        print(f'変更後のリスト： {fruits}')


def change(fruits):
    print(f'変更前のリスト： {fruits}')
    idx = int(input('変更するフルーツの格納場所を選択してください'))
    if 0 <= idx < len(fruits):
        print(f'{fruits[idx]}を別のフルーツに変更します')
        change_fruit = input('新しいフルーツを選択してください')
        fruits[idx] = change_fruit
        print(f'変更後のリスト： {fruits}')
    else:
        print(f'インデックス：{idx}は存在しません')


def delete(fruits):
    print(f'変更前のリスト： {fruits}')
    del_fruit = input('削除するフルーを選択してください')
    if del_fruit in fruits:
        print(f'{del_fruit}を削除します。')
        fruits.remove(del_fruit)
        print(f'変更後のリスト： {fruits}')
    else:
        print(f'{del_fruit}はリスト{fruits}に存在しません。')


fruits_list = ['apple', 'banana', 'lemon']
func_dict = {1: add, 2: change, 3: delete, 0: '終了'}
while True:
    print('メニューから関数を選択してください')
    for k, v in func_dict.items():
        print(f'{k}: {v}')
    choice = int(input(': '))

    if choice == 0:
        print('操作を終了します')
        break
    elif choice in func_dict:
        func_dict[choice](fruits_list)
    else:
        print('メニューから選択してください')
    print()
