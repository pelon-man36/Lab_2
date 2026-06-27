from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")
    option = input("Do you want to toss a coin?(y/n) ")

    while option != "n":
        print("Tossing coins...")
        player1.toss_coin()
        side1 = player1.get_coin_side()
        player2.toss_coin()
        side2 = player2.get_coin_side()
        print(f"{player1.get_name()} got {side1}.")
        print(f"{player2.get_name()} got {side2}.")

        if side1 == side2:
            print(f"Match! {player1.get_name()} wins a coin!")
            player1.win_coin()
            player2.lose_coin()
        else:
            print(f"No match! {player2.get_name()} wins a coin!")
            player1.lose_coin()
            player2.win_coin()

        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")
        option = input("Do you want to toss a coin?(y/n) ")
    
    print("Match end!")
    print(f"{player1.get_name()} total: {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} total: {player2.get_wallet()} coins.")
    if player1.get_wallet() == player2.get_wallet():
        print("Tie! No winner or loser!")
    elif player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins!")
    else:
        print(f"{player2.get_name()} wins!")

main()
