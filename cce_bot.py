from __future__ import unicode_literals, print_function
from prompt_toolkit import print_formatted_text
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML, ANSI, FormattedText
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
import pandas as pd
from game import dataLoad

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
    print('Selected:'+text)


#Game Loop
# running = True
# while running:
#     process_events() # process input and other stuff
#     update() # update all objects that need to be updated, e.g. position changes, physics, all that other stuff
#     draw() #render things on screen
    


if __name__ == '__main__':
    main()