from app.Conf.conf import *

class Spell:
    def __init__(self, id, name, range, damage, cost):
        self.id = id
        self.name = name
        self.range = range
        self.damage = damage
        self.cost = cost
        self.possible_attacks = []

    def clear_possible_attacks(self):
        self.possible_attacks = []

    def find_possible_attacks(self, map, player_position, player_name):
        # Extract the x and y values from the player's position
        player_x = player_position[0]
        player_y = player_position[1]

        if DEBUG_MODE_SPELL == True:
            print(f'Starting find possible attacks for {player_name} from position {player_position}')

        # Determine which cells are within the spell's range
        for x in range(max(0, player_x - self.range), min(map.mapSize, player_x + self.range + 1)):
            for y in range(max(0, player_y - self.range), min(map.mapSize, player_y + self.range + 1)):
                map_value = map.map[x][y]
                if abs(x - player_x) + abs(y - player_y) <= self.range:
                    if DEBUG_MODE_SPELL_DEEP == True:
                        print(f'Checking at ({x}, {y}) -> {map_value}')

                    # Check if the cell is occupied by an enemy character
                    if isinstance(map_value, (str)) and map_value != player_name:
                        if DEBUG_MODE_SPELL == True:
                            print(f'Found possible attacks for {player_name} at position ({x}, {y})')
                        
                        # Add the enemy character's position to the list of possible attacks
                        self.possible_attacks.append((x, y, map_value))

        def seq(self, dX,dY):
            a = self.gcd(dX,dY)
            if a > 1:
                bar = seq(dX//a, dY//a) # for int type, is actual division
                res = [a*bar[0], a*bar[1]]
                return res
            if (dX%2)==(dY%2)==1:
                bar = seq(dX//2, dY//2)
                res = [bar[0]+[dX%2]+bar[0], bar[1]+[dY%2]+bar[1]]
                return res
            elif (dY>1 and (dX%2)==1) or (dX>1 and (dY%2)==1):
                bar = seq(dX//2, dY//2) # one division is without remainder
                res = [bar[0]+[dX%2]+bar[0], bar[1]+[dY%2]+bar[1]]
                return res
            elif dX>dY:
                return [[(i+1)%2 for i in range(dX+dY)], [i%2 for i in range(dX+dY)]]
            return [[i%2 for i in range(dX+dY)], [(i+1)%2 for i in range(dX+dY)]]
    
    def sign(self, i):
        return -1 if i<0 else 1

    def visualise(self, map, vision_map, POS_PLAYER):
        possible_pos = []
        for i in range(len(map)):
            for j in range(len(map[i])):
                if self.isObstacle(map, (i,j)):
                    continue
                elif (i,j)==POS_PLAYER:
                    continue
                else :
                # Si renseigné, alors à porté
                    if vision_map[(i,j)]==0:
                        possible_pos.append((i,j))
                    if vision_map[(i,j)]==-1:
                        continue
                    if vision_map[(i,j)]==5:
                        continue
                # Sinon hors range
        return possible_pos

    def get_vision_map(self, map, pos, PO):
        dic = {pos:0}
        obstacles = []
        for i in range(1,PO+1):
            for j in range(PO+1-i):
                x = pos[0] + i
                y = pos[1] + j
                if x>=0 and x<len(map) and y>=0 and y<len(map[x]):
                    dic[(x,y)]=map[x][y]
                    if self.isObstacle(map,(x,y)):
                        obstacles.append((x,y))
                x = pos[0] - j
                y = pos[1] + i
                if x>=0 and x<len(map) and y>=0 and y<len(map[x]):
                    dic[(x,y)]=map[x][y]
                    if self.isObstacle(map,(x,y)):
                        obstacles.append((x,y))
                x = pos[0] - i
                y = pos[1] - j
                if x>=0 and x<len(map) and y>=0 and y<len(map[x]):
                    dic[(x,y)]=map[x][y]
                    if self.isObstacle(map,(x,y)):
                        obstacles.append((x,y))
                x = pos[0] + j
                y = pos[1] - i
                if x>=0 and x<len(map) and y>=0 and y<len(map[x]):
                    dic[(x,y)]=map[x][y]
                    if self.isObstacle(map,(x,y)):
                        obstacles.append((x,y))

        for obstacle in obstacles:
            # print("obstacle :",obstacle)
            if dic[obstacle]==2: # skip si déjà dans l'ombre d'un obstacle
                continue
            if obstacle==pos:
                continue # obstacle sur point de départ, on ignore (on pourrait aussi dire 0 vision)
            dX=obstacle[0]-pos[0]
            dXObstacle=dX
            dY=obstacle[1]-pos[1]
            dYObstacle=dY
            dXa = abs(dX)
            dYa = abs(dY)
            # print("(%s,%s)" % (dXa,dYa), end = " ")
            seqs_bord_obstacle_haut = self.seq(abs(2*(dXa-1) +1), 2*(dYa-(dXa==0)) +1)
            # print(" -> h seq(%s,%s)" % (abs(2*(dXa-1) +1), 2*(dYa-(dXa==0)) +1), end = " ")
            seqs_bord_obstacle_bas = self.seq(2*(dXa-(dYa==0)) +1, abs(2*(dYa-1)+1))
            # print("& b seq(%s,%s)" % (2*(dXa-(dYa==0)) +1, abs(2*(dYa-1)+1)))
            if False :
                if dYa==0:
                    seqs_bord_obstacle_haut = seqs_bord_obstacle_bas
                    print("  [correction] haut : seq(%s,%s)"% (2*(dXa-(dYa==0)) +1, dYa+((dYa+1)%2)))
                elif dXa==0 :
                    seqs_bord_obstacle_bas = seqs_bord_obstacle_haut
                    print("  [correction] bas : seq(%s,%s)"% (dXa+((dXa+1)%2), 2*(dYa-(dXa==0)) +1))

            # premier bord
            x=obstacle[0]
            y=obstacle[1]
            signX = self.sign(dX)
            signY = self.sign(dY)
            l = len(seqs_bord_obstacle_bas[0])
            dist = dXa+dYa
            a= 0 if (dXa!=dYa or dXa%2==0) else (dXa-1)//2# sauter moitié d'un cycle de déplacements pour obstacle en diagonale impaire
            border_1=[]
            while dist < PO:
                x += signX*seqs_bord_obstacle_bas[0][a%l]
                y += signY*seqs_bord_obstacle_bas[1][a%l]
                if False :
                    if x<0 or x>=len(map) or y<0 or y>=len(map[x]):
                        x -= signX*seqs_bord_obstacle_bas[0][a%l]
                        y -= signY*seqs_bord_obstacle_bas[1][a%l]
                        break
                dist += seqs_bord_obstacle_bas[0][a%l] + seqs_bord_obstacle_bas[1][a%l]
                a+=1
                border_1.append((x,y))
                dic[(x,y)] = -3
            corner_1 = (x,y)

            # deuxième bord
            x=obstacle[0]
            y=obstacle[1]
            signX = self.sign(dX) if dX!=0 else -1
            signY = self.sign(dY) if dY!=0 else -1
            l = len(seqs_bord_obstacle_haut[0])
            dist = dXa+dYa
            a= 0 if (dXa!=dYa or dXa%2==0) else (dXa-1)//2# sauter moitié d'un cycle de déplacements pour obstacle en diagonale impaire
            border_2=[]
            while dist < PO:
                x += signX*seqs_bord_obstacle_haut[0][a%l]
                y += signY*seqs_bord_obstacle_haut[1][a%l]
                if False:
                    if x<0 or x>=len(map) or y<0 or y>=len(map[x]):
                        x -= signX*seqs_bord_obstacle_haut[0][a%l]
                        y -= signY*seqs_bord_obstacle_haut[1][a%l]
                        break

                dist += seqs_bord_obstacle_haut[0][a%l] + seqs_bord_obstacle_haut[1][a%l]
                a+=1
                if dist <= PO:
                    border_2.append((x,y))
                    dic[(x,y)] = -2
            corner_2 = (x,y)

            # prolongement des bords
            # print(corner_1, corner_2, border_1, border_2)
            arc_limite_po=[]
            x,y = corner_1
            x2,y2 = corner_2

            TO=10;a=0
            if False :
                print(x,y, end=" ")
                xlim = max(min(x,len(map)-1), 0)
                ylim = max(min(y,len(map[xlim])-1), 0)
                print("->",xlim,ylim)
                dic[(xlim,ylim)]=5
            while (abs(x-x2)+abs(y-y2))>2 and a<TO:
                dX=x-pos[0]
                dy=y-pos[1]
                x+=-self.sign(dX)*(-1 if dXObstacle==0 else 1)
                y+=self.sign(dY)*(-1 if dYObstacle==0 else 1)
                # print(x,y)
                a +=1
                arc_limite_po.append((x,y))
            # print("Filling up")
            bord_sup_complet = arc_limite_po + ([] if dYObstacle==0 else border_1)
            # print(arc_limite_po, bord_sup_complet)
            for c in bord_sup_complet:
                # from red to grey is towards x=x_pos (else ignore)
                x,y=c
                dist=abs(pos[0]-x)+abs(pos[1]-y)
                content = dic[(x,y)] if (dist<=PO and (x>=0 and x<len(map) and y>=0 and y<len(map))) else 0
                TO=25; a=0
                while content!=-2 and (x,y)!=obstacle and a<TO: # count obstacle as part of opposite border
                    if dist<=PO and (x>=0 and x<len(map) and y>=0 and y<len(map)):
                        # print("+1 :(%s,%s)" % (x,y),dic[(x,y)]==content,end="  ")
                        #dic[(x,y)]=-1
                        True
                    x += self.sign(obstacle[0]-c[0])
                    dist=abs(pos[0]-x)+abs(pos[1]-y)
                    content = dic[(x,y)] if (dist<=PO and (x>0 and x<len(map) and y>0 and y<len(map))) else 0
                    a=a+1
                # print()
                #dic[c]=5
        return dic

