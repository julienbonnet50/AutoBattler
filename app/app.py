from app.Constants.conf import *

class App:
    def __init__(self, map, characters):
        self.map = map
        self.characters = characters
    
    def firstTurn(self):
        for char in self.characters:
            self.map.placeCharacters(char)

        self.map.display()

    def find_player_by_position(self, position):
        if DEBUG_MODE_SPELL:
            print(f"Trying to find char at ({position[0], position[1]})")

        positionCharName = self.map.map[position[0]][position[1]][0]
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
            Exception("No target found")

        target.hp -= spell.damage

        print(f"{caster.name} casts {spell.name} on {target.name} for {spell.damage} damage!")
        return True
    

    def doTurn(self):
        self.map.resetMap()
        for char in self.characters:
            # Start
            print(f"Starting turn of {char.name}")
            # Movements
            char.clear_moves()
            char.get_possible_moves(char.position_x, char.position_y, char.pm, self.map.mapSize)

            if DEBUG_MODE_MOVE == True:
                print(char.possible_moves)

            move_evaluated = char.evaluate_moves(self.map)
            char.move(move_evaluated)
            self.map.placeCharacters(char)

            # Spells 
            spell = char.is_attack_possible(self.map)
            if spell != False:
                target = self.find_player_by_position(spell[1])
                self.spellActionApp(char, target, spell[0])

            if DEBUG_MODE_SPELL == True:
                print
            
            print("\n")
            
        self.map.display()