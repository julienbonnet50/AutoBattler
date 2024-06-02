from app.Entity.charactersSpellsList import CharactersSpellsList
from app.Map.map import Map
from app.Waves.wave import Wave
from app.Entity.characters import Characters
from app.Buffs.buffs import Buffs
from app.Buffs.buff import Buff
import random

class Waves:
    def __init__(self):
        self.waves = []
        self.charList = CharactersSpellsList()
        self.buffsPool = Buffs()
        self.addWave1()
        self.addWave2()         

    def addWave1(self):
        map = Map(25)
        
        charactersSelected = [self.charList.charactersList[1], 
                              self.charList.charactersList[2]]
        wave = Wave(map, charactersSelected)

        self.waves.append(wave)

    def addWave2(self):
        map = Map(10)
               
        charactersSelected = [self.charList.charactersList[3]]
        wave = Wave(map, charactersSelected)

        self.waves.append(wave)