from types import NoneType
from app.Constants.conf import *

class App:
    def __init__(self, map, characters):
        self.map = map
        self.characters = characters

    def printStats(self):
        for char in self.characters:
            char.printStats()

    def checkDeadChar(self):
        for char in self.characters:
            if char.hp < 0:
                print(f'\nGame is done, {char.name} is dead !\n ')
                return False
        return True
    
    def firstTurn(self):
        print("Turn : 0")
        for char in self.characters:
            self.map.placeCharacters(char)
            if DEBUG_MODE_MOVE == True:
                print(f'Placed {char.name} at ({char.position_x}, {char.position_y})')

        self.map.display()

    def find_player_by_position(self, position):
        positionCharName = self.map.map[position[0]][position[1]]

        if positionCharName == '':
            print(f"No characters found at ({position[0], position[1]})")

        for char in self.characters:
            if char.name == positionCharName:
                if DEBUG_MODE_SPELL == True:
                    print(f"Found {positionCharName} at position ({position[0], [position[1]]})")
                return char
            
        return None

    def spellActionApp(self, caster, target, spell):
        if target is None:
            print("No target found")
            return False

        target.hp -= spell.damage

        print(f"{caster.name} casts {spell.name} on {target.name} for {spell.damage} damage!")
        return True
    

    def doTurn(self):
        for char in self.characters:
            # Start
            print(f"Starting turn of {char.name}")

            # Movements
            char.clear_moves()
            char.get_possible_moves(char.position_x, char.position_y, char.pm, self.map.mapSize)

            if DEBUG_MODE_MOVE == True:
                print(f'Possible moves : {char.possible_moves}')

            move_evaluated = char.evaluate_moves(self.map)
            char.move(move_evaluated)
            self.map.placeCharacters(char)
            self.map.resetMap(self.characters)

            # Spells 
            while char.checkPA() == True:
                spell = char.is_attack_possible(self.map)
                if spell != False:
                    target = self.find_player_by_position(spell[1])
                    self.spellActionApp(char, target, spell[0])
                else: break

            char.resetPA()
            char.clearSpells()
            
            print("\n")
            self.printStats()
            self.map.display()
            
