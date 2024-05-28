from app.Constants.conf import DEBUG_MODE_MOVE

class App:
    def __init__(self, map, characters):
        self.map = map
        self.characters = characters
    
    def firstTurn(self):
        for char in self.characters:
            self.map.placeCharacters(char)

        self.map.display()
    
    def spellActionApp(self, caster, name, spell):
        for target in self.characters:
            if target.name == name:
                # Apply the spell's damage to the target player's PA
                target.hp -= spell.damage

                # Print a message to indicate that the spell was cast
                print(f"{caster.name} casts {spell.name} on {target.name} for {spell.damage} damage!")

                # Return True to indicate that the attack was successful
                return True

    def doTurn(self):
        self.map.resetMap()
        for char in self.characters:
            # Movements
            char.clear_moves()
            char.get_possible_moves(char.position_x, char.position_y, char.pm, self.map.mapSize)
            print(char.possible_moves)
            move_evaluated = char.evaluate_moves(self.map)
            char.move(move_evaluated)
            self.map.placeCharacters(char)

            # Spells 
            char.is_attack_possible(self.map)
            

        self.map.display()