from game import *

def main():
    my_game = jeu()
    pyxel.run(my_game.update, my_game.draw)

main()