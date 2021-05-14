from controllers import GameController
import sys

if __name__ == "__main__":
    # This is the main "entrypoint" to the game
    player = sys.argv[1]
    game = GameController(player)
    game.main_menu()
