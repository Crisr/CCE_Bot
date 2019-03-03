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
    def bottom_toolbar():
        return HTML('Example: <b><style bg="ansired">Scenario...</style></b>')
    text = prompt('Select Scenario> ', bottom_toolbar=bottom_toolbar, completer=completer)
    print('Selected:',text)
    CCE_Game = game_loop.Game(data, text)
    CCE_Game.run()

if __name__ == '__main__':
    main()