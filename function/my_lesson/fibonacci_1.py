import time

def fibo(n):
    n_1 = 1
    n_2 = 0
    if n == 0:
        return 0
    for _ in range(n):
        if n <= 2:
            return n_1 + n_2
        else:
            num = n_1
            n_1 += n_2
            n_2 = num
            n -= 1

before = time.time()
for i in range(100):
    print(f'fibonacci-{i}: ',fibo(i))
after = time.time()
total = after - before
print(total)