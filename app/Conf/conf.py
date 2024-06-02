import pygame
import os

sourceFileDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pygame.font.init() 

# LOG
DEBUG_BUFF = False
DEBUG_MAP = False
DEBUG_CHAR = False
DEBUG_MODE_MOVE = True
DEBUG_MODE_SPELL = True
DEBUG_MODE_SPELL_DEEP = False

# WINDOWS :
WIDTH = 900
HEIGHT = 550
SPACE_SIZE = 20

# TURN
TIME = 0.3

# COLORS
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
VIOLET = pygame.Color(102, 0, 102)
HAPPY_BLUE = pygame.Color(0, 153, 255)



# FONT
PIXEL_FONT_PATH = os.path.join(sourceFileDir, 'assets', 'font', 'pixel_font.ttf')

PIXEL_FONT_28 = pygame.font.Font(PIXEL_FONT_PATH, 28)

PIXEL_FONT_22 = pygame.font.Font(PIXEL_FONT_PATH, 22)
PIXEL_FONT_16 = pygame.font.Font(PIXEL_FONT_PATH, 16)
PIXEL_FONT_15 = pygame.font.Font(PIXEL_FONT_PATH, 15)



