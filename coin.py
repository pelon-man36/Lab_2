from random import randint

class Coin():
    def __init__(self, _sideup):
        self._sideup = _sideup

    def toss(self):
        flip = randint(0, 1)