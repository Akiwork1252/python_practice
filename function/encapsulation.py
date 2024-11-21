# レスポンスシビリティの分離
def casino_entrance(age, min_age=21):


    def inner_casino_entrance():
        print('Welcome')

    if age > min_age:
       inner_casino_entrance()


casino_entrance(22)