def greeting(func):
    def inner(*args, **kwargs):
        print('こんにちは')
        func(*args, **kwargs)
        print('よろしくお願いします')
    return inner


@greeting
def say_name(name):
    print(f'私の名前は{name}です。')


@greeting
def say_name_and_origin(name, origin):
    print(f"I'm {name}. I'm from {origin}")


# say_name = greeting(say_name)
# print(say_name)
# say_name('aki')
say_name('aki')
print('*'*30)
say_name_and_origin('aki', 'Tokyo')
print('*'*30)





