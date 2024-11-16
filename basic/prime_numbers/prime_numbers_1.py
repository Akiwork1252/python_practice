import time

num = int(input('数字を入力してください'))
i = 2

before = time.time()
while True:
    if num == i:
        print(f'{num}は素数です')
        break
    elif num % i == 0:
        print(f'{num}は素数ではありません')
        break
    i += 1
after = time.time()
total_time = after - before

print('*'*30)
print(f'計算にかかった時間：{total_time}')
