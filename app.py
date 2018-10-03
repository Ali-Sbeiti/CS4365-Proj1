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
#-- Libraries
#Import Tkinter Lib (Python 3.0 CORE)
from tkinter import *

#-- Tk GUI Layout: Window (Contains)--> Frames --> Widgets
#GUI Frame
class AppWindow:
    def __init__(self, master):

        # -- Window Configuration
        #Window Size
        master.geometry("500x500")
        #Window Title
        master.title("AI Project 1")

        # -- Initialize Frame Container
        #Frame Container Gets Nested Into Window (Here called "root")
        frame = Frame(master)
        #Force Frame Somewhere Into Window
        frame.pack()
        
        # -- Widgets
        self.button = Button(frame, text="QUIT", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi = Button(frame, text="HI")
        self.hi.pack(side=RIGHT)

#Initialize Tk Window Object
root = Tk()

#Add Frame and Widgets to Window
appWin = AppWindow(root)

#Continue to Process Window
root.mainloop()