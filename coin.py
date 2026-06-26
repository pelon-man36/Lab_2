from random import randint

class Coin():
    def __init__(self, _sideup):
        self._sideup = _sideup

    def toss(self):
        flip = randint(0, 1)
        if flip == 0:
            self._sideup = "Heads"
        else:
            self._sideup = "Tails"
        print(self._sideup)