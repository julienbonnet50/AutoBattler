from app.Constants.conf import *

class Spell:
    def __init__(self,name, range, damages, cost):
        self.name = name
        self.range = range
        self.damage = damages
        self.cost = cost
        self.possible_attacks = []

    def find_possible_attacks(self, map, player_position, player_name):
        # Extract the x and y values from the player's position
        player_x = player_position[0]
        player_y = player_position[1]

        if DEBUG_MODE_SPELL == True:
            print(f'Starting find possible attacks for {player_name} from position {player_position}')

        # Determine which cells are within the spell's range
        for x in range(max(0, player_x - self.range), min(map.mapSize, player_x + self.range + 1)):
            for y in range(max(0, player_y - self.range), min(map.mapSize, player_y + self.range + 1)):
                if abs(x - player_x) + abs(y - player_y) <= self.range:
                    if DEBUG_MODE_SPELL == True:
                        print(f'Checking at ({x}, {y})')

                    # Check if the cell is occupied by an enemy character
                    if map.map[x][y] != '' and map.map[x][y][0] != player_name[0]:
                        if DEBUG_MODE_SPELL == True:
                            print(f'Found possible attacks for {player_name} at position ({x}, {y})')
                        
                        # Add the enemy character's position to the list of possible attacks
                        self.possible_attacks.append((x, y, map.map[x][y]))