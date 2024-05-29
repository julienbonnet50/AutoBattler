from app.Entity.charactersList import CharactersList
from app.Map.map import Map
from app.Waves.wave import Wave
from app.Entity.characters import Characters

class Waves:
    def __init__(self):
        self.waves = []
        self.charList = CharactersList()
        self.addWave1()
        self.addWave2()

    def addWave1(self):
        map = Map(25)
        charactersSelected = [self.charList.Entity_eliotrope, self.charList.Entity_bouftou_blanc, self.charList.Entity_tofu]
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
                    'ennemies')
        
        self.charList.Entity_eliotrope.position_x = 5
        self.charList.Entity_eliotrope.position_y = 9
        
        charactersSelected = [self.charList.Entity_eliotrope,  Entity_monster]
        wave = Wave(map, charactersSelected)

        self.waves.append(wave)