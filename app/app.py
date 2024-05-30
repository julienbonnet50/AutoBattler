import sys
sys.dont_write_bytecode = True
import time
from types import NoneType
from app.Waves.wave import Wave
from app.Conf.conf import *
from app.Buffs.buffChoicer import *
import pygame
import os

# get the directory of this file
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

class App:
    def __init__(self, ally, wave, buffPools):
        pygame.init()

        self.turn = 1
        self.map = wave.map
        self.characters = wave.characters.append(ally)
        self.ennemiesAlive = None
        self.alliesAlive = None
        self.game_window = None
        self.buffSelected = buffPools

        self.initUi()

        self.buffChoicer = BuffChoicer(self.buffSelected,WIDTH, HEIGHT)
    
        self.orderChars()


    def initUi(self):
        # Get icon
        iconPath = os.path.join(sourceFileDir, 'assets', 'iconAutoBattler.png')
        programIcon = pygame.image.load(iconPath)
        pygame.display.set_icon(programIcon)

        # Initialise game window
        pygame.display.set_caption('AutoBattler')
        self.game_window  = pygame.display.set_mode((WIDTH, HEIGHT))

    # UI + Console prints

    def placeInformation(self, font, x, y, text, color, bold):
        info_surface = font.render(
            f'{text}', bold, color
        )
        info_rect = info_surface.get_rect()
        info_rect.midtop = (x, y)
        self.game_window.blit(info_surface, info_rect)

    def printStats(self):
        count_ally = 0
        count_ennemie = 0
        for char in self.characters:
            char.printStats()
            title_font = pygame.font.SysFont(TIMES_NEW_ROMAN, 22,  True)
            core_font = pygame.font.SysFont(TIMES_NEW_ROMAN, 16)
           
            if char.team == "ally":
                self.placeInformation(title_font, WIDTH/2 + 125, HEIGHT/2, 'Ally stats', HAPPY_BLUE, True)
                self.placeInformation(core_font, WIDTH/2 + 130, (count_ally * 82) + HEIGHT/2 + 42, f'Name : {char.name}', HAPPY_BLUE, True)
                self.placeInformation(core_font, WIDTH/2 + 115, (count_ally * 82) + HEIGHT/2 + 62, f'HP : {char.hp}', HAPPY_BLUE, True)
                self.placeInformation(core_font, WIDTH/2 + 135, (count_ally * 82) + HEIGHT/2 + 82, f'Position : ({char.position_x}, {char.position_y})', HAPPY_BLUE, True)
                count_ally += 1
            else:
                self.placeInformation(title_font, WIDTH/2 + +150,SPACE_SIZE, 'Ennemies stats', VIOLET, True)
                self.placeInformation(core_font, WIDTH/2 + 130, (count_ennemie * 82) + SPACE_SIZE + 42, f'Name : {char.name}', VIOLET, True)
                self.placeInformation(core_font, WIDTH/2 + 115, (count_ennemie * 82) + SPACE_SIZE + 62, f'HP : {char.hp}', VIOLET, True)
                self.placeInformation(core_font, WIDTH/2 + 135, (count_ennemie * 82) + SPACE_SIZE + 82, f'Position : ({char.position_x}, {char.position_y})', VIOLET, True)
                count_ennemie += 1


    def displayTurn(self):
        score_font = pygame.font.SysFont(TIMES_NEW_ROMAN, 15)
        score_surface = score_font.render('Turn : ' + str(self.turn), True, WHITE)
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

    def displayGrid(self):
        for x in range(0, self.map.mapSize * SPACE_SIZE, SPACE_SIZE):
            for y in range(0, SPACE_SIZE * self.map.mapSize, SPACE_SIZE):
                rect = pygame.Rect(x + SPACE_SIZE, y + SPACE_SIZE, SPACE_SIZE, SPACE_SIZE)
                pygame.draw.rect(self.game_window, WHITE, rect, 1)

    # Wave :
    
    def selectAllyBuffed(self):
        allyBuffed = []
        for char in self.characters:
            if char.team == 'ally':
                allyBuffed.append(char)  
        return allyBuffed      
    
    def game_over(self):
        my_font = pygame.font.SysFont(TIMES_NEW_ROMAN, 20)
        self.placeInformation(my_font,WIDTH/2, HEIGHT/4, f'Game turn : ' + str(self.turn), RED, True)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        quit()

    def game_win(self):
        my_font = pygame.font.SysFont(TIMES_NEW_ROMAN, 20)

        self.placeInformation(my_font, WIDTH/2, HEIGHT/4, f'GOOD GAME !!! done in ' + str(self.turn) + ' turn', GREEN, True)

    def getGameState(self):
        for char in self.characters:
            if char.hp < 0:
                print(f'\n{char.name} is dead !')
                self.characters.remove(char)
                self.ennemiesAlive -= 1

            if self.alliesAlive == 0:
                self.game_over()

            if self.ennemiesAlive == 0:
                self.game_win()

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
    
    # Buff

    def buffChoice(self):
        if DEBUG_BUFF == True:
            print(f'Starting buff choice')
        
        self.buffChoicer.displayBuffChoice(self.game_window, False)
        buffChosenIndex = self.buffChoicer.choseBuff(self.game_window)
    
    def applyBuff(self, indexBuff):
        buffChosen = self.buffSelected[indexBuff]
        for char in self.characters:
            if char.team == buffChosen.attribution:
                if buffChosen.name.contains('damage-value'):
                    char_enhanced = char
                    char_enhanced.damage += buffChosen.damage
                    self.characters.delete(char)
                    self.characters.append(char_enhanced)
                elif buffChosen.name.contains('damage-ratio'):
                    char_enhanced = char
                    char_enhanced.damage = char_enhanced.damage * buffChosen.ratio
                    self.characters.delete(char)
                    self.characters.append(char_enhanced)
        
        self.orderChars()

    # Turns
    
    def orderChars(self):
        if DEBUG_BUFF == True:
            print(f'Ordering characters')
        self.characters = self.characters.sort(key=lambda character: character.speed, reverse=True)
        
    def startTurn(self):
        self.game_window.fill(BLACK)
        self.displayGrid()
        self.displayChar()
                
    def endTurn(self):
        self.getGameState()
        self.printStats()
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
        self.map.display()

    def doTurn(self):
        for char in self.characters:
            # Start
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
                    if self.spellActionApp(char, target, spell[0]) == False:
                        break
                else: break

            char.resetPA()
            char.clearSpells()
            
            # End
            self.endTurn()


        time.sleep(TIME)
        self.turn += 1



            
