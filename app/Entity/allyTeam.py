from app.Entity.charactersList import *

class AllyTeam:
    def __init__(self, charList):
        self.characters = []
        self.charList = charList
        self.addAlly()
        
    def addAlly(self):
        self.characters.append(self.charList.Entity_ARCHER)
        
        