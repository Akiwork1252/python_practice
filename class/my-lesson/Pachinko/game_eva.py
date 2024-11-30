import random
from pachinko import Pachinko

def eva(self):
    Pachinko.lend(self)
    n = Pachinko.ball_goes_in(self)
    def lottery(n):
        n = random.randrange(1, 319)
        user = random.randrange(1, 319)
        if n == user:
            print('大当り')
        else:
            print('-')

