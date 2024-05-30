from app.Entity.characters import Characters
from app.Spells.spell import Spell
from app.Conf.conf import *
from app.Constants.initCharacters import *
from app.Constants.initSpells import *

class CharactersList:
    def __init__(self):
        # Spells
        self.Spell_offense = Spell(OFFENSE_NAME, OFFENSE_RANGE, OFFENSE_DAMAGES, OFFENSE_COST)
        self.Spell_morsure = Spell(MORSURE_NAME, MORSURE_RANGE, MORSURE_DAMAGES, MORSURE_COST)
        self.Spell_portail = Spell(PORTAIL_NAME, PORTAIL_RANGE, PORTAIL_DAMAGES, PORTAIL_COST)
        self.Spell_beco = Spell(BECO_NAME, BECO_RANGE, BECO_DAMAGES, BECO_COST)

        # Players
        self.Entity_ARCHER = Characters(ARCHER_INIT_NAME, 
                            ARCHER_INIT_HP,
                            ARCHER_INIT_PA, 
                            ARCHER_INIT_PM, 
                            ARCHER_INIT_POSITION_X, 
                            ARCHER_INIT_POSITION_Y,
                            [self.Spell_offense],
                            ARCHER_INIT_TEAM,
                            ARCHER_INIT_PATHIMG,
                            ARCHER_INIT_DAMAGE,
                            ARCHER_INIT_SPEED)

        self.Entity_HAND = Characters(HAND_INIT_NAME + "1", 
                            HAND_INIT_HP,
                            HAND_INIT_PA, 
                            HAND_INIT_PM, 
                            HAND_INIT_POSITION_X, 
                            HAND_INIT_POSITION_Y,
                            [self.Spell_morsure],
                            HAND_INIT_TEAM,
                            HAND_INIT_PATHIMG,
                            HAND_INIT_DAMAGE,
                            HAND_INIT_SPEED)

        self.Entity_MOSKITOS = Characters(MOSKITOS_INIT_NAME, 
                            MOSKITOS_INIT_HP,
                            MOSKITOS_INIT_PA, 
                            MOSKITOS_INIT_PM, 
                            MOSKITOS_INIT_POSITION_X, 
                            MOSKITOS_INIT_POSITION_Y,
                            [self.Spell_beco],
                            MOSKITOS_INIT_TEAM,
                            MOSKITOS_INIT_PATHIMG,
                            MOSKITOS_INIT_DAMAGE,
                            MOSKITOS_INIT_SPEED)
        
        self.Entity_BOSS = Characters(BOSS_INIT_NAME, 
                            BOSS_INIT_HP,
                            BOSS_INIT_PA, 
                            BOSS_INIT_PM, 
                            BOSS_INIT_POSITION_X, 
                            BOSS_INIT_POSITION_Y,
                            [self.Spell_beco],
                            BOSS_INIT_TEAM,
                            BOSS_INIT_PATHIMG,
                            BOSS_INIT_DAMAGE,
                            BOSS_INIT_SPEED)
