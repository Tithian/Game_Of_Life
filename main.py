import time
import os

from goly import Goly
from gui import GameTable

MODE = "GUI"  # Console, GUI

if __name__ == '__main__':
    game = None
    if MODE.lower() == 'gui':
        test = GameTable()
        test.mainloop()
    elif MODE.lower() == 'console':
        game = Goly(12, 10, prob=0.2)
        for i in range(0, 100):
            print(game)
            time.sleep(1)
            game.comprobarCambios()
            if game.isGameDead():
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
    else:
        exit()
