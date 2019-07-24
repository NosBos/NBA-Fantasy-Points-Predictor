import xlrd
import xlwt
from xlutils.copy import copy
import os.path
import pandas as pd


file_location = "C:/Harjap Gill/Hackathon 2019/NBA_per_game_2018_stats.xlsx"

#open original data
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)


def fantasytotal(ppp,ppor,ppdr,ppa,pps,ppb,ppfgm,ppt):
    file = "C:/Harjap Gill/Hackathon 2019/data.xls"
    #create new data grid
    w_book=xlwt.Workbook()
    #add sheet
    w_sheet=w_book.add_sheet("Player Fantasy Data")
   
   #setting headers to data
    w_sheet.write(0,0,"Name")   
    w_sheet.write(0,1,"Points/Game") 
    w_sheet.write(0,2,"Assists/Game")   
    w_sheet.write(0,3,"Rebounds/Game")
    w_sheet.write(0,4,"Steals/Game")
    w_sheet.write(0,5,"Blocks/Game") 
    w_sheet.write(0,6,"Fantasy Points/Game") 
    
    #iterate through given data and find totals
    for i in range(1,sheet.nrows):
        points = sheet.cell_value(i,29)*ppp
        o_rebound = sheet.cell_value(i,21)*ppor
        d_rebound = sheet.cell_value(i,22)*ppdr
        assists = sheet.cell_value(i,24)*ppa
        steals = sheet.cell_value(i,25)*pps
        blocks = sheet.cell_value(i,26)*ppb
        missed_fg = (sheet.cell_value(i,9)-sheet.cell_value(i,8))*ppfgm
        turnovers = sheet.cell_value(i,27)*ppt
        fantasy_total = points + o_rebound + d_rebound+assists+steals+blocks+missed_fg+turnovers
        
        
        #writing onto the new created excel file
        w_sheet.write(i,0,sheet.cell_value(i,1)) #Name
        w_sheet.write(i,1,points/ppp) #points
        w_sheet.write(i,2,assists/ppa) #assists
        w_sheet.write(i,3,(o_rebound/ppor + d_rebound/ppdr))  #offensive +defensive rebounds
        w_sheet.write(i,4,steals/pps) #steals
        w_sheet.write(i,5,blocks/ppb) #blocks
        w_sheet.write(i,6,fantasy_total)  #fantasy totals
        
        
        
    #if file exists, deleate it
    if os.path.exists(file):
        os.remove(file)                  
    
    #save all data assigned onto directory                  
    w_book.save(file)
    
    #sort the data array by fantasy points column
    new_worksheet = pd.ExcelFile(file)
    new_sheet = new_worksheet.parse("Player Fantasy Data")
    new_sheet = new_sheet.sort_values(['Fantasy Points/Game'],ascending=False)
    
    #update sort to file
    new_sheet.to_excel(file, sheet_name = "Player Fantasy Data")
    
        
def sort_data(column):
    #function called by buttons on gui which sort the data based on the given column
    file = "C:/Harjap Gill/Hackathon 2019/data.xls"
    new_worksheet = pd.ExcelFile(file)
    new_sheet = new_worksheet.parse("Player Fantasy Data")
    
    if column == ('points'):
        new_sheet=new_sheet.sort_values(['Points/Game'],ascending=False)
        
    elif column == ('assists'):
        new_sheet=new_sheet.sort_values(['Assists/Game'],ascending=False)
        
    elif column == ('rebounds'):
        new_sheet=new_sheet.sort_values(['Rebounds/Game'],ascending=False)
           
    elif column == ('steals'):
        new_sheet=new_sheet.sort_values(['Steals/Game'],ascending=False)
        
    elif column == ('blocks'):
            new_sheet=new_sheet.sort_values(['Blocks/Game'],ascending=False)
                
    elif column == ('fantasy'):
        new_sheet=new_sheet.sort_values(['Fantasy Points/Game'],ascending=False)
        
    new_sheet.to_excel("C:/Harjap Gill/Hackathon 2019/data.xls", sheet_name = "Player Fantasy Data")    
        
        

def search(player_name):
    player_stats = []
    for i in range(1, sheet.nrows):
        if player_name == sheet.cell_value(i, 1):
            for n in range(1, sheet.ncols):
                player_stats.append(sheet.cell_value(i,n))
    
    return player_stats    
        
