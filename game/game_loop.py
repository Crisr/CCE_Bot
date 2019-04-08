import game.commandPattern as Cmd
import game.hex_and_map as hm
from prompt_toolkit import print_formatted_text

map_info = print_formatted_text


class Game:
    def __init__(self, data, scenario, bot_side):
        self.xls_data = data
        self.scenario = scenario  # panda Series!
        self.bot_side = bot_side
        self.GAME_END = False
        self.Scenario_Map = hm.CCE_Map(data, scenario, bot_side)
        self.CCE_Cmd = Cmd.GameCommand()

    def run(self):
        # --Tests
        print(
            "B2@E3>",
            hm.coords_to_literal(
                self.Scenario_Map.get_neighboor(hm.literal_to_coord("B2"), "E3")
            ),
        )
        print(
            "C3@E2>",
            hm.coords_to_literal(
                self.Scenario_Map.get_neighboor(hm.literal_to_coord("C3"), "E2")
            ),
        )
        # Should return False:
        print(
            "A1@E5>",
            hm.coords_to_literal(
                self.Scenario_Map.get_neighboor(hm.literal_to_coord("A1"), "E5")
            ),
        )
        # Tests--
        while not self.GAME_END:
            print("Loop")

            self.GAME_END = True
        #     process_events() # process input and other stuff
        #     update() # update all objects that need to be updated, e.g. position changes, physics, all that other stuff
        #     draw() #render things on screen


# Test

