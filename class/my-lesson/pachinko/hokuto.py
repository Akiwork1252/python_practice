from store import Store

class Hokuto(Store):
    def hokuto(self):
        print('CR北斗の拳で遊びます。')
        Store.lend(self)
