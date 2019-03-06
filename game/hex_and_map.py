from collections import namedtuple
import string,re
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
        print(scenario['Maps'][0])
        self.map = [[{'id':str(a)+str(b)} for a in range(5)] for b in range(6)]
    
    def DrawMap(self):
        pass

    

#test
print("A1: ",literal_to_coord('A1'))
print('B2: ',literal_to_coord('B2'))
print('N10: ',literal_to_coord('N10'))
print(coords_to_literal(OffsetCoord(2, 2)))