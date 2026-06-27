from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    option = input("Do you want to toss coins? (y/n) ")
    
    while option != "n":
        