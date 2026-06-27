from coin import Coin
class Player(Coin):
    def __init__(self, _name="Player 1", _wallet=20, _coin=Coin()):
        self._name = _name
        self._name = _wallet
        self._coin = _coin

    def toss_coin(self):
        self._coin.toss()

    def get_coin_side(self):
        get = Coin()
        get.get_sideup()