from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    option = input("Do you want to toss a coin?(y/n) ")

    while option != "n":
        print("Hi")
        option = input("Do you want to toss a coin?(y/n) ")

main()
