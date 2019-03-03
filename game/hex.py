from collections import namedtuple
import string

OffsetCoord = namedtuple("OffsetCoord", "col, row")
odd_q = -1
def literal_to_coord(s):
    ASCII_List = string.ascii_uppercase
    col = int(s[1])+odd_q
    row = ASCII_List.index(s[0])
    # row = h.r + (h.q + offset * (h.q & 1)) // 2
    return OffsetCoord(col, row)

#test
print(literal_to_coord('A1'))