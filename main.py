import sys
sys.dont_write_bytecode = True

from app.Entity.characters import Characters
from app.Map.map import Map
from app.app import App
from app.Constants.conf import *
from app.Constants.initCharacters import *
from app.Constants.initSpells import *
from app.Spells.spell import Spell
import tkinter as tk
import time

# init
map = Map(25)
turnToPlay = 5
turn = 1

# Spells
offense = Spell(OFFENSE_NAME, OFFENSE_RANGE, OFFENSE_DAMAGES, OFFENSE_COST)
morsure = Spell(MORSURE_NAME, MORSURE_RANGE, MORSURE_DAMAGES, MORSURE_COST)
portail = Spell(PORTAIL_NAME, PORTAIL_RANGE, PORTAIL_DAMAGES, PORTAIL_COST)

# Players
eliotrope = Characters(P1_INIT_NAME, 
                       P1_INIT_HP,
                       P1_INIT_PA, 
                       P1_INIT_PM, 
                       P1_INIT_POSITION_X, 
                       P1_INIT_POSITION_Y,
                       [offense],
                       P1_INIT_TEAM)

bouftou1 = Characters(P2_INIT_NAME + "1", 
                     P2_INIT_HP,
                     P2_INIT_PA, 
                     P2_INIT_PM, 
                     P2_INIT_POSITION_X, 
                     P2_INIT_POSITION_Y,
                     [morsure],
                     P2_INIT_TEAM)

# bouftou2 = Characters(P2_INIT_NAME + "2", 
#                      P2_INIT_HP,
#                      P2_INIT_PA, 
#                      P2_INIT_PM, 
#                      P2_INIT_POSITION_X - 2, 
#                      P2_INIT_POSITION_Y - 2,
#                      [morsure],
#                      P2_INIT_TEAM)

# bouftou3 = Characters(P2_INIT_NAME + "3", 
#                      P2_INIT_HP,
#                      P2_INIT_PA, 
#                      P2_INIT_PM, 
#                      P2_INIT_POSITION_X + 3, 
#                      P2_INIT_POSITION_Y + 3,
#                      [morsure],
#                      P2_INIT_TEAM)

# Instanciate characters
characters = [eliotrope, bouftou1]
game = App(map, characters)

# Start wave
game.firstTurn()

while game.deadChar == False:
    print("Turn : ", game.turn)
    game.doTurn()

