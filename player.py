from coin import Coin

class Player(Coin):
    def __init__(self, _name="Player 1", _wallet=20, _coin=Coin()):
        self._name = _name
        self._wallet = _wallet
        self._coin = _coin

    def toss_coin(self):
        self._coin.toss()

    def get_coin_side(self):
        return self._coin.get_sideup()

    def win_coin(self):
        self._wallet += 1

    def lose_coin(self):
        self._wallet -= 1

    def get_wallet(self):
        return self._wallet

    def get_name(self):
        return self._name
    
