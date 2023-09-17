import os
import time

from goly import Goly

if __name__ == '__main__':
    bool_array = [
        [False, False, False, False, False, False],

        [False, False, False, False, False, False],

        [False, True, True, True, False, False],

        [False, False, False, False, False, False],

        [False, False, False, False, False, False],

        [False, False, False, False, False, False]
                  ]
    game = Goly(6, 6, tabla=bool_array)
    for i in range(0, 100):
        print(game)
        time.sleep(0.1)
        game.comprobarCambios()
        if game.isGameDead():
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

