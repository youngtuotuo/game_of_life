import logging
from gol.game import GameOfLife


def main():
    game = GameOfLife()
    while game.run:
        game.play()
    game.quit()


if __name__ == "__main__":
    main()
