from Hackathon_Nba import *
from tkinter import *
from tkinter import messagebox

def floatTest(num):
        floatTest2 = False
        try:
                float(num)
                floatTest2 = True
        except ValueError:
                floatTest2 = False
        if floatTest2 == True:
                return True
        else:
                return False
        
        
def pointCalculator():
        
        pts = pts_entry.get("1.0", END)
        oreb = oreb_entry.get("1.0", END)
        dreb = dreb_entry.get("1.0", END)
        ast = ast_entry.get("1.0", END)
        stl = stl_entry.get("1.0", END)
        blk = blk_entry.get("1.0", END)
        fgmi = fgmi_entry.get("1.0", END)
        to = to_entry.get("1.0", END)
        
        #Needs to floatcheck all variables
        if floatTest(pts) == True and floatTest(oreb) == True and floatTest(dreb) == True and floatTest(ast) == True and floatTest(stl) == True and floatTest(blk) == True and floatTest(fgmi) == True and floatTest(to) == True:                                                       
                pts, oreb, dreb, ast = float(pts), float(oreb), float(dreb), float(ast)
                stl, blk, fgmi, to = float(stl), float(blk), float(fgmi), float(to)
                fantasytotal(pts, oreb, dreb, ast, stl, blk, fgmi, to)
        else:
                messagebox.showinfo("ERROR", "Please input numbers!")
        
        
def newPage():
        newPage = Toplevel()
        newPage.title("New Page")
        
        global pts_entry, oreb_entry, dreb_entry, ast_entry
        global stl_entry, blk_entry, fgmi_entry, to_entry
        
        ptsLabel = Label(newPage, text = "PTS")
        orebLabel = Label(newPage, text = "OREB")
        drebLabel = Label(newPage, text = "DREB")
        astLabel = Label(newPage, text = "AST")
        stlLabel = Label(newPage, text = "STL")
        blkLabel = Label(newPage, text = "BLK")
        fgmiLabel = Label(newPage, text = "FGMI")
        toLabel = Label(newPage, text = "TO")
        
        ptsLabel.grid(row = 0, column = 0)
        orebLabel.grid(row = 1, column = 0)
        drebLabel.grid(row = 2, column = 0)
        astLabel.grid(row = 3, column = 0)
        stlLabel.grid(row = 4, column = 0)
        blkLabel.grid(row = 5, column = 0)
        fgmiLabel.grid(row = 6, column = 0)
        toLabel.grid(row = 7, column = 0)
        
        pts_entry = Text(newPage, width = 10, height = 1)    
        oreb_entry = Text(newPage, width = 10, height = 1)
        dreb_entry = Text(newPage, width = 10, height = 1)    
        ast_entry = Text(newPage, width = 10, height = 1)
        stl_entry = Text(newPage, width = 10, height = 1)    
        blk_entry = Text(newPage, width = 10, height = 1)
        fgmi_entry = Text(newPage, width = 10, height = 1)    
        to_entry = Text(newPage, width = 10, height = 1)        
        
        pts_entry.grid(row = 0, column = 1)
        oreb_entry.grid(row = 1, column = 1) 
        dreb_entry.grid(row = 2, column = 1)
        ast_entry.grid(row = 3, column = 1) 
        stl_entry.grid(row = 4, column = 1)
        blk_entry.grid(row = 5, column = 1) 
        fgmi_entry.grid(row = 6, column = 1)
        to_entry.grid(row = 7, column = 1)         
        
        calculateButton = Button(newPage, text = "Find the best players!", command = pointCalculator)
        calculateButton.grid(row = 8, columnspan = 2)
        
        
#Title Page      
def main():
        root = Tk()
        root.title("Title Page")
        
        label = Label(root, text = "Find the best fantasy players based on league settings")
        label.grid(row = 0, column = 0)
        button = Button(root, text = "Get Started!", command = newPage)
        button.grid(row = 1, column = 0)

    
        
        root.mainloop()
    

if __name__ == "__main__":
        main()