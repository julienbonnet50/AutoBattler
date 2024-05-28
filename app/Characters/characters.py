import random
from app.Constants.conf import *

class Characters():

    def __init__(self, name, hp, pa, pm, position_x, position_y, spells):
        self.name = name
        self.hp = hp
        self.pa = pa
        self.current_pa = pa
        self.pm = pm
        self.position_x = position_x
        self.position_y = position_y
        self.spells = spells
        self.possible_moves = []
    
    def printStats(self):
        print(f'{self.name} has {self.hp} HP left')

    def checkIfAlive(self):
        if self.hp > 0:
            print(f"Starting turn of {self.name}")
            return True
        
        return False

    # Movement 

    def move(self, position):
        distance = abs(self.position_x - position[0]) + abs(self.position_y  - position[1])
        self.position_x = position[0]
        self.position_y = position[1]
        if DEBUG_MODE_MOVE == True:
            print(f"Charater {self.name} used {distance} PM to move ({self.position_x}, {self.position_y})")

    def evaluate_moves(self, map):
       #TODO : for possible_move in self.possible_moves:

        final_position = random.choice(self.possible_moves)
        if  map.map[final_position[0]][final_position[1]] != '':
            if DEBUG_MODE_MOVE == True:
                print(f"Characters {self.name} cannot move because cell ({final_position[0]}, {final_position[1]}) is already occupied")
            return self.position_x, self.position_y

        if DEBUG_MODE_MOVE == True:
            print(f"Move picked is : {final_position}")

        return final_position

    def get_possible_moves(self, position_x, position_y, pm, map_size):
        # Vérifier si le joueur a encore des points de déplacement
        if pm <= 0:
            return []

        # Explorer les cases adjacentes
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Calculer la nouvelle position
            new_position_x = position_x + dx
            new_position_y = position_y + dy

            # Vérifier si la nouvelle position est dans les limites de la grille
            if 0 <= new_position_x < map_size and 0 <= new_position_y < map_size:
                # Vérifier si le joueur a suffisamment de points de déplacement pour s'y rendre
                distance = abs(dx) + abs(dy)
                if pm >= distance:

                    if (new_position_x, new_position_y) not in self.possible_moves:
                        # Appeler récursivement la fonction avec la nouvelle position et le nombre de points de déplacement restants
                        self.get_possible_moves(new_position_x, new_position_y, pm - distance, map_size)

                        # Ajouter la nouvelle position et les possibilités de déplacement suivantes à la liste de possibilités de déplacement
                        self.possible_moves.append((new_position_x, new_position_y))
    
    def clear_moves(self):
        self.possible_moves = []

    # Spells

    def clearSpells(self):
        for spell in self.spells:
            spell.clear_possible_attacks()

    def checkPA(self):
        for spell in self.spells:
            if spell.cost <= self.current_pa:
                return True
        return False

    def resetPA(self):
        self.current_pa = self.pa
    
    def is_attack_possible(self, map):
        for spell in self.spells:
            spell.find_possible_attacks(map, (self.position_x, self.position_y), self.name)
            if len(spell.possible_attacks) > 0:
                spellPosition = random.choice(spell.possible_attacks)
                # Get the target player's position from the spell position
                target_position = (spellPosition[0], spellPosition[1], spellPosition[2])
                # Call the spell_action method with the target player's position
                if DEBUG_MODE_SPELL == True:
                    print(f"Found possible attack from spell {spell.name} at position ({target_position})")

                self.current_pa -= spell.cost
                return spell, target_position

        return False
