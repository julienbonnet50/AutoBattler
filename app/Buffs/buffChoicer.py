import pygame
import math
from app.Conf.conf import *

class BuffChoicer():
    def __init__(self, buffSelected, width, height):
        self.buffSelected = buffSelected
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(FRANKLIN, 35)
        self.fontColor = pygame.Color(255, 255, 255)
        self.buttons = self.addButtons()

    def drawText(self, surface, text, color, rect, font, align, aa=False, bkg=None):
        lineSpacing = -2
        spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

        listOfWords = text.split(" ")
        if bkg:
            imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
            for image in imageList: image.set_colorkey(bkg)
        else:
            imageList = [font.render(word, aa, color) for word in listOfWords]

        maxLen = rect[2]
        lineLenList = [0]
        lineList = [[]]
        for image in imageList:
            width = image.get_width()
            lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
            if len(lineList[-1]) == 0 or lineLen <= maxLen:
                lineLenList[-1] += width
                lineList[-1].append(image)
            else:
                lineLenList.append(width)
                lineList.append([image])

        lineBottom = rect[1]
        lastLine = 0
        for lineLen, lineImages in zip(lineLenList, lineList):
            lineLeft = rect[0]
            if align == 1:
                lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages)-1)
            elif align == 2:
                lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages)-1)) // 2
            elif align == 3 and len(lineImages) > 1:
                spaceWidth = (rect[2] - lineLen) // (len(lineImages)-1)
            if lineBottom + fontHeight > rect[1] + rect[3]:
                break
            lastLine += 1
            for i, image in enumerate(lineImages):
                x, y = lineLeft + i*spaceWidth, lineBottom
                surface.blit(image, (round(x), y))
                lineLeft += image.get_width() 
            lineBottom += fontHeight + lineSpacing

        if lastLine < len(lineList):
            drawWords = sum([len(lineList[i]) for i in range(lastLine)])
            remainingText = ""
            for text in listOfWords[drawWords:]: remainingText += text + " "
            return remainingText
        return ""

    def resolveBuffFontColor(self, buff):
        if buff.rarity == 0:
            return (255, 255, 255)
        if buff.rarity == 1:
            return (3, 104, 238)

    def addButtons(self):
        buttons = []
        count = 0
        for buff in self.buffSelected:
            if DEBUG_BUFF == True:
                print(f'Created button for {buff.name}')
            buttons.append({f"index": {count},"name": f"{buff.name}", "desc": f"{buff.description}", "color": self.resolveBuffFontColor(buff), "pos_x": (SPACE_SIZE) + (count*(150 + SPACE_SIZE)), "pos_y": 100, "size": (150, 200)})
            count  += 1 

        return buttons

    def displayAndGetBuff(self, game_window):
        running = True
        while running:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # check if the mouse click occurred within the bounds of a button
                    for button in self.buttons:
                        if button['rect'].collidepoint(event.pos):
                            # execute the button's action
                            if button['index'] == 0:
                                if DEBUG_BUFF == True:
                                    print('Buff 1 selected')
                                return button['index']
                            elif button['index'] == 1:
                                if DEBUG_BUFF == True:
                                    print('Button 2 selected')
                                return button['index']
                            elif button['index'] == 2:
                                if DEBUG_BUFF == True:
                                    print('Button 3 selected')
                                return button['index']

            # clear the window
            game_window.fill((0, 0, 0))

            # draw the buttons
            for button in self.buttons:
                # define the textRect for each button and store it in the button dictionary
                button['rect'] = pygame.Rect(button['pos_x'], button['pos_y'] + 150, button['size'][0], button['size'][1])
                self.drawText(surface=game_window,
                              text="Take it",
                              color=button['color'],
                              rect=button['rect'],
                              font=self.font,
                              align=2,
                              aa=True)

                buttonColor = pygame.Color(button['color'])

                textRect = pygame.Rect(button['pos_x'], button['pos_y'], button['size'][0], button['size'][1])
                pygame.draw.rect(game_window, buttonColor, textRect, 1)
                self.drawText(surface=game_window,
                            text=button['desc'],
                            color=button['color'],
                            rect=textRect,
                            font=self.font,
                            align=2,
                            aa=True)

            pygame.display.update()
                             
    
