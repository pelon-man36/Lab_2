"""
Coin Program
Johan D. Ramirez Maldonado
This program simulates flipping a single coin.
It is either heads or tails.
06/27/26
"""

from random import randint

class Coin():
    def __init__(self, _sideup="Heads"):
        self._sideup = _sideup

    def toss(self):
        flip = randint(0, 1)
        if flip == 0:
            self._sideup = "Heads"
        else:
            self._sideup = "Tails"

    def get_sideup(self):
        return self._sideup

