import sys
sys.dont_write_bytecode = True
import pygame
import os
from app.Conf.conf import *
from app.Entity.allyTeam import *
from app.Waves.waves import *
from app.app import *

# get the directory of this file
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

class Menu:
    def __init__(self):
        pygame.init()
        self.game_window = None
        self.button_width, self.button_heigth = 150, 50
        self.font = PIXEL_FONT_28
        self.initUi()
    
    def initUi(self):
        # Get icon
        iconPath = os.path.join(sourceFileDir, 'assets', 'iconAutoBattler.png')
        programIcon = pygame.image.load(iconPath)
        pygame.display.set_icon(programIcon)

        # Initialise game window
        pygame.display.set_caption('AutoBattler')
        self.game_window  = pygame.display.set_mode((WIDTH, HEIGHT))

    # Create a function to start the game
    def start_game(self):
        self.run_pve_sewer(wavesList=Waves())
        print("Starting game...")

    # Create a function to quit the game
    def quit_game(self):
        pygame.quit()
        sys.exit()
            
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    # Main container function that holds the buttons and game functions
    def runMenu(self):
        click = False
        while True:
    
            self.game_window.fill((0,190,255))
            menuBackgroundPath = os.path.join(sourceFileDir, 'assets', 'menu' ,'menu_background.png')
            backgroundImage = pygame.image.load(menuBackgroundPath)
            self.game_window.blit(backgroundImage, (0, 0))

            
            self.draw_text('Main Menu', self.font, (0,0,0), self.game_window, WIDTH/2 - 25, 40)
    
            mx, my = pygame.mouse.get_pos()

            #creating buttons
            button_1 = pygame.Rect(WIDTH/2 - 50, HEIGHT/3 - 25, 200, 50)
            button_2 = pygame.Rect(WIDTH/2 - 50, HEIGHT/1.5 - 25, 200, 50)
            

            #defining functions when a certain button is pressed
            if button_1.collidepoint((mx, my)):
                if click:
                    self.start_game()
            if button_2.collidepoint((mx, my)):
                if click:
                    self.quit_game()
            pygame.draw.rect(self.game_window, (255, 0, 0), button_1)
            pygame.draw.rect(self.game_window, (255, 0, 0), button_2)
    
            #writing text on top of button
            self.draw_text('PLAY', self.font, (255,255,255), self.game_window, WIDTH/2 - 50 + 70, HEIGHT/3 - 10)
            self.draw_text('OPTIONS', self.font, (255,255,255), self.game_window, WIDTH/2 - 50 + 50 , HEIGHT/1.5 - 10)

            for event in pygame.event.get():
                if event.type == pygame.quit:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            
    # Start Sewer waves
    def run_pve_sewer(self, wavesList):
        allyTeam = AllyTeam(wavesList.charList)
        
        for i in range (0, len(wavesList.waves)):
            game = App(allyTeam.characters, wavesList.waves[i])
            game.firstTurn()
            while game.ennemiesAlive > 0:
                print("Turn : ", game.turn)
                game.doTurn()

            game.buffChoice()
            allyTeam.characters = game.selectAllyBuffed()

            time.sleep(3)
        

