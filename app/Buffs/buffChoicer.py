import pygame
from app.Conf.conf import *
from utils.display.draw import *
import time


class BuffChoicer():
    def __init__(self, buffSelected, width, height):
        self.buffSelected = buffSelected
        self.width = width
        self.height = height
        self.buttons = self.addButtons()

    def resolveBuffFontColor(self, buff):
        if buff.rarity == 0:
            return (255, 255, 255), "classic"
        if buff.rarity == 1:
            return (3, 104, 238), "rare"
        if buff.rarity == 2:
            return (214, 55, 219), "epic"

    def addButtons(self):
        buttons = []
        count = 0
        for buff in self.buffSelected:
            if DEBUG_BUFF == True:
                print(f'Created button for {buff.name}')
            color, text = self.resolveBuffFontColor(buff)
            buttons.append({f"index": count,"name": f"{buff.name}", "desc": f"{buff.description}", "color": color, "pos_x": (SPACE_SIZE) + (count*(150 + SPACE_SIZE)), "pos_y": 100, "size": (150, 200), "text": text})
            count  += 1 

        return buttons

    def cleanBuffDisplay(self, game_window):
        allBuffRect = pygame.Rect(SPACE_SIZE, SPACE_SIZE, WIDTH, 200)
        pygame.draw.rect(game_window, BLACK, allBuffRect, 1)
        pygame.display.update(allBuffRect)

    def displayBuffChoice(self, game_window, isBuffHovered, indexBuffHovered = -1):
        time.sleep(0.05)
        self.cleanBuffDisplay(game_window)
        for button in self.buttons:
            buffHovered = pygame.Rect(button['pos_x']-7, button['pos_y']-7, button['size'][0]+14, button['size'][1]+14)
            if isBuffHovered == True and button['index'] == indexBuffHovered:
                hoverColor = GREEN
            else:
                hoverColor = BLACK

            pygame.draw.rect(game_window, hoverColor, buffHovered, 1)
            pygame.display.update(buffHovered)

            buttonColor = pygame.Color(button['color'])

            textRect = pygame.Rect(button['pos_x'], button['pos_y'], button['size'][0], button['size'][1])
            textRectText = pygame.Rect(button['pos_x'], button['pos_y'] + 40, button['size'][0], button['size'][1])

            pygame.draw.rect(game_window, buttonColor, textRect, 1)
            drawText(surface=game_window,
                        text=button['desc'],
                        color=button['color'],
                        rect=textRectText,
                        font=PIXEL_FONT_22,
                        align=2,
                        aa=True)
            
            # define the textRect for each button and store it in the button dictionary
            button['rect'] = pygame.Rect(button['pos_x'], button['pos_y'] + 150, button['size'][0], button['size'][1])
            drawText(surface=game_window,
                            text=button['text'],
                            color=button['color'],
                            rect=button['rect'],
                            font=PIXEL_FONT_16,
                            align=2,
                            aa=True)
            
            pygame.display.update(buffHovered)
            
    def choseBuff(self, game_window):
        pygame.event.clear()
        while True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for button in self.buttons:
                rectHovered = pygame.Rect(button['pos_x'], button['pos_y'], button['size'][0], button['size'][1])
                if rectHovered.collidepoint(mouse_x, mouse_y):
                    self.displayBuffChoice(game_window, True, button['index'])

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if the mouse click occurred within the bounds of a button
                    print(f'Click at {event.pos}')
                    for button in self.buttons:
                        textRect = pygame.Rect(button['pos_x'], button['pos_y'], button['size'][0], button['size'][1])
                        pygame.display.update()
                        if textRect.collidepoint(event.pos):
                            # execute the button's action
                            for i in range (0, len(self.buttons)):
                                if button['index'] == i:
                                    if DEBUG_BUFF == True:
                                        print(f'Buff number {i} selected')
                                    return i
                                
    def applyBuff(self, indexBuff, characters):
        buffChosen = self.buffSelected[indexBuff]
        for char in characters:
            if char.team == buffChosen.attribution:
                if 'damage-value' in buffChosen.name:
                    char_enhanced = char
                    char_enhanced.damage += buffChosen.value
                    characters.remove(char)
                    characters.append(char_enhanced)
                elif 'damage-ratio' in buffChosen.name:
                    char_enhanced = char
                    char_enhanced.damage = char_enhanced.damage * buffChosen.ratio
                    characters.remove(char)
                    characters.append(char_enhanced)
                elif 'hp-value' in buffChosen.name:
                    char_enhanced = char
                    char_enhanced.max_hp += buffChosen.value
                    char_enhanced.hp += buffChosen.value
                    characters.remove(char)
                    characters.append(char_enhanced)
                elif 'speed-value' in buffChosen.name:
                    char_enhanced = char
                    char_enhanced.speed += buffChosen.value
                    characters.remove(char)
                    characters.append(char_enhanced)
                elif 'speed-ratio' in buffChosen.name:
                    char_enhanced = char
                    char_enhanced.speed += char_enhanced.speed * buffChosen.ratio 
                    characters.remove(char)
                    characters.append(char_enhanced)
                elif 'pa-value' in buffChosen.name:
                    char_enhanced = char
                    char_enhanced.pa += buffChosen.value
                    characters.remove(char)
                    characters.append(char_enhanced)
                    
        return characters

