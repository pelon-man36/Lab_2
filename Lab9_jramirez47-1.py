from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    name1 = player1.get_name()
    name2 = player2.get_name()
    print(f"{name1} has {player1.get_wallet} coins")
    print(f"{name2} has {player2.get_wallet} coins")
    option = input("Do you want to toss coins? (y/n) ")
#
    while option != "n":
        print("Tossing coins...")
        player1.toss_coin()
        player2.toss_coin()
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()
        print(f"{name1} got {side1}.")
        print(f"{name2} got {side2}.")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"Match! {name1} wins a coin!")
        else:
            player1.lose_coin()
            player2.win_coin()
            print(f"No match! {name2} wins a coin!")

        print(f"{name1} has {player1.get_wallet} coins")
        print(f"{name2} has {player2.get_wallet} coins")
        option = input("Do you want to toss coins? (y/n) ")
main()
print("End of Program")
