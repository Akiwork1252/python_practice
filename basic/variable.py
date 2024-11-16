import random

# h(文字列の数)、w(文字列の長さ)
h, w = map(int, input('Enter the number').split())
s_list = []
count = 0

# wの長さの文字列をh個作成する
for i in range(h):
    s = ''
    for j in range(w):
        x = random.randint(0, 1)
        if x == 0:
            s += '*'
        else:
            s += '-'
    s_list.append(s)

# 変数を動的に作成
val_list = []
for i in s_list:
    exec(f"s_{count} = '{i}'")
    count += 1
