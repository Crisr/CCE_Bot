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
        dt = np.dtype([('cellName', np.unicode_, 4)])        
        self.map['cells']=np.fromiter((str(a)+str(b) for a in range(self.map['col']) for b in range(self.map['row'])),dtype="S4")
        pass
    
    def DrawMap(self):
        pass



#test
print("A1: ",literal_to_coord('A1'))
print('B2: ',literal_to_coord('B2'))
print('N10: ',literal_to_coord('N10'))
print(coords_to_literal(OffsetCoord(2, 2)))