import game.hex_and_map as hm
import logging
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style

style = Style.from_dict({
    'cinfo': '#ff0066 italic'
})

map_info = print_formatted_text

class Counter:
    def __init__(self, name_str):
        self.name = name_str
        self.hexpos = ()
        self.history = []

    def get_Name(self):
        return self.name

    def get_MapPos(self):
        return self.hexpos

    def set_MapPos(self, OffsetCoord): #OffsetCoord tuple
        self.hexpos = OffsetCoord
        self.history.append(OffsetCoord)
        map_info(HTML('Counter {} {}'.format(self.name, hm.coords_to_literal(OffsetCoord))),style=style)
    
    def undo(self):
        if len(self.history) == 0:
            logging.error('Counter {} undo history empty'.format(self.name))
            return "Error: Undo history empty!"
        self.set_MapPos(self.history.pop)
        return True

class CounterGroup:
    def __init__(self, counter_names_str_list):
        self.groupNames = counter_names_str_list

    def randomSetUp(self, validHexes_list): # 2D list of A1, A2.. B1, B2 hex names
        pass