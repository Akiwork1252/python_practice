def even(start):
    while start >= 2:
        if start % 2 == 0:
            yield start
        start -= 1


print(even(19))
for i in even(19):
    print(i)


