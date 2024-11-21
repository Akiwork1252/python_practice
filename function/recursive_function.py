# recursive function

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))
print('*'*20)

# recursive_function
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(f'再帰{fibonacci(6)}')
print('*'*20)

# 再帰なし
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



print(f'あき{fibo(6)}')
print('*'*30)

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

print(f'かめ{fibo_kame(5)}')