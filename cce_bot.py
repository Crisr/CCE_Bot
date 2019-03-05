from __future__ import unicode_literals, print_function
from prompt_toolkit import print_formatted_text
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML, ANSI, FormattedText
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
import pandas as pd
from game import dataLoad, game_loop

print = print_formatted_text

def main():
    print(HTML('<orange><b>Combat Commander: Europe</b></orange> - <white>Combat bot</white>'))
    print(HTML('====================================='))
    print()
    data = dataLoad.get_googleSheetRecords()
    ScenarioList = data['Scenarios']['Scenario'].tolist()
    completer = WordCompleter(ScenarioList)
    def bottom_toolbar_Scenario():
        return HTML('Example: <b><style bg="ansired">Scenario...</style></b>')
    SelectedScenario = prompt('Select Scenario> ', bottom_toolbar=bottom_toolbar_Scenario, completer=completer)
    
    Scenario_row = data['Scenarios'].loc[data['Scenarios']['Scenario'] == SelectedScenario]
    factions = Scenario_row[['GER', 'RUS', 'US']].dropna(axis='columns').keys() #drop NaN values

    completer = WordCompleter(factions.tolist())
    def bottom_toolbar_Side():
        return HTML('Example: <b><style bg="ansired">...</style></b>')
    bot_side = prompt('Select Bot Faction '+factions.tolist()[0]+'/'+factions.tolist()[1]+'> ', bottom_toolbar=bottom_toolbar_Side, completer=completer)
   
    CCE_Game = game_loop.Game(data, Scenario_row, bot_side)
    CCE_Game.run()

if __name__ == '__main__':
    main()