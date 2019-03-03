from collections import namedtuple
import string,re

OffsetCoord = namedtuple("OffsetCoord", "col, row")
odd_q = -1
def literal_to_coord(s):
    ASCII_List = string.ascii_uppercase
    col = int(re.search(r'\d+', s).group())+odd_q
    row = ASCII_List.index(s[0])
    return OffsetCoord(col, row)

#test
print("A1: ",literal_to_coord('A1'))
print('B2: ',literal_to_coord('B2'))
print('N10: ',literal_to_coord('N10'))