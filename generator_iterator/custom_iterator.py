class MyIterator:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        num = self.current
        self.current += 1
        return num

    def __iter__(self):
        return self


myiterator = MyIterator(10)
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(iter(myiterator))
print(id(myiterator))
print(id(iter(myiterator)))