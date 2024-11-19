# 与えられた引数の二乗を返す関数に機能を追加する

def power_two(func):
    def wrapper(x):
        x_two = x**2
        return func(x_two)
    return wrapper


def add_list(func):
    def wrapper(x):
        power_list = [2, 3, 4]
        ans = []
        for i in power_list:
            p = x**i
            ans.append(p)
        return ans
    return wrapper


# @power_two
@add_list
def power(n):
    print(n**2)


n = int(input('Enter the number: '))
power(n)
