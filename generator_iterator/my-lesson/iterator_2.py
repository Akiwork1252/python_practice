class MyIterator:
    def __init__(self, start):
        self.count = start

    def __next__(self):
        if self.count < 2:
            raise StopIteration
        elif self.count % 2 == 0:
            num = self.count
            self.count -= 2
            return num
        else:
            self.count -= 1
            return self.__next__()

    def __iter__(self):
        return self


iter = MyIterator(10)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))