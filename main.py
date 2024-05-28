import sys
sys.dont_write_bytecode = True

from app.Characters.characters import Characters
from app.Map.map import Map
from app.app import App
from app.Constants.initCharacters import *
from app.Constants.initSpells import *
from app.Spells.spell import Spell

# init
map = Map(7)
turnToPlay = 2

# Spells
offense = Spell(OFFENSE_RANGE, OFFENSE_DAMAGES, OFFENSE_COST)
morsure = Spell(MORSURE_RANGE, MORSURE_DAMAGES, MORSURE_COST)

# Players
eliotrope = Characters(P1_INIT_NAME, 
                       P1_INIT_PA, 
                       P1_INIT_HP,
                       P1_INIT_PM, 
                       P1_INIT_POSITION_X, 
                       P1_INIT_POSITION_Y,
                       [offense])

bouftou = Characters(P2_INIT_NAME, 
                     P2_INIT_HP,
                     P2_INIT_PA, 
                     P2_INIT_PM, 
                     P2_INIT_POSITION_X, 
                     P2_INIT_POSITION_Y,
                     [morsure])



# Instanciate characters
characters = [eliotrope, bouftou]
game = App(map, characters)
# Start
print("Turn : ", 0)
game.firstTurn()

for i in range (0, turnToPlay):
    print("Turn : ", i + 1)
    game.doTurn()
