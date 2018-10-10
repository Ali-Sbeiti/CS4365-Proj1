# -- Libraries
#Import Tkinter Lib (Python 3.0 CORE library)
from tkinter import filedialog
from tkinter import *

# -- Output
#Append to end of matrixlog
def initialOut(out,matrix):
    out.matrixLog.config(state=NORMAL)
    out.matrixLog.insert(END,'####################################\nInitial State:\n\n')
    out.matrixLog.config(state=DISABLED)
    printBoard(out,matrix)
    out.matrixLog.config(state=NORMAL)
    out.matrixLog.insert(END,'####################################\n\n')
    out.matrixLog.config(state=DISABLED)

def printBoard(out,matrix):
    out.matrixLog.config(state=NORMAL)
    for x in matrix:
        for y in x:
            out.matrixLog.insert(END, '|' + y + '|')
        out.matrixLog.insert(END, '\n')
    out.matrixLog.insert(END, '\n')
    out.matrixLog.config(state=DISABLED)

# -- File Finding/Parsing
#Parse File Input for Puzzle Matrix, Returns a list of lists to represent 2D matrix
def parseFile(self):
    #List Will Contain Rows That Represent our Puzzle Board
    matrix = []
    #Counter Tracks Which Row on Board We're Building
    row = 0
    try:
        #Open File Passed in From File Dialog Window
        with open(self.fileName, 'r') as file:
            #Parse Each Line in the File
            for x in file:
                #Trim Whitespace on Line From File
                rowLine = x.strip()
                if rowLine:
                 #For Every Non-Empty Row From File, Append Empty List
                 matrix.append([])
                 #Parse Each Column of Row line
                 for y in rowLine:
                     columnVal = y.strip()
                     if columnVal:
                         #Append Each Matrix Element to the Current Row
                         matrix[row].append(columnVal)
                if rowLine:
                    #Increment Row ID Number
                    row += 1
            #New file opened successfully, clear textbox
            self.matrixLog.delete(1.0,END) 
            initialOut(self,matrix)
                                
    except:
        #Could Not Open, Or Could not Read Input (Bad Input)
        print('Failed to Open and Read File --> ' + self.fileName)

#Function Calls the file explorer on host OS
def openFile(self):
    #Prompt user to load in puzzle file, in .txt format
    self.fileName = filedialog.askopenfilename(initialdir = "./",title = "Select Puzzle File",filetypes = (("text files","*.txt"),("all files","*.*")))
    #Update selected file path
    self.filePath = Label(self.frame, text="File Path Selected: " + self.fileName).grid(row=1, sticky=W)
    #Function reads and stores Puzzle state in memory
    parseFile(self)
            
# -- Tk GUI Layout: Window (Contains)--> self.frames (Contains)--> Widgets
#GUI self.frame
class AppWindow:
    def __init__(self, master):

        # -- Window Configuration
        #Window Size
        master.geometry("500x500")
        #Window Title
        master.title("AI Project 1")

        # -- Initialize self.frame Container
        #self.frame Container Gets Nested Into Window (Here called "root")
        self.frame = Frame(master)
        #Configure Grid Systems
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        #Force self.frame Somewhere Into Window
        self.frame.pack()
        
        # -- Default Widgets
        #Store Filename of Selected File
        self.fileName = None
        #Show PATH of file selected by the user
        self.filePath = Label(self.frame, text="File Path Selected: " + ("None" if self.fileName == None else self.fileName)).grid(row=1, sticky=W)

        #Calls openFile() functions to instance file explorer 
        self.fileSelect = Button(self.frame, text="Open File", command=lambda:openFile(self)).grid(row=2, sticky=W, pady=10)

        #Display Text Box Output Module
        self.matrixLog = Text(self.frame)
        self.matrixLog.grid(row=3, sticky=N+E+W+S, padx=8, pady=8)
        self.matrixLog.config(state=DISABLED)
        #Scrollbar for Text Box (TUDO: Not working)
        #scroll = Scrollbar(matrixLog).pack(side=RIGHT, fill=Y)

# -- Workbench: Spawns Application Graphics and Methods
#Initialize Tk Window Object
root = Tk()
#Add self.frame and Widgets to Window
appWin = AppWindow(root)
#Continue to Process Window
root.mainloop()