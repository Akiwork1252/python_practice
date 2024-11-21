import time

def fibo_kame(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_1 + n_2
            n_2 = n_1
            n_1 = result
        return result


before = time.time()
for i in range(100):
    print(f'fibonacci-{i}: ',fibo_kame(i))
after = time.time()
total = after - before
print(total)