from app.Entity.charactersList import *

class AllyTeam:
    def __init__(self, charList):
        self.characters = []
        self.charList = charList
        self.addAlly()
        
    def addAlly(self):
        if DEBUG_CHAR == True:
            print(f'add archer')
        self.characters.append(self.charList.Entity_ARCHER)
        
        