
import csv
import os
from utils.csv_loader import *
from app.Conf.conf import *

class CharactersList:
    def __init__(self):
        # Spells
        self.spellsList
        self.charactersList

    def load_csv(self, file_path):
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    # Load buff 

    def loadBuffData(self):
        sourceFileDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pathCharData = os.path.join(sourceFileDir, 'Data', 'characters.csv')

        dataChar = load_csv(pathCharData)

        for char in dataChar:
            self.buffList.append(char)
            if  DEBUG_CHAR == True:
                print(f'Append char {char.name} to charList')
            


