import sys
sys.dont_write_bytecode = True

from app.Waves.waves import Waves
from app.app import App
from app.Conf.conf import *
from app.Data.initCharacters import *
from app.Data.initSpells import *
from app.Entity.allyTeam import *
from app.menu import *
import time

# init
menu = Menu()

# Start menu
menu.runMenu()

# Start waves
wavesList = Waves()
allyTeam = AllyTeam(wavesList.charList)

for i in range (0, len(wavesList.waves)):
    game = App(allyTeam.characters, wavesList.waves[i], wavesList.buffsPool.buffsList)
    game.firstTurn()
    while game.ennemiesAlive > 0:
        print("Turn : ", game.turn)
        game.doTurn()

    game.buffChoice()
    allyTeam.characters = game.selectAllyBuffed()

    time.sleep(3)
