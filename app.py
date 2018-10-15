# -- Libraries
#Import Tkinter Lib (Python 3.3 CORE library)
from tkinter import filedialog
from tkinter import *
#Import Copy Lib (3.3 CORE)
import copy
#INFINITY "Constant"
INFINITY = 1000000
from time import sleep

# -- RBFS Function
def RBFS(this):
    #Fill Object and a List of children
    this.addSubtree(findChildren(this.state))

    #Check Pre-conditions
    #Check if current node is a goal state
    if(this.nodeHeuristic == 0):
        #Add goal state to the list of solution states
        this.solution.append(this.state)
        return 0
    #No Children (Moves) Possible (Impossible?)
    if not this.children:
        return INFINITY
    
    #For every child matrix, place in a puzzle node object
    nodeChildren = []
    for child in this.children:
        nodeChildren.append(Puzzle(child))

    #Initial Sort List of Puzzle Node objects organized by heuristic values (Low -> High)
    nodeChildren.sort(key=lambda node: node.nodeHeuristic)
    
    #Increment through subtree until a valid path to the solution has been found
    while True:
        #DEBUG
        sleep(2)
        #Node with lowest heuristic is always the candidate
        candidate = nodeChildren[0]
        #Set candidates grandfather to current node state
        candidate.previous = this.state
        #CHeck to see if search fucntion is about to loop
        if(this.previous):
            if(this.previous == candidate.state):
                print("NO LOOP")
                candidate.nodeHeuristic = INFINITY
                return this.nodeHeuristic

        #Check if cheapest node is within bound set by parent
        if(this.maxHeuristic < candidate.nodeHeuristic):
            #If not within bound, set heuristic of parent with cheapest node in subtree
            this.nodeHeuristic = candidate.nodeHeuristic
            print("Reverted Recursion")
            return this.nodeHeuristic
        #Set maximum bound to the heuristic of the next cheapest node (including parent)
        if(this.maxHeuristic > nodeChildren[1].nodeHeuristic):
            candidate.maxHeuristic = nodeChildren[1].nodeHeuristic
        else:
            candidate.maxHeuristic = this.maxHeuristic
        #Explore next cheapest subtree
        nextHeu = RBFS(candidate)
        #IF candidate was the goal state
        if(nextHeu == 0):
            #recursively add states to the list of solution states
            this.solution.append(this.state)
            return nextHeu
        #Resort child list in case of heuristic changes change
        nodeChildren.sort(key=lambda node: node.nodeHeuristic)

# -- Heuristic Functions
def findHeuristic(matrix):
    #Build goal state matrix based on file passed in.
    goal = []
    for x in range(len(matrix)):
        goal.append([])
        for y in range(len(matrix[x])):
            goal[x].append(str((len(matrix)*x)+y))
    #Use Manhattan distance Method to return Heuristic Value
    #Initial Heuristic of Matrix
    heuristicValue = 0
    for i in range(len(matrix)):
        for o in range(len(matrix[x])):
            for k in range(len(goal)):
                for n in range(len(goal[k])):
                    if(matrix[i][o] == goal[k][n]):
                        if((k == 0) and (n == 0)):
                            pass
                        else:
                            heuristicValue += (abs(k-i) + abs(n-o))
                            #DEBUGprint("FOUND: " + "[" + str(i) + str(o) + " |AT| " + str(k) + str(n)+ "]:" + str(abs(k-i)) +" + " + str(abs(n-o)))
    print("Total H(n): " + str(heuristicValue))
    return heuristicValue

#Returns a list of possible board states after one move
def findChildren(matrix):
    #find empty tile on matrix
    empty = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if(matrix[x][y] == '0'):
                empty.append(x)
                empty.append(y)
    states = []
    #check if a north swap is possible
    if((empty[0] - 1) >= 0):
        print("Swap North")
        states.append(tileSwap(matrix, empty, [(empty[0] - 1), empty[1]]))
    #check if a south swap is possible
    if((empty[0] + 1) < len(matrix)):
        print("Swap South")
        states.append(tileSwap(matrix, empty, [(empty[0] + 1), empty[1]]))
    #check if east swap is possible
    if((empty[1] + 1) < len(matrix[empty[0]])):
        print("Swap East")
        states.append(tileSwap(matrix, empty, [empty[0], (empty[1] + 1)]))
    #check if west swap is possible
    if((empty[1] - 1) >= 0):
        print("Swap West")
        states.append(tileSwap(matrix, empty, [empty[0], (empty[1] - 1)]))

    return states

    #Debug
    '''for state in states:
        printBoard(appWin, state)
    printBoard(appWin, matrix)'''
#Swaps the empty tile of a matrix with some other tile in a direction
def tileSwap(matrix,empty,tile):
    #Create a copy of the matrix object
    newPuzzle = copy.deepcopy(matrix)
    #Swap tiles of the 2 coordinates passed in (Empty and Tile)
    newPuzzle[empty[0]][empty[1]], newPuzzle[tile[0]][tile[1]] = newPuzzle[tile[0]][tile[1]], newPuzzle[empty[0]][empty[1]]
    return newPuzzle


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
        test = Puzzle(matrix)
        RBFS(test)
        test.solution.reverse()
        for t in test.solution:
            printBoard(appWin, t)                             
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

# -- Tree/Node Object Structure
#Node object structure
class Puzzle:
    solution = []
    def __init__(self,matrix,max=INFINITY):
        self.children = []
        self.state = matrix
        self.previous = []
        self.nodeHeuristic = findHeuristic(matrix)
        self.maxHeuristic = max

    #Object Functions
    #Add child subtree to this node
    def addSubtree(self, tree):
        self.children = copy.deepcopy(tree)

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