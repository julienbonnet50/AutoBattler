from app.Entity.charactersSpellsList import *

class AllyTeam:
    def __init__(self, charList):
        self.characters = []
        self.charList = charList
        self.addAlly()
        
    def addAlly(self):
        self.characters.append(self.charList.charactersList[0])
        self.characters.append(self.charList.charactersList[5])
        self.characters.append(self.charList.charactersList[6])

        
        