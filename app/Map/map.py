from app.Characters.characters import Characters

class Map:
    def __init__(self, x):
        self.mapSize = x
        self.map = self.create_map(x)

    def create_map(self, n):
        map = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('')
            map.append(row)
        return map
    
    def resetMap(self, characters):
        self.map = self.create_map(self.mapSize)
        for char in characters:
            self.placeCharacters(char)
    
    def placeCharacters(self, characters):
        self.map[characters.position_x][characters.position_y] = characters.name
    
    def display(self):
        s = self.mapSize
        grid_size = s * s #
        # print(grid_size)
        num_rows = s
        num_cols = s

        for row in range(num_rows):
            for col in range(num_cols-1):
                print("+---",end="")

            print("+---+")
            for col in range(num_cols):
                i = row*num_cols|col     
                value = self.map[col][row]     
                if value == '':
                    value = ' '
                else:
                    value = value[0]
                print(f"| {value} ",end="")
            print("|")

        for col in range(num_cols-1):
            print("+---",end="")

        print("+---+")

        print("\n")