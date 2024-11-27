def return_nums(n):
    division_list = []
    for i in range(1, n+1):
        if n % i == 0:
            division_list.append(i)
    if len(division_list) == 2:
        return n


# print(return_nums(4002))


def add_primenums_list(n):
    prime_nums = []
    for i in range(1, n + 1):
        x = return_nums(i)
        if x is None:
            continue
        else:
            prime_nums.append(x)
    return prime_nums


# x = add_primenums_list(4001)
# print(x)

num = int(input('数字を入力してください'))

prime_numbers_list = add_primenums_list(num)

def mygenerator(prime_number_list):
    idx_count = 0
    while idx_count <= len(prime_numbers_list):
        yield prime_numbers_list[idx_count]
        idx_count += 1


print(next(mygenerator(13)))
print(next(mygenerator(13)))
print(next(mygenerator(13)))
print(next(mygenerator(13)))





