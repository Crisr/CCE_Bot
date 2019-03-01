from __future__ import unicode_literals, print_function
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML, ANSI, FormattedText
from prompt_toolkit.styles import Style
import pandas as pd
from game import dataLoad

print = print_formatted_text

def main():
    print(HTML('<orange><b>Combat Commander: Europe</b></orange> - <white>Combat bot</white>'))
    print(HTML('====================================='))
    print()
    print(HTML('Select Scenario:'))
    print(dataLoad.get_googleSheetRecords())
    


if __name__ == '__main__':
    main()