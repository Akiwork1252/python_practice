def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

power_two = power(2)
print(power_two(4))


# lambda
def power_l(exponent):
    return lambda base: base ** exponent


power_l = power_l(2)
print(power_l(4))
print('*'*20)

nums = [6, 33, 78, 92, 71, 3]
print(list(filter(lambda i: i % 2, nums)))