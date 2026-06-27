from coin import Coin
class Player(Coin):
    def __init__(self, _name="Player 1", _coin=Coin(),  _wallet=20):
        self._name = _name
        self._name = _wallet
        self._coin = _coin

    def toss_coin(self):
        
