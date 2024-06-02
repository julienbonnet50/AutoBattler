import sys
sys.dont_write_bytecode = True
import time
from types import NoneType
from app.Waves.wave import Wave
from app.Conf.conf import *
from app.Buffs.buffChoicer import *
from app.Map.map import *
import copy
from utils.display.draw import *



import pygame
import os

# get the directory of this file
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

class App:
    def __init__(self, allies, wave, buffPools):
        pygame.init()

        self.turn = 1
        self.wave_id = wave.id
        self.initial_map = None
        self.map = wave.map
        self.characters = wave.characters
        self.ennemiesAlive = None
        self.alliesAlive = None
        self.game_window = None
        self.buffSelected = buffPools

        self.initial_map = copy.deepcopy(self.map)
        self.addAlly(allies)
        self.initUi()

        self.buffChoicer = BuffChoicer(self.buffSelected,WIDTH, HEIGHT)
    
        # self.orderChars()

    # Start 
    
    def addAlly(self, allies):
        count = 0
        for ally in allies:
            if DEBUG_CHAR == True:
                print(f'{ally.name} added')
            ally.position_x = self.map.mapSize - (2 + count)
            ally.position_y = self.map.mapSize - 2
            self.characters.append(ally)

    def initUi(self):
        # Get icon
        iconPath = os.path.join(sourceFileDir, 'assets', 'iconAutoBattler.png')
        programIcon = pygame.image.load(iconPath).convert()
        pygame.display.set_icon(programIcon)

        # Initialise game window
        pygame.display.set_caption('AutoBattler')
        self.game_window  = pygame.display.set_mode((WIDTH, HEIGHT))

    # UI + Console prints

    def displayTurn(self):
        score_surface = PIXEL_FONT_15.render('Turn : ' + str(self.turn), True, WHITE)
        score_rect = score_surface.get_rect()
        self.game_window.blit(score_surface, score_rect)

    def displayChar(self):
        for char in self.characters:
            CHAR_COLOR = char.resolveColor()
            ratio = char.hp  / char.max_hp
            if DEBUG_MODE_MOVE == True:
                print(f'Trying to create rectangle for body at pos ({char.position_x}, {char.position_y})')

            # Load img
            path_to_asset = os.path.join(sourceFileDir, 'assets', 'characters', char.imgpath)
            character_image = pygame.image.load(path_to_asset).convert_alpha()

            # Draw characters
            self.game_window.blit(character_image, ((char.position_x ) * SPACE_SIZE + SPACE_SIZE, (char.position_y) * SPACE_SIZE + SPACE_SIZE))

            # Draw Health bar
            pygame.draw.rect(self.game_window, RED, pygame.Rect(
                (char.position_x) * SPACE_SIZE + SPACE_SIZE - 10, (char.position_y) * SPACE_SIZE -10 + SPACE_SIZE, SPACE_SIZE + 20, 5 )
            )
            pygame.draw.rect(self.game_window, GREEN, pygame.Rect(
                (char.position_x) * SPACE_SIZE + SPACE_SIZE - 10, (char.position_y) * SPACE_SIZE - 10 + SPACE_SIZE, (SPACE_SIZE + 20) * ratio, 5 )
            )

    # Wave :
    
    def selectAllyBuffed(self):
        allyBuffed = []
        for char in self.characters:
            if char.team == 'ally':
                allyBuffed.append(char)  
                if DEBUG_CHAR == True:
                    print(f'{char.name} returned with buff')
        return allyBuffed      
    
    def game_over(self):
        placeInformation(self.game_window, PIXEL_FONT_22, WIDTH/2, HEIGHT/4, 250 , SPACE_SIZE , f'Game turn : ' + str(self.turn), RED, True)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        quit()

    def game_win(self):
        placeInformation(self.game_window, PIXEL_FONT_22, WIDTH/2, HEIGHT/4, 50 , SPACE_SIZE , f'GOOD GAME !!! done in ' + str(self.turn) + ' turn', GREEN, True)

    def getGameState(self):
        for char in self.characters:
            if char.hp < 0:
                print(f'\n{char.name} is dead !')
                self.characters.remove(char)
                if char.team == 'ennemies':
                    self.ennemiesAlive -= 1
                elif char.team == 'ally':
                    self.alliesAlive -= 1

            if self.alliesAlive < 1:
                self.game_over()

            if self.ennemiesAlive < 1:
                self.game_win()

    def find_player_by_position(self, position):
        positionCharName = self.map.map[position[0]][position[1]]

        if positionCharName == '':
            print(f"No characters found at ({position[0], position[1]})")

        for char in self.characters:
            if char.name == positionCharName:
                if DEBUG_CHAR == True:
                    print(f"Found {positionCharName} at position ({position[0], [position[1]]})")
                return char
            
        return None

    def spellActionApp(self, caster, target, spell):
        if target is None:
            if DEBUG_MODE_SPELL == True:
                print("No target found")
            return False
        
        if target.team  == caster.team:
            if DEBUG_MODE_SPELL == True:
                print("Target got the same team as caster")
            return False

        caster.current_pa -= spell.cost
        target.hp -= spell.damage

        if DEBUG_MODE_SPELL == True:
            print(f"{caster.name} casts {spell.name} on {target.name} for {spell.damage} damage!")
        return True
    
    # Buff

    def buffChoice(self):
        if DEBUG_BUFF == True:
            print(f'Starting buff choice')
        self.game_window.fill(BLACK)
        pygame.display.update()
        self.buffChoicer.displayBuffChoice(self.game_window, False)
        buffChosenIndex = self.buffChoicer.choseBuff(self.game_window)
        self.characters= self.buffChoicer.applyBuff(indexBuff=buffChosenIndex, characters=self.characters)

    # Turns
    
#    def orderChars(self):
#       if DEBUG_BUFF == True:
#            print(f'Ordering characters')
#        self.characters = self.characters.sort(key=lambda character: character.speed, reverse=True)
        
    def startTurn(self):
        self.game_window.fill(BLACK)
        self.map.displayMap(self.game_window)
        # self.map.displayGrid(self.game_window)
        self.displayChar()
                
    def endTurn(self):
        self.getGameState()
        printStats(self.game_window, self.characters, self.ennemiesAlive, self.alliesAlive)
        self.map.display()
        self.displayTurn()
        pygame.display.update()
        print('\n')

    def firstTurn(self):
        countEnnemies = 0
        countAllies = 0
        print("Turn : 0")
        for char in self.characters:
            if char.team == 'ennemies':
                countEnnemies += 1
            elif char.team == 'ally':
                countAllies += 1

            self.map.placeCharacters(char)

        self.ennemiesAlive = countEnnemies
        self.alliesAlive = countAllies
        self.map.display()

    def resolveMapWave(self, id):
        if id == 1:
            return MAP_WAVE_1
        elif id == 2:
            return MAP_WAVE_2

    def doTurn(self):
        for char in self.characters:
            # Start
                # Movements

            self.startTurn()
            char.clear_moves()
            char.get_possible_moves(char.position_x, char.position_y, char.pm, self.map.mapSize)

            if DEBUG_MODE_MOVE == True:
                print(f'Possible moves : {char.possible_moves}')

            char.move(char.evaluate_moves(self.map))
            self.map.resetMap(map=self.resolveMapWave(self.wave_id), characters=self.characters)

            # Spells 
            while char.checkPA() == True:
                spell = char.is_attack_possible(self.map)
                if spell != False:
                    target = self.find_player_by_position(spell[1])
                    if self.spellActionApp(char, target, spell[0]) == False:
                        break
                else: break

            char.resetPA()
            char.clearSpells()
            
            # End
            self.endTurn()
            time.sleep(TIME)


        self.turn += 1



            
