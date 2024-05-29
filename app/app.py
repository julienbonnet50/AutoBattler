import sys
sys.dont_write_bytecode = True
import time
from types import NoneType
from app.Constants.conf import *
import pygame

class App:
    def __init__(self, map, characters):
        self.turn = 1
        self.map = map
        self.characters = characters
        self.deadChar = False
        self.game_window = None
        
        self.initUi()


    def initUi(self):
        # Initialising pygame
        pygame.init()

        # Initialise game window
        pygame.display.set_caption('AutoBattler')
        self.game_window = game_window = pygame.display.set_mode((WIDTH, HEIGHT))

    def placeInformation(self, font, x, y, text, color, bold):
        info_surface = font.render(
            f'{text}', bold, color
        )
        info_rect = info_surface.get_rect()
        info_rect.midtop = (x, y)
        self.game_window.blit(info_surface, info_rect)

    def printStats(self):
        for char in self.characters:
            char.printStats()
            title_font = pygame.font.SysFont(FONT, 22,  True)
            core_font = pygame.font.SysFont(FONT, 16)
           
            if char.team == "ally":
                self.placeInformation(title_font, WIDTH/2 + 125, HEIGHT/2, 'Ally stats', HAPPY_BLUE, True)
            else:
                self.placeInformation(title_font, WIDTH/2 + 150, SPACE_SIZE, 'Ennemies stats', VIOLET, True)

    def displayTurn(self):
        score_font = pygame.font.SysFont(FONT, 15)
        score_surface = score_font.render('Turn : ' + str(self.turn), True, WHITE)
        score_rect = score_surface.get_rect()
        self.game_window.blit(score_surface, score_rect)

    def displayChar(self):
        for char in self.characters:
            CHAR_COLOR = char.resolveColor()
            ratio = char.hp  / char.max_hp
            if DEBUG_MODE_MOVE == True:
                print(f'Trying to create rectangle for body at pos ({char.position_x}, {char.position_y})')

            pygame.draw.rect(self.game_window, CHAR_COLOR, pygame.Rect(
		    (char.position_x ) * SPACE_SIZE + SPACE_SIZE, (char.position_y) * SPACE_SIZE + SPACE_SIZE, SPACE_SIZE, SPACE_SIZE))

            # Draw Health bar
            pygame.draw.rect(self.game_window, RED, pygame.Rect(
                (char.position_x) * SPACE_SIZE + SPACE_SIZE - 10, (char.position_y) * SPACE_SIZE -10 + SPACE_SIZE, SPACE_SIZE + 20, 5 )
            )
            pygame.draw.rect(self.game_window, GREEN, pygame.Rect(
                (char.position_x) * SPACE_SIZE + SPACE_SIZE - 10, (char.position_y) * SPACE_SIZE - 10 + SPACE_SIZE, (SPACE_SIZE + 20) * ratio, 5 )
            )

    def displayGrid(self):
        for x in range(0, self.map.mapSize * SPACE_SIZE, SPACE_SIZE):
            for y in range(0, SPACE_SIZE * self.map.mapSize, SPACE_SIZE):
                rect = pygame.Rect(x + SPACE_SIZE, y + SPACE_SIZE, SPACE_SIZE, SPACE_SIZE)
                pygame.draw.rect(self.game_window, WHITE, rect, 1)
            
    def game_over(self):
        my_font = pygame.font.SysFont(FONT, 20)

        game_over_surface = my_font.render(
            'Game turn : ' + str(self.turn), True, WHITE)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (WIDTH/2, HEIGHT/4)
        self.game_window.blit(game_over_surface, game_over_rect)

        for char in self.characters:
            if char.hp < 0:
                game_over_msg1_surface = my_font.render(
                    f'Game is done, {char.name} is dead !', True, WHITE
                )
                game_over_msg1_rect = game_over_msg1_surface.get_rect()
                game_over_msg1_rect.midtop = (WIDTH/2, HEIGHT/2)
                self.game_window.blit(game_over_msg1_surface, game_over_msg1_rect)

        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        quit()

    def startTurn(self):
        self.game_window.fill(BLACK)
        self.displayGrid()
        self.displayChar()
                
    def endTurn(self):
        if self.deadChar == False:
            self.printStats()
            self.map.display()
            print('\n')

    def checkDeadChar(self):
        for char in self.characters:
            if char.hp < 0:
                print(f'\nGame is done, {char.name} is dead !')
                self.game_over()
                self.deadChar = True
    
    def firstTurn(self):

        print("Turn : 0")
        for char in self.characters:
            self.map.placeCharacters(char)
            if DEBUG_MODE_MOVE == True:
                print(f'Placed {char.name} at ({char.position_x}, {char.position_y})')

        self.map.display()

    def find_player_by_position(self, position):
        positionCharName = self.map.map[position[0]][position[1]]

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
            print("No target found")
            return False
        
        if target.team  == caster.team:
            print("Target got the same team as caster")
            return False

        caster.current_pa -= spell.cost
        target.hp -= spell.damage

        print(f"{caster.name} casts {spell.name} on {target.name} for {spell.damage} damage!")
        return True
    

    def doTurn(self):
        if self.deadChar == True:
            return False

        for char in self.characters:
            # Start
            if char.checkIfAlive() == False:
                break
            # Movements
            self.startTurn()
            char.clear_moves()
            char.get_possible_moves(char.position_x, char.position_y, char.pm, self.map.mapSize)

            if DEBUG_MODE_MOVE == True:
                print(f'Possible moves : {char.possible_moves}')

            move_evaluated = char.evaluate_moves(self.map)
            char.move(move_evaluated)
            self.map.placeCharacters(char)
            self.map.resetMap(self.characters)

            # Spells 
            while char.checkPA() == True:
                spell = char.is_attack_possible(self.map)
                if spell != False:
                    target = self.find_player_by_position(spell[1])
                    self.spellActionApp(char, target, spell[0])
                else: break

            char.resetPA()
            char.clearSpells()
            
            # End
            self.checkDeadChar()

            self.endTurn()
            self.displayTurn()
            pygame.display.update()

        time.sleep(TIME)
        self.turn += 1



            
