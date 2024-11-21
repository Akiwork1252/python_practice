def func(n):
    return n * n

f = func
print(f(2))

func_list = [1, 2, func]
print(func_list[2](2))


def execute_func(func, param):
    return func(param)


print(execute_func(func, 2))


def return_func():
    def inner_func():
        print('This is an inner func')
    return inner_func

f = return_func()
print(f)
f()

print('*'*20)
# 状態が静的
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

power_two = power(2)
print(power)
print(power(2))
print(power_two) # inner_powerオブジェクト
print(power_two(3))

print('*'*30)
# 状態が動的
def average():
    nums = []
    def inner_average(num):
        nums.append(num)
        print(nums)
        return sum(nums) / len(nums)
    return inner_average

average_nums = average()
print(average_nums)
print(average_nums(2))
print(average_nums(4))
print(average_nums(6))