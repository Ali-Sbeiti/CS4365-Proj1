# -- Libraries
#Import Tkinter Lib (Python 3.0 CORE library)
from tkinter import filedialog
from tkinter import *

# -- RBFS Function
def RBFS(matrix):
    findHeuristic(matrix)

# -- Heuristic Functions
def findHeuristic(matrix):
    #Build goal state matrix based on file passed in.
    goal = []
    for x in range(len(matrix)):
        goal.append([])
        for y in range(len(matrix[x])):
            goal[x].append(str((len(matrix)*x)+y))
    #Debug## Board Comparisons
    print(matrix)
    print(goal)
    #Use Manhattan distance Method to return Heuristic Value
    #Initial Heuristic of Matrix
    heuristicValue = 0
    for i in range(len(matrix)):
        for o in range(len(matrix[x])):
            for k in range(len(goal)):
                for n in range(len(goal[k])):
                    if(matrix[i][o] == goal[k][n]):
                        #Debug
                        print("Matched " + matrix[i][o] + ": [" + str(i) + "],[" + str(o) + "] --> [" + str(k) + "],[" + str(n) + "] = " + str(( abs(k-i) + abs(n-o))))
                        heuristicValue += (abs(k-i) + abs(n-o))
    print("Total H(n): " + str(heuristicValue))
    return heuristicValue

# -- Output
#Append to end of matrixlog
def initialOut(out,matrix):
    #Make GUI textarea writable 
    out.matrixLog.config(state=NORMAL)
    #Add borders for readability
    for i in range(20):
        out.matrixLog.insert(END,'#')
    #Label Initial State
    out.matrixLog.insert(END, '\nInitial State: \n\n')
    out.matrixLog.config(state=DISABLED)

    #Print Current Board State (Initial)
    printBoard(out,matrix)

    out.matrixLog.config(state=NORMAL)
    #add borders for readability
    for i in range(20):
        out.matrixLog.insert(END, '#')
    out.matrixLog.insert(END, '\n\n')
    out.matrixLog.config(state=DISABLED)

#Print current state of the puzzle matrix
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
        print('Failed to Open and Read File OR Aborted Open Operation --> ' + self.fileName)
        return

    #File Open and Read, now start search algorithm, Recursive Best-First Search (RBFS)
    try:
        RBFS(matrix)                              
    except:
        #Could not solve puzzle
        print('Read Puzzle into Memory but could not solve --> ' + self.fileName)
        return
        

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