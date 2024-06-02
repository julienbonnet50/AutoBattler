from app.Buffs.buff import *
from app.Conf.conf import *
from utils.csv_loader import *
import os

class Buffs:
    def __init__(self):
        self.buffsList = []
        self.addClassicBuffs()
        
    
    def addClassicBuffs(self):
        sourceFileDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pathBuffData = os.path.join(sourceFileDir, 'Data', 'buff.csv')
        dataBuff = load_csv(pathBuffData)

        for buff in dataBuff:
            
            buffMapping = Buff(name=buff["name"],
                               description=buff["description"],
                               value=int(buff["value"]),
                               attribution=buff["attribution"],
                               rarity=int(buff["rarity"]),
                               ratio=float(buff["ratio"]))
            
            self.buffsList.append(buffMapping)
            if DEBUG_BUFF == True:
                print(f'Append buff {buffMapping.name} to buffList')
            

        