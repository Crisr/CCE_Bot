from collections import namedtuple
import string,re
import numpy as np
# map hexes in odd_q configuration https://www.redblobgames.com/grids/hexagons/#coordinates

OffsetCoord = namedtuple("OffsetCoord", "col, row")

def literal_to_coord(s):
    odd_q = -1
    ASCII_List = string.ascii_uppercase
    col = int(re.search(r'\d+', s).group())+odd_q
    row = ASCII_List.index(s[0])
    return OffsetCoord(col, row)

def coords_to_literal(OffsetCoord):
    if OffsetCoord == False: 
        return 'Coords out of bounds'
    ASCII_List = string.ascii_uppercase
    col = ASCII_List[OffsetCoord.col]
    row = str(OffsetCoord.row+1)
    # if (OffsetCoord.row % 2) == 0:
    #     print("{0} is Even".format(num))
    return col+row

class CCE_Map:
    def __init__(self, data, scenario, bot_side):
        self.xls_data = data
        self.scenario = scenario #panda Series!
        self.bot_side = bot_side
        test = data['Maps'].loc[data['Maps']['name']==scenario['Maps'][0]]
        # print(test) #selects row in Maps sheet where Id = map name
        self.map = {
                    'name':scenario['Maps'][0],
                    'col':test.loc[0,'col'],
                    'row':test.loc[0,'row']}   
        self.map['cells_coords']=[[OffsetCoord(x,y) for x in range(self.map['col'])] for y in range(self.map['row'])]
        self.map['cells_names']=[[coords_to_literal(OffsetCoord(x,y)) for x in range(self.map['col'])] for y in range(self.map['row'])]
        self.hex_edges=['E3','E2','E1','E6','E5','E4'] # Edge 1 on top and then clockwise
        self.oddq_directions = [
        [(1,  0), (1, -1),  (0, -1), 
         (-1, -1), (-1,  0), (0, 1)],
        
        [(1, 1), (1,  0), (0, -1), 
        (-1,  0), (-1, 1), (0, 1)]
        ]
        pass

    def get_neighboor(self, OffCoord, direction): # direction = hex_edges value!
        parity = OffCoord.col & 1
        ind = self.hex_edges.index(direction)
        dir = self.oddq_directions[parity][ind]
        #check boundries, return False if out of bounds
        if ((OffCoord.col + dir[0]) > self.map['col']) or ((OffCoord.col + dir[0]) < 0): 
            return False
        if ((OffCoord.row + dir[1]) > self.map['row']) or ((OffCoord.row + dir[1]) < 0): 
            return False
        return OffsetCoord(OffCoord.col + dir[0], OffCoord.row + dir[1])
    
    def DrawMap(self):
        pass



#test
# print("A1: ",literal_to_coord('A1'))
# print('B2: ',literal_to_coord('B2'))
# print('N10: ',literal_to_coord('N10'))
# print(coords_to_literal(OffsetCoord(2, 2)))