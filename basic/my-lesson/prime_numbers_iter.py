class PrimeNumbersIterator:
    def __init__(self, start=0, stop=1000):
        self.start = start
        self.stop = stop

    # 素数判定。素数であれば値を返す
    def return_prime_numbers(self, num):
        division_list = []
        for i in range(1, num+1):
            if num % i == 0:
                division_list.append(i)
        if len(division_list) == 2:
            return num

    # 入力されたstopまでの全ての素数をリスト化する
    def add_list(self):
        stop = self.stop
        prime_list = []
        for i in range(1, stop+1):
            n = self.return_prime_numbers(i)
            if n is None:
                continue
            else:
                prime_list.append(n)
        return prime_list

    def __next__(self):
        prime_list = self.add_list()
        num = self.start
        self.start += 1
        while self.start < len(prime_list):
            return prime_list[num]

    def __iter__(self):
        return self


prime_iter = PrimeNumbersIterator()
print(next(prime_iter))
print(next(prime_iter))
print(next(prime_iter))
print(next(prime_iter))
print(next(prime_iter))
