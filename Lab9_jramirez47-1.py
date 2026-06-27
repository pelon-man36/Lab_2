from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    option = input("Do you want to toss a coin?(y/n) ")

    while option != "n":
        print("Tossing coins...")
        player1.toss_coin()
        side1 = player1.get_coin_side()
        player2.toss_coin()
        side2 = player2.get_coin_side()
        print(f"{player1.get_name()} got {side1}.")
        print(f"{player2.get_name()} got {side2}.")
        option = input("Do you want to toss a coin?(y/n) ")

main()
