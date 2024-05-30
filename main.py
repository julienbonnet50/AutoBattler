import sys
sys.dont_write_bytecode = True

from app.Waves.waves import Waves
# from app.Buffs.buffs import Buffs
from app.app import App
from app.Conf.conf import *
from app.Constants.initCharacters import *
from app.Constants.initSpells import *
from app.Spells.spell import Spell
from app.menu import *
import time

# init
wavesList = Waves()
menu = Menu()

# Start menu
menu.runMenu()
# Start waves
for i in range (0, len(wavesList.waves)):
    game = App(wavesList.waves[i], wavesList.buffsPool.buffsList)
    game.firstTurn()
    while game.ennemiesAlive > 0:
        print("Turn : ", game.turn)
        game.doTurn()

    game.buffChoice()

    time.sleep(3)
