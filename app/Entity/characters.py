import random
from app.Conf.conf import *

class Characters():

    def __init__(self, id, name, hp, pa, pm, position_x, position_y, spells, team, imgpath, damage, speed):
        self.id = id
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.pa = pa
        self.team = team
        self.current_pa = pa
        self.pm = pm
        self.damage = damage
        self.speed = speed
        self.current_pm = pm
        self.position_x = position_x
        self.position_y = position_y
        self.spells = spells
        self.imgpath = imgpath
        self.possible_moves = []
    
    def printStats(self):
        print(f'{self.name} has {self.hp} HP left')

    def checkIfAlive(self):
        if self.hp > 0:
            if DEBUG_MODE_MOVE == True:
                print(f"Starting turn of {self.name}")
            return True
        
        return False

    def resolveColor(self):
        if self.team == "ally":
            return HAPPY_BLUE
        elif self.team == "ennemies":
            return VIOLET
        
    # Movement 

    def move(self, position):
        distance = abs(self.position_x - position[0]) + abs(self.position_y  - position[1])
        self.position_x = position[0]
        self.position_y = position[1]
        if DEBUG_MODE_MOVE == True:
            print(f"Charater {self.name} used {distance} PM to move ({self.position_x}, {self.position_y})")

    def evaluate_moves(self, map):
        if len(self.possible_moves) < 1:
            if DEBUG_MODE_MOVE == True:
                return self.position_x, self.position_y
            
        random.shuffle(self.possible_moves)
        
        possibleMoves = self.possible_moves
        for move in possibleMoves:
            if  map.map[move[0]][move[1]] == 0:
                if DEBUG_MODE_MOVE == True:
                    print(f"Move picked is : {move}")
                return move
            if  map.map[move[0]][move[1]] != 1:
                if DEBUG_MODE_MOVE == True:
                    print(f"Characters {self.name} cannot move because cell ({move[0]}, {move[1]}) is an obsactle")
                continue
            if  map.map[move[0]][move[1]] != 0 and map.map[move[0]][move[1]] != 1:
                if DEBUG_MODE_MOVE == True:
                    print(f"Characters {self.name} cannot move because cell ({move[0]}, {move[1]}) is already occupied") 
                continue       
            else: continue

    def get_possible_moves(self, position_x, position_y, pm, map_size):
        # Vérifier si le joueur a encore des points de déplacement
        if pm <= 0:
            return []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_position_x = position_x + dx
            new_position_y = position_y + dy
            if 0 <= new_position_x < map_size and 0 <= new_position_y < map_size:
                distance = abs(dx) + abs(dy)
                if pm >= distance:
                    if (new_position_x, new_position_y) not in self.possible_moves:
                        self.get_possible_moves(new_position_x, new_position_y, pm - distance, map_size)
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

                return spell, target_position

        return False
