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
from tkinter import filedialog
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
        #Configure Grid Systems
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        #Force Frame Somewhere Into Window
        frame.pack()
        
        # -- Default Widgets
        #Store Filename of Selected File
        self.fileName = "NONE"
        #Show PATH of file selected by the user
        self.filePath = Label(frame, text="File Path Selected: " + self.fileName).grid(row=1, sticky=W)

        #Function Calls the file explorer on host OS
        def openFile():
            self.fileName = filedialog.askopenfilename(initialdir = "./",title = "Select Puzzle File",filetypes = (("text files","*.txt"),("all files","*.*")))
            self.filePath = Label(frame, text="File Path Selected: " + self.fileName).grid(row=1, sticky=W)
        #Calls openFile() functions to instance file explorer 
        self.fileSelect = Button(frame, text="Open File", command=openFile).grid(row=2, sticky=W, pady=10)

        #Display Text Box Output Module
        self.matrixLog = Text(frame, wrap=WORD).grid(row=3, sticky=N+E+W+S, padx=8, pady=8)
        #Scrollbar for Text Box (TUDO: Not working)
        #scroll = Scrollbar(matrixLog).pack(side=RIGHT, fill=Y)

#Initialize Tk Window Object
root = Tk()

#Add Frame and Widgets to Window
appWin = AppWindow(root)

#Continue to Process Window
root.mainloop()