''' Initial Testing Code
#Creates puzzle board of desired size
def createBoard(size,input):
    # 2D matrix representing the puzzle board
    puzzle = []
    count = 0

    #Populate Puzzle Board with Rows
    for x in range (0, size):
        #adds "Row" to the puzzle list
        puzzle.append([])

        #Populate Puzzle Board Row with Input values 
        for y in range(0, size):
            puzzle[x].append(input[count])
            count = count + 1
    
    #return reference to puzzle matrix
    return puzzle

def printBoard(puzzle):
    for x in puzzle:
        print(*x, sep=" ")

test = createBoard(3, [0,1,2,3,4,5,6,7,8])
printBoard(test)
'''
#--Libraries
#Import Tkinter Lib (Python 3.0 CORE)
from tkinter import *

#--Tk GUI Layout
#GUI Frame
class AppWin(Frame):
    def __init__(self, master):
        #initialize Frame Object
        Frame.__init__(self, master)
        self.master = master
        #assign grid to Frame
        self.grid()
        self.populateFrame()
        
        #--Window Configuration
        #Window Size
        master.geometry("500x500")
        #Window Name
        master.title("AI Project 1")
    
    def populateFrame(self):
        

        
        

#--Win Test
#Create Window Instance
root = Tk()
#Assign Application --> Tk Object
app = AppWin(root)
#Continue Processing Window
root.mainloop()
    
