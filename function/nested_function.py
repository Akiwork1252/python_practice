msg = 'I am global'

def outer():
    msg = 'I am outer'

    def inner():
        msg = 'I am inner'
        print(msg)

    inner()
    print(msg)


outer()
print(msg)
