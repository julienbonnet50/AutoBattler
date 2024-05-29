import sys
sys.dont_write_bytecode = True

from app.Waves.waves import Waves
# from AutoBattler.app.Buffs.buffs import Buffs
from app.app import App
from app.Constants.conf import *
from app.Constants.initCharacters import *
from app.Constants.initSpells import *
from app.Spells.spell import Spell
import time

# init
wavesList = Waves()
# buffs = Buffs()

# Start wave 1
for i in range (0, len(wavesList.waves)):
    game = App(wavesList.waves[i])
    game.firstTurn()
    while game.ennemiesAlive > 0:
        print("Turn : ", game.turn)
        game.doTurn()

    # buffPool = buffs.generatePool()
    time.sleep(5)
