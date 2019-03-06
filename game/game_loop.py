import game.commandPattern as Cmd
import game.hex_and_map as hm


class Game:
    def __init__(self, data, scenario, bot_side):
        self.xls_data = data
        self.scenario = scenario #panda Series!
        self.bot_side = bot_side
        self.GAME_END = False
        self.Scenario_Map = hm.CCE_Map(data, scenario, bot_side)
        self.CCE_Cmd = Cmd.GameCommand()

    def run(self):
        while not self.GAME_END:
            print('Loop')
            self.GAME_END = True
        #     process_events() # process input and other stuff
        #     update() # update all objects that need to be updated, e.g. position changes, physics, all that other stuff
        #     draw() #render things on screen

#Test