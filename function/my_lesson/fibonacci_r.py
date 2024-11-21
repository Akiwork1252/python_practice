def fibonacci(n):
    if n < 2:
        print(n, end=' ')
        return n
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)


print(f'\nAnswer:{fibonacci(6)}')