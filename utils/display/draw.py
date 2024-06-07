import pygame
from app.Conf.conf import *

def drawText(surface, text, color, rect, font, align, aa=False, bkg=None):
    '''
    textAlign  = 0
    textAlign Right = 1
    textAlign Center = 2
    textAlign Block = 3
    '''

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


def placeInformation(game_window, font, x, y, width, height, text, color, bold):
    infoRect = pygame.Rect(x, y, width, height)

    drawText(surface=game_window,
                text=text,
                color=color,
                rect=infoRect,
                font=font,
                align=0,
                aa=True)
    

def printStats(game_window, characters, ennemiesAlive, alliesAlive):
    count_ally = 0
    count_ennemie = 0
    title_font = PIXEL_FONT_22
    core_font = PIXEL_FONT_16
    initial_width = 120
    width_space = initial_width
    name_space = 60
    HP_space = 50
    damage_space = 80
    position_space = 80

    if DEBUG_CHAR == True:
        print(f'Ennemies alive : {ennemiesAlive}')
        print(f'Allies alive : {alliesAlive}')

    placeInformation(game_window, title_font, WIDTH/2 + width_space, HEIGHT/2, 180 , SPACE_SIZE + 20 , 'Ally stats', HAPPY_BLUE, True)
    placeInformation(game_window, title_font, WIDTH/2 + width_space, SPACE_SIZE, 250 , SPACE_SIZE + 20 ,'Ennemies stats', VIOLET, True)

    # TODO : if (ennemiesAlive < 5):

    for char in characters:
        width_space = initial_width
        if char.team == "ally" and count_ally < 2:

            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ally * 102) + HEIGHT/2 + 42, 150 , SPACE_SIZE , f'Name : ', HAPPY_BLUE, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + name_space, (count_ally * 102) + HEIGHT/2 + 42, 150 , SPACE_SIZE , f'{char.name}', WHITE, False)
            
            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ally * 102) + HEIGHT/2 + 62, 150 , SPACE_SIZE , f'HP : ', HAPPY_BLUE, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + HP_space, (count_ally * 102) + HEIGHT/2 + 62, 150 , SPACE_SIZE , f'{char.hp}', WHITE, False)

            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ally * 102) + HEIGHT/2 + 82, 150 , SPACE_SIZE , f'Damages : ', HAPPY_BLUE, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + damage_space, (count_ally * 102) + HEIGHT/2 + 82, 150 , SPACE_SIZE , f'{char.damage}', WHITE, False)

            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ally * 102) + HEIGHT/2 + 102, 150 , SPACE_SIZE , f'Position : ', HAPPY_BLUE, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + position_space, (count_ally * 102) + HEIGHT/2 + 102, 200 , SPACE_SIZE , f'({char.position_x}, {char.position_y})', WHITE, False)
            count_ally +=  1

        if char.team == "ally" and 4 > count_ally > 1:
            width_space = initial_width + 150

            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ally * 102) + HEIGHT/2 + 42, 150 , SPACE_SIZE , f'Name : ', HAPPY_BLUE, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + name_space, (count_ally * 102) + HEIGHT/2 + 42, 150 , SPACE_SIZE , f'{char.name}', WHITE, False)
            
            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ally * 102) + HEIGHT/2 + 62, 150 , SPACE_SIZE , f'HP : ', HAPPY_BLUE, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + HP_space, (count_ally * 102) + HEIGHT/2 + 62 + (20 * count_ally), 150 , SPACE_SIZE , f'{char.hp}', WHITE, False)

            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ally * 102) + HEIGHT/2 + 82 + (40 * count_ally), 150 , SPACE_SIZE , f'Damages : ', HAPPY_BLUE, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + damage_space, (count_ally * 102) + HEIGHT/2 + 82 + (40 * count_ally), 150 , SPACE_SIZE , f'{char.damage}', WHITE, False)
            
            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ally * 102) + HEIGHT/2 + 102 + (60 * count_ally), 150 , SPACE_SIZE , f'Position : ', HAPPY_BLUE, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + position_space, (count_ally * 102) + HEIGHT/2 + 102 + (60 * count_ally), 200 , SPACE_SIZE , f'({char.position_x}, {char.position_y})', WHITE, False)
            count_ally +=  1

        elif char.team == "ennemies" and count_ennemie < 2:
            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ennemie * 102) + SPACE_SIZE + 42, 150 , SPACE_SIZE , f'Name : ', VIOLET, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + name_space, (count_ennemie * 102) + SPACE_SIZE + 42, 150 , SPACE_SIZE , f'{char.name}', WHITE, False)

            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ennemie * 102) + SPACE_SIZE + 62, 150 , SPACE_SIZE , f'HP : ', VIOLET, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + HP_space, (count_ennemie * 102) + SPACE_SIZE + 62, 150 , SPACE_SIZE , f'{char.hp}', WHITE, False)

            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ennemie * 102) + SPACE_SIZE + 82, 150 , SPACE_SIZE , f'Damages : ', VIOLET, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + damage_space, (count_ennemie * 102) + SPACE_SIZE + 82, 150 , SPACE_SIZE , f'{char.damage}', WHITE, False)

            placeInformation(game_window, core_font, WIDTH/2 + width_space, (count_ennemie * 102) + SPACE_SIZE + 102, 150 , SPACE_SIZE , f'Position : ', VIOLET, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + position_space, (count_ennemie * 102) + SPACE_SIZE + 102, 200 , SPACE_SIZE , f'({char.position_x}, {char.position_y})', WHITE, False)

            count_ennemie += 1

        elif char.team == "ennemies" and  4 > count_ennemie > 1 :
            width_space = initial_width + 150

            placeInformation(game_window, core_font, WIDTH/2 + width_space, ((count_ennemie - 2) * 102) + SPACE_SIZE + 42, 150 , SPACE_SIZE , f'Name : ', VIOLET, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + name_space, ((count_ennemie - 2) * 102) + SPACE_SIZE + 42, 150 , SPACE_SIZE , f'{char.name}', WHITE, False)

            placeInformation(game_window, core_font, WIDTH/2 + width_space, ((count_ennemie - 2) * 102) + SPACE_SIZE + 62, 150 , SPACE_SIZE , f'HP : ', VIOLET, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + HP_space, ((count_ennemie - 2) * 102) + SPACE_SIZE + 62, 150 , SPACE_SIZE , f'{char.hp}', WHITE, False)

            placeInformation(game_window, core_font, WIDTH/2 + width_space, ((count_ennemie - 2) * 102) + SPACE_SIZE + 82, 150 , SPACE_SIZE , f'Damages : ', VIOLET, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + damage_space, ((count_ennemie - 2) * 102) + SPACE_SIZE + 82, 150 , SPACE_SIZE , f'{char.damage}', WHITE, False)

            placeInformation(game_window, core_font, WIDTH/2 + width_space, ((count_ennemie - 2) * 102) + SPACE_SIZE + 102, 150 , SPACE_SIZE , f'Position : ', VIOLET, False)
            placeInformation(game_window, core_font, WIDTH/2 + width_space + position_space, ((count_ennemie - 2) * 102) + SPACE_SIZE + 102, 200 , SPACE_SIZE , f'({char.position_x}, {char.position_y})', WHITE, False)

            count_ennemie += 1

        # TODO : Add somethings for summons ? 