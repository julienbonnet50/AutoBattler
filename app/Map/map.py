from app.Entity.characters import Characters
from app.Conf.conf import *
import tkinter as tk
from tkinter import *

class Map:
    def __init__(self, x):
        self.mapSize = x
        self.map = self.create_map(x)
        self.bodies = []

    def create_map(self, n):
        map = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('')
            map.append(row)
        return map
    
    def addWindow(self, window):
        self.window = window
    
    def resetMap(self, characters):
        self.map = self.create_map(self.mapSize)
        for char in characters:
            self.placeCharacters(char)
    
    def placeCharacters(self, character):
        if DEBUG_CHAR == True:
                print(f'Placed {character.name} at ({character.position_x}, {character.position_y})')
        self.map[character.position_x][character.position_y] = character.name
    
    def display(self):
        if DEBUG_MAP == True:
            s = self.mapSize
            grid_size = s * s #
            # print(grid_size)
            num_rows = s
            num_cols = s
            print("\n")
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
