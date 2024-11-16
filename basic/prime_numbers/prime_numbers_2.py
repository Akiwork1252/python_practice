import time

num = int(input(f'好きな数字を入力してください'))
division_list = []

before = time.time()
for i in range(1, num+1):
    if num % i == 0:
        division_list.append(i)
    i += 1

if len(division_list) == 2:
    print(f'{num}は素数です')
    print(f'割り切れる数字：{division_list}')
else:
    print(f'{num}は素数ではありません')
    print(f'割り切れる数字：{division_list}')
after = time.time()
total = after - before
print('*'*30)
print(f'探索にかかった時間：{total}')
