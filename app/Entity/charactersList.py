from app.Entity.characters import Characters
from app.Spells.spell import Spell
from app.Constants.conf import *
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
        self.Entity_eliotrope = Characters(P1_INIT_NAME, 
                            P1_INIT_HP,
                            P1_INIT_PA, 
                            P1_INIT_PM, 
                            P1_INIT_POSITION_X, 
                            P1_INIT_POSITION_Y,
                            [self.Spell_offense],
                            P1_INIT_TEAM)

        self.Entity_bouftou_blanc = Characters(BOUFTOU_INIT_NAME + "1", 
                            BOUFTOU_INIT_HP,
                            BOUFTOU_INIT_PA, 
                            BOUFTOU_INIT_PM, 
                            BOUFTOU_INIT_POSITION_X, 
                            BOUFTOU_INIT_POSITION_Y,
                            [self.Spell_morsure],
                            BOUFTOU_INIT_TEAM)

        self.Entity_tofu = Characters(TOFU_INIT_NAME, 
                            TOFU_INIT_HP,
                            TOFU_INIT_PA, 
                            TOFU_INIT_PM, 
                            TOFU_INIT_POSITION_X, 
                            TOFU_INIT_POSITION_Y,
                            [self.Spell_beco],
                            TOFU_INIT_TEAM)
