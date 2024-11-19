def add_number(func):
    def wrapper(x):
        num = [2, 3, 4, 5, 6, 7, 8, 9]
        for i in num:
            func(i)
    return wrapper


@add_number
def power(n):
    result = n ** 2
    print(f'{n}の2乗は{result}')
    return result


power(1)