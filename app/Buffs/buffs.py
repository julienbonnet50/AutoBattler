from app.Constants.initBuffs import *
from app.Buffs.buff import *

class Buffs:
    def __init__(self):
        self.buffsList = []
        self.addClassicBuffs()

    
    def addClassicBuffs(self):
        print(f'Append buff to buffList')
        self.buffsList.append(Buff(BUFF_DAMAGE_VALUE_NAME, 
                                   BUFF_DAMAGE_VALUE_DESC,
                                   BUFF_DAMAGE_VALUE_VALUE, 
                                   BUFF_DAMAGE_VALUE_RATIO, 
                                   BUFF_DAMAGE_VALUE_ATTRIBUTION, 
                                   0))
        
        self.buffsList.append(Buff(BUFF_DAMAGE_RATIO_NAME,
                                   BUFF_DAMAGE_RATIO_DESC,
                                   BUFF_DAMAGE_RATIO_VALUE, 
                                   BUFF_DAMAGE_RATIO_RATIO, 
                                   BUFF_DAMAGE_RATIO_ATTRIBUTION, 
                                   0))
        
        self.buffsList.append(Buff(BUFF_RANGE_NAME, 
                                   BUFF_RANGE_DESC,
                                   BUFF_RANGE_VALUE, 
                                   BUFF_RANGE_VALUE_RATIO, 
                                   BUFF_DAMAGE_RATIO_ATTRIBUTION, 
                                   0))
        

        