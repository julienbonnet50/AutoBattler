from app.Entity.charactersList import *

class AllyTeam:
    def __init__(self):
        self.characters = []
        self.charList = CharactersList()
        self.addAlly()
        
    def addAlly(self):
        self.characters.append(self.charList.Entity_ARCHER)
        
        