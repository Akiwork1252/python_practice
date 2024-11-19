def upper(n):
    def inner(m):
        return n ** m
    return inner


t = upper(3)
print(t(4))