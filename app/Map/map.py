from app.Entity.characters import Characters
from app.Data.initMap import * 
from app.Conf.conf import *
import tkinter as tk
from tkinter import *
import random
import os
from math import gcd
import copy

class Map:
    def __init__(self, map, mapSize):
        self.mapSize = mapSize
        self.map = map
        self.bodies = []
        self.obstaclesImgPath = []


    def create_map(self, n):
        map = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('')
            map.append(row)
        self.map = map
        self.mapSize = n
    
    def addWindow(self, window):
        self.window = window
    
    def resetMap(self, map, characters):
        self.map = map
        if DEBUG_MAP == True:
            print(f'Reset map with : {map}')

        for char in characters:
            self.placeCharacters(char)
    
    def placeCharacters(self, character):
        if DEBUG_CHAR == True:
                print(f'Placed {character.name} at ({character.position_x}, {character.position_y})')
        self.map[character.position_x][character.position_y] = character.name

    def displayMap(self, game_window):
        if self.mapSize < 12:
            mapImgPath = os.path.join(sourceFileDir, 'assets', 'map', 'bossmap_200x200.png')
        elif self.mapSize > 24:
            mapImgPath = os.path.join(sourceFileDir, 'assets', 'map', 'map_500x500.png')
            
        mapImg = pygame.image.load(mapImgPath).convert()
        # Draw Map
        game_window.blit(mapImg, (10 , 10))
        self.displayObstacle(game_window)
    
    def displayObstacle(self, game_window):
        for x in range(0, self.mapSize):
            for y in range(0, self.mapSize):
                if self.map[x][y] == 1:
                    obstacleImgPath = IMG_BOX_PATH
                elif self.map[x][y] == 2: 
                    obstacleImgPath = IMG_TORCH_PATH
                elif  self.map[x][y] == 3: 
                    obstacleImgPath = IMG_GREEN_JAR_PATH
                elif self.map[x][y] == 4:
                    obstacleImgPath = IMG_RED_JAR_PATH
                else: continue

                mapObstacleImg = pygame.image.load(obstacleImgPath).convert_alpha()
                game_window.blit(mapObstacleImg, ((x ) * SPACE_SIZE + SPACE_SIZE, (y) * SPACE_SIZE + SPACE_SIZE))


    def displayGrid(self, game_window):
        for x in range(0, self.mapSize * SPACE_SIZE, SPACE_SIZE):
            for y in range(0, SPACE_SIZE * self.mapSize, SPACE_SIZE):
                rect = pygame.Rect(x + SPACE_SIZE, y + SPACE_SIZE, SPACE_SIZE, SPACE_SIZE)
                pygame.draw.rect(game_window, WHITE, rect, 1)
    
    def isObstacle(self, map, pos):
        return (map[pos[0]][pos[1]]==1)
    
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
                    if isinstance(value, (int, float, complex)):
                        value = value
                    elif isinstance(value, str):
                        value = value[0]
                    print(f"| {value} ",end="")
                print("|")

            for col in range(num_cols-1):
                print("+---",end="")

            print("+---+")

            print("\n")
