from coin import Coin

class Player(Coin):
    def __init__(self, _name="Player 1", _wallet=20, _coin=Coin()):
        self._name = _name
        self._wallet = _wallet
        self._coin = _coin

    def toss_coin(self):
        self._coin.toss()
        print(self._coin.toss())