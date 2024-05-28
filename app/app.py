from types import NoneType
from app.Constants.conf import *
import tkinter as tk
from tkinter import *

class App:
    def __init__(self, map, characters):
        self.turn = 1
        self.map = map
        self.characters = characters
        self.deadChar = False
        self.window = tk.Tk()
        self.window.title("AutoBattler")
        self.canvas = Canvas(self.window, bg=BACKGROUND, 
				height=HEIGHT, width=WIDTH) 
        
    def initWindows(self):
        print("Initiate windows")
        self.canvas.pack() 
    
        self.window.update()
        window_width = self.window.winfo_width() 
        window_height = self.window.winfo_height() 
        screen_width = self.window.winfo_screenwidth() 
        screen_height = self.window.winfo_screenheight() 

        x = int((screen_width/2) - (window_width/2)) 
        y = int((screen_height/2) - (window_height/2)) 

        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}") 
        
    def game_over(self): 
        self.canvas.delete(ALL) 
        self.canvas.create_text(self.canvas.winfo_width()/2, 
                        self.canvas.winfo_height()/3, 
                        font=('consolas', 70), 
                        text="GAME DONE", fill="red", 
                        tag="gameover") 
        
        text = f'Game duration : {self.turn}'
        self.canvas.create_text(self.canvas.winfo_width()/2, 
                        self.canvas.winfo_height()/1.4, 
                        font=('consolas', 40), 
                        text=text, fill="white") 
        
    
    def displayChar(self):
        for char in self.characters:
            print(f'Trying to create rectangle for body at pos ({char.position_x}, {char.position_y})')
            self.canvas.create_rectangle( 
                (char.position_x - 1) * SPACE_SIZE, (char.position_y - 1) * SPACE_SIZE, (char.position_x + 1) * SPACE_SIZE, 
                (char.position_y + 1) * SPACE_SIZE, fill=CHAR_COLOR)
                                 

    def printStats(self):
        if self.deadChar == False:
            for char in self.characters:
                char.printStats()
                
    def endTurn(self):
        if self.deadChar == False:
            self.printStats()
            self.map.display()
            self.displayChar()


    def checkDeadChar(self):
        for char in self.characters:
            if char.hp < 0:
                print(f'\nGame is done, {char.name} is dead !')
                self.deadChar = True
                self.game_over()
    
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

        target.hp -= spell.damage

        print(f"{caster.name} casts {spell.name} on {target.name} for {spell.damage} damage!")
        return True
    

    def doTurn(self):
        if self.deadChar == True:
            return False
        
        self.canvas.delete(ALL)
        for char in self.characters:
            # Start
            if char.checkIfAlive() == False:
                break

            # Movements
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
            self.turn += 1
            self.window.after(TIME, self.doTurn)

            
