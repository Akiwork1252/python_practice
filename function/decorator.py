def greeting(func):
    def wrapper(x):
        print('こんにちは')
        func(x)
        print('よろしくお願いします')
    return wrapper

@greeting
def self_introduction(name):
    print(f'私の名前は{name}です。')


name = input('あなたの名前はなんですか')
self_introduction(name)
greeting(self_introduction)
