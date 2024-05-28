class Spell:
    def __init__(self, range, damages, cost):
        self.range = range
        self.damage = damages
        self.cost = cost
        self.possible_attacks = []

    def find_possible_attacks(self, map, player_position):
        # Extract the x and y values from the player's position
        player_x = player_position[0]
        player_y = player_position[1]

        # Determine which cells are within the spell's range
        for x in range(max(0, player_x - self.range), min(map.mapSize, player_x + self.range + 1)):
            for y in range(max(0, player_y - self.range), min(map.mapSize, player_y + self.range + 1)):
                if abs(x - player_x) + abs(y - player_y) <= self.range:
                    # Check if the cell is occupied by an enemy character
                    if map.map[x][y] != '':
                        # Add the enemy character's position to the list of possible attacks
                        self.possible_attacks.append((x, y, map.map[x][y]))