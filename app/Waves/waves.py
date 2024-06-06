from app.Entity.charactersSpellsList import CharactersSpellsList
from app.Map.map import Map
from app.Waves.wave import Wave
from app.Entity.characters import Characters
from app.Buffs.buffs import Buffs
from app.Buffs.buff import Buff
from app.Data.initMap import *
import random

class Waves:
    def __init__(self):
        self.waves = []
        self.charList = CharactersSpellsList()
        self.buffsPool = Buffs()
        self.buffsSelected = None
        self.addWave1()
        self.addWave2()         

    def addWave1(self):
        map = Map(map=MAP_WAVE_1, mapSize=26)
        
        charactersSelected = [self.charList.charactersList[1], 
                              self.charList.charactersList[2],
                              self.charList.charactersList[4]]
        
        buffSelected = self.selectBuff(5, 0)
        
        wave = Wave(id=1, 
                    map=map, 
                    characters=charactersSelected, 
                    buffSelected=buffSelected)

        self.waves.append(wave)

    def addWave2(self):
        map = Map(map=MAP_WAVE_2, mapSize=11)
               
        charactersSelected = [self.charList.charactersList[3]]
        
        buffSelected = self.selectBuff(5, 0)
        
        wave = Wave(id=2, 
                    map=map, 
                    characters=charactersSelected, 
                    buffSelected=buffSelected)

        self.waves.append(wave)
        
    def selectBuff(self, numberOfBuff, difficulty):
        buffSelected = []
        if difficulty == 0:
            for i in range (0, numberOfBuff):
                random_float = random.uniform(0, 1)
                if random_float < 0.1:
                    buffs = [buff for buff in self.buffsPool.buffsList if buff.rarity == 2]
                elif random_float < 0.3:
                    buffs = [buff for buff in self.buffsPool.buffsList if buff.rarity == 1]
                else:
                    buffs = [buff for buff in self.buffsPool.buffsList if buff.rarity == 0]
                    
                buffSelected.append(random.choice(buffs))
        
        return buffSelected


                    
                    