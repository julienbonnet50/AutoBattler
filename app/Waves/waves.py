from app.Entity.charactersList import CharactersList
from app.Map.map import Map
from app.Waves.wave import Wave
from app.Entity.characters import Characters
from app.Buffs.buffs import Buffs
from app.Buffs.buff import Buff
import random

class Waves:
    def __init__(self):
        self.waves = []
        self.charList = CharactersList()
        self.buffsPool = Buffs()
        self.addWave1()
        self.addWave2()         

    def addWave1(self):
        map = Map(25)
        charactersSelected = [self.charList.Entity_ARCHER,
                              self.charList.Entity_HAND, 
                              self.charList.Entity_MOSKITOS]
        wave = Wave(map, charactersSelected)

        self.waves.append(wave)

    def addWave2(self):
        map = Map(10)

        Entity_monster = Characters("Boss", 
                    600,
                    12, 
                    3, 
                    2,
                    0,
                    [self.charList.Spell_beco],
                    'ennemies',
                    'hand.png')
        
        Entity_ARCHER_2 = Characters("Archer", 
                    100,
                    5, 
                    4, 
                    5,
                    9,
                    [self.charList.Spell_offense],
                    'ally',
                    'archer.png')
               
        charactersSelected = [Entity_ARCHER_2, Entity_monster]
        wave = Wave(map, charactersSelected)

        self.waves.append(wave)