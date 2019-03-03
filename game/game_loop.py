
class Game:
    def __init__(self, data, scenario):
        self.xls_data = data
        self.scenario = scenario
        self.GAME_END = False

    def run(self):
        while not self.GAME_END:
            print('Loop')
            self.GAME_END = True
        #     process_events() # process input and other stuff
        #     update() # update all objects that need to be updated, e.g. position changes, physics, all that other stuff
        #     draw() #render things on screen

