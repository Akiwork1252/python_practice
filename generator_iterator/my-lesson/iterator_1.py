class MyIterator:
    def __init__(self, count):
        self.count = count

    def __next__(self):
        while self.count >= 2:
            if self.count % 2 == 0:
                num = self.count
                self.count -= 2
                return num

    def __iter__(self):
        return self


iter = MyIterator(11)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))