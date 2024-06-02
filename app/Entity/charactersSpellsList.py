
import os
from utils.csv_loader import *
from app.Conf.conf import *
from app.Spells.spell import *
from app.Entity.characters import *

class CharactersSpellsList:
    def __init__(self):
        # Spells
        self.spellsList = []
        self.charactersList = []
        self.loadSpellData()
        self.loadCharData()

    # Load buff 
    
    def loadSpellData(self):
        sourceFileDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pathSpellData = os.path.join(sourceFileDir, 'Data', 'spells.csv')
        dataSpell = load_csv(pathSpellData)

        for spell in dataSpell:
        
            spellMapping = Spell(id=int(spell["id"]),
                                 name=spell["name"], 
                                 range=int(spell["range"]), 
                                 damage=int(spell["damage"]), 
                                 cost=int(spell["cost"]))
            
            self.spellsList.append(spellMapping)
            if  DEBUG_MODE_SPELL == True:
                print(f'Append spell {spellMapping.name} to spellList')

    def loadCharData(self):
        sourceFileDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pathCharData = os.path.join(sourceFileDir, 'Data', 'characters.csv')

        dataChar = load_csv(pathCharData)
        
        for char in dataChar:
            charMapping = Characters(id=int(char["id"]),
                                     damage=int(char["damage"]),
                                     name=char["name"],
                                     hp=float(char["hp"]),
                                     imgpath=char["imgpath"],
                                     pa=int(char["pa"]),
                                     pm=int(char["pm"]),
                                     position_x=int(char["position_x"]),
                                     position_y=int(char["position_y"]),
                                     speed=int(char["speed"]),
                                     spells=char["spells"].split("-"),
                                     team=char["team"]
                                     )
            charMapping.spells = self.resolveSpells(charMapping)
            self.charactersList.append(charMapping)
            if  DEBUG_CHAR == True:
                print(f'Append char {charMapping.name} to charList')
            
    def resolveSpells(self, char):
        spellsResolved = []
        for spellId in char.spells:
            spellId = spellId.replace("'", "")
            spell = self.spellsList[int(spellId)]
            spellsResolved.append(spell)
            
        return spellsResolved

