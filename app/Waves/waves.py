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
        charactersSelected = [self.charList.Entity_HAND, 
                              self.charList.Entity_MOSKITOS]
        wave = Wave(map, charactersSelected)

        self.waves.append(wave)

    def addWave2(self):
        map = Map(10)
               
        charactersSelected = [self.charList.Entity_BOSS]
        wave = Wave(map, charactersSelected)

        self.waves.append(wave)