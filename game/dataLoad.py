import pandas as pd
import pygsheets
from oauth2client.service_account import ServiceAccountCredentials
import os.path


def get_googleSheetRecords():
    # loads local xls or else google sheets xls
    if os.path.isfile('CombatCommanderEurope.xlsx'):
        print ('xlsx exists!')
        xls = pd.ExcelFile('CombatCommanderEurope.xlsx')     
        dataframe_collection = {} 
        for title in xls.sheet_names:
           dataframe_collection[title] = xls.parse(title)
        return dataframe_collection
    else:
        # scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        # credentials = ServiceAccountCredentials.from_json_keyfile_name('SolitaireBoardGames-c207d72eba1a.json', scope)
        gc = pygsheets.authorize(service_file='SolitaireBoardGames-c207d72eba1a.json')
        wks = gc.open('CombatCommanderEurope')
        
        worksheet_list = wks.worksheets()        
        dataframe_collection = {} 
        for item in worksheet_list:
            current_sheet = wks.worksheet('title',item.title)
            print("Downloading: ", current_sheet.title)
            # Extract all records
            dataframe_collection[current_sheet.title] = current_sheet.get_as_df()            
        return dataframe_collection
    




