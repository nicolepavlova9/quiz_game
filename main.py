from models.game import Game


def main():
    game = Game()

    while True:
        game.start_game()
        if input("Do you want to play again? (y/n): ").lower() != "y":
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
