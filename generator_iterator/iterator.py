nums = [1, 2, 3, 4]

print(type(nums))
it_nums = iter(nums)
print(type(it_nums))
print(next(it_nums))
print('*'*20)
print(id(nums))
print(id(it_nums))
print(id(iter(it_nums)))

for i in it_nums:
    print(i)