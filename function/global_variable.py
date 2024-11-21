call_count = 0  # CALL_COUNT = 0 (constant variable) 後で書き換えられたくない


def print_count():
    global call_count
    call_count += 1
    print(f'funk1: {call_count}')


def print_count2():
    global call_count
    call_count += 1
    print((f'func2: {call_count}'))


def print_count3():
    call_count = 0
    call_count += 1
    print((f'func3: {call_count}'))



print_count()
print_count2()
print_count()
print_count3()
print(call_count)