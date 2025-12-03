from sac_graphics import *

class Grid():
    '''The Grid class implements a grid system using Cell objects inherited from Rectagle objects
     from John Zelle's graphics.py module.

     The Grid class create a list of lists, a matrix or multidimensional list.  The class uses
     tuples as the row, col index into the grid, hiding the multidimensional nature of the list.
     The class provides several useful methods and conforms to the emulation of container types
     in Python.  Implementing the __len__ method so len(Grid) returns the appropriate data and
     the __getitem__ method to allow the list to support indexing in the form of Grid[tuple]
     representing Grid[(row,col)], as well as the __iter__ method.  The Cell subclass inherits
     and extends the Rectangle class allowing images to be associated with a cell, as well as a
     cell type and a list for the collection of information about the Cell or hold other objects
     - accessible with standard object notation.

      Legal stuff:   All content in the grid.py file is the sole intellectual property of Adam R.
                     Albina, PhD with the exception of material from the reference Zelle graphics.py library.
                     The class is built using John Zelle’s graphics.py package available at:
                     http://mcsp.wartburg.edu/zelle/python.  The Zelle package is licensed
                     under the terms of the GPL (http://www.gnu.org/licenses/gpl.html) and used here
                     accordingly.

                     This derivative work is also licensed under GPL with the following addendum:  use of the
                     Grid class requires preservation of the legal notices in the header of the class file grid.py
                     to include author attributions in derived material or in the Appropriate Legal Notices
                     displayed by conveying works.  The original source code remains the intellectual property
                     of Adam R. Albina, for which specific provision exist in the GPL.  Use of the above assets
                     for commercial gain is prohibited.  Any other uncovered use of the assets without prior
                     permission of the author is a violation of the Saint Anselm College Intellectual
                     Property Policy as well as federal copywrite law.
    '''

    ##
    ## Version: 1.01 Original version created October 2019.  ARA
    ##
    ##
    ## Version: 1.02 Added the ability to sort by the cell attribute CellNum. November 2019.  ARA
    ##
    ##
    ## Version: 1.03 Added the ability getLRDiag from a cell loc, and getRLDiag from a cell location
    ## returns an ordered list including the specfied cell - ordered by cell number. November 2019.  ARA
    ##
    ##
    ## Version 1.04 Added the abiity to clear a particular cell or clear all of the cell attributes in
    ## in the entire grid.  These methods will only clear the custom cell attributes: imageFile, img, type,
    ## and collection.  All other attributes remain unchanged to include cellNumber.
    ##
    ## Version 1.05 Added the getCellLocation() method to provide the row and column tuple of a given cell
    ## object.
    ##


    def __init__(self,w: int,h: int,sizeofCell=100,cellOutlineColor="black",cellFillColor=None,cellBorder=1,offset_w=0,offset_h=0,numbered=False):
        self.__w = w
        self.__h = h
        self.__sizeofCell= sizeofCell
        self.__drawn = False
        self.__rows = 0
        self.__cols = 0
        self.cellOutlineColor = cellOutlineColor
        self.cellFillColor = cellFillColor
        self.cellBorder = cellBorder
        self.numbered = numbered
        self.version = "1.05"

        # Determine how many nested lists we will need (how many rows we can get)
        # Assuming that all cells are going to be sizeofCell pixels wide, then h+offset_h//sizeofCell
        # should give us the answer - we might have some cells drawn partially off the screen
        # if the numbers don't divide evenly so we should pick a height and width that is divisible
        # by sizeofCell with no remainder.
        self.__n = ((h + offset_h) // sizeofCell)

        #Make sure that the grid is at least a 2 x 2 grid so at least each cell is  a corner
        if self.__n < 2 or (w - offset_w) // sizeofCell < 2:
            raise InvalidConstruction()


        #print("cols = ", ((w - offset_w) // sizeofCell))
        # set up an empty list of lists to match the grid size (matrix)
        self.grid = [ [] for i in range(0, self.__n) ]

        # set our row counter variable to zero so we can append a list to a new row
        # as we build our matrix of Rectangle objects
        rowct = 0

        # This loop creates our matrix (list of lists)
        # and appends row after row of Rectangle objects
        # to it.
        for j in range(offset_w,self.__h,self.__sizeofCell):
            for i in range(offset_h,self.__w,self.__sizeofCell):
                pt1=Point(i,j)
                pt2 = Point(i+sizeofCell,j+sizeofCell)
                #space = Rectangle(pt1,pt2)
                space = Cell(pt1,pt2)
                space.setFill(cellFillColor)
                space.setOutline(cellOutlineColor)
                space.setWidth(cellBorder)
                self.grid[rowct].append(space)
            rowct+=1
        self.__rows = rowct
        self.__cols = len(self.grid[0])

    def __getitem__(self, pos: tuple):
        '''This method allows the Grid to support indexing in the form of Grid[tuple]. Returns a Cell object.'''
        try:
            tup = self.grid[pos[0]][pos[1]]
            return tup
        except TypeError:
            return None

    def __iter__(self):
        '''This method implements an iterator for the Grid Class. Returns a Cell object.'''
        for rowct, row in enumerate(self.grid):
            for itemct, cell in enumerate(row):
                yield cell

    def __len__(self)->int:
        '''This method allows for the len function to return the number of items in the Grid'''
        count = 0
        for rows in self.grid:
            for rects in rows:
                count+=1
        return count

    def shape(self)->tuple:
        '''Method returns the row and column count as a tuple'''
        return (self.__rows, self.__cols)

    def draw(self,win: GraphWin):
        ''' This method draws each square in the matrix and labels it with row and item number
        if the numbered boolean variable is True on __init__.  graphWin is the parameter.  If the cell
        object has an image associated with it - the image is redrawn.'''
        for rowct, row in enumerate(self.grid):
            for itemct, cell in enumerate(row):
                if self.__drawn:
                    cell.undraw()
                    if cell.img is not None:
                        cell.undrawImage()
                cell.draw(win)
                if cell.img is not None:
                    cell.drawImage(win)
                if self.numbered:
                    label = Text(cell.getCenter(),str(rowct) + "," + str(itemct))
                    label.setTextColor("black")
                    label.draw(win)
        self.__drawn = True

    def getGridLocation(self,p: Point)->tuple:
        '''This method returns a tuple containing the row and colum of Point object in the
        grid of rectangles drawn.  When you click somewhere on the grid - we first find the
        rectangle into which you clicked and then return the row and col tuple of where that
        point is in the grid.'''
        for rowidx, row in enumerate(self.grid):
            for rectidx, rect in enumerate(row):
                if p:
                    ptX = p.getX()
                    ptY = p.getY()
                    P1x = rect.getP1().getX()
                    P1y = rect.getP1().getY()
                    P2x = rect.getP2().getX()
                    P2y = rect.getP2().getY()

                    if ((min(P1x,P2x)<=ptX<=max(P1x,P2x)) and (min(P1y,P2y)<=ptY<=max(P1y,P2y))):
                        return (rowidx, rectidx)
        else:
            return None

    def getCellLocation(self, cell) -> tuple:
        """This method returns a tuple containing the row and column of a cell object."""
        c = (cell.cellNum -1) % self.__cols
        r = (cell.cellNum -1) // self.__cols
        return (r, c)

    def getRow(self,r: int)->list:
        '''Method returns a list of Cell objects in the row specified by parameter r.'''
        if r <= self.__rows -1 and r >= 0:
            rowList = []
            for i in range(0, self.__cols):
                rowList.append(self.grid[r][i])
            return rowList
        else:
            return None

    def getCol(self,c: int)->list:
        '''Method returns a list of Cell objects in the column specified by parameter r.'''
        if c <= self.__cols -1 and c >= 0:
            colList = []
            for i in range(0,self.__rows):
                colList.append(self.grid[i][c])
            return colList
        else:
            return None

    def getLRDiag(self,loc):
        '''Method returns a list of Cell objects in the in left to right diagonal from the
        cell specified in tuple parameter loc.  Returns a list from left to right of the cells
        including the cell sepcified in cell order.'''
        LRDiagList=[]

        # includes the cell at the given location
        # from cell to upper left edge
        R=loc[0]
        C=loc[1]
        while R!=-1 and C!=-1:
            LRDiagList.append(self.grid[R][C])
            R-=1
            C-=1

        # exludes the cell at the given location
        # from cell to bottom right edge
        R=loc[0] + 1
        C=loc[1] + 1
        while R!=8 and C!=8:
            LRDiagList.append(self.grid[R][C])
            R+=1
            C+=1

        LRDiagList.sort()
        return LRDiagList

    def getRLDiag(self,loc):
        '''Method returns a list of Cell objects in the in right to left diagonal from the
        cell specified in tuple parameter loc.  Returns a list from right to left of the cells
        including the cell sepcified in cell order.'''
        RLDiagList=[]

        # includes the cell at the given location
        # from cell to upper right edge
        R=loc[0]
        C=loc[1]
        while R!=-1 and C!=8:
            RLDiagList.append(self.grid[R][C])
            R-=1
            C+=1

        # exludes the cell at the given location
        # from cell to bottom left edge
        R=loc[0] + 1
        C=loc[1] - 1
        while R!=8 and C!=-1:
            RLDiagList.append(self.grid[R][C])
            R+=1
            C-=1

        RLDiagList.sort()
        return RLDiagList

    def getAdjCells(self, click: tuple)->list:
        '''This method returns a list cells of each
        cell that is adjacent to the provided cell tuple.'''
        adjList = []
        loc = None

        #Check to see if the clicked cell is a corner
        #If it is we only have three adjacent cells return
        #a list and we are done.
        loc = self.__isCorner(click)
        if loc in ["UL", "UR", "BL", "BR"]:
            if loc == "UL":
                adjList.append(self.grid[click[0]][click[1]+1])
                adjList.append(self.grid[click[0]+1][click[1]])
                adjList.append(self.grid[click[0]+1][click[1]+1])
            elif loc == "UR":
                adjList.append(self.grid[click[0]][click[1]-1])
                adjList.append(self.grid[click[0]+1][click[1]])
                adjList.append(self.grid[click[0]+1][click[1]-1])
            elif loc == "BL":
                adjList.append(self.grid[click[0]][click[1]+1])
                adjList.append(self.grid[click[0]-1][click[1]])
                adjList.append(self.grid[click[0]-1][click[1]+1])
            elif loc == "BR":
                adjList.append(self.grid[click[0]][click[1]-1])
                adjList.append(self.grid[click[0]-1][click[1]])
                adjList.append(self.grid[click[0]-1][click[1]-1])
            return adjList

        # Check to see if location is on a side, if it is then
        # we only have 5 adjecnt cells reutrn a list and we are done.
        loc = self.__isSide(click)
        if loc in ["LS","RS","TS","BS"]:
            if loc == "LS":
                adjList.append(self.grid[click[0]-1 ][click[1]])
                adjList.append(self.grid[click[0]+1 ][click[1]])
                adjList.append(self.grid[click[0]+1 ][click[1]+1 ])
                adjList.append(self.grid[click[0]-1 ][click[1]+1 ])
                adjList.append(self.grid[click[0]][click[1]+1 ])
                return adjList
            elif loc == "RS":
                adjList.append(self.grid[click[0]-1 ][click[1]])
                adjList.append(self.grid[click[0]+1 ][click[1]])
                adjList.append(self.grid[click[0]+1 ][click[1]-1])
                adjList.append(self.grid[click[0]][click[1]-1])
                adjList.append(self.grid[click[0]-1][click[1]-1])
                return adjList
            elif loc == "TS":
                adjList.append(self.grid[click[0]][click[1]+1])
                adjList.append(self.grid[click[0]][click[1]-1])
                adjList.append(self.grid[click[0]+1][click[1]])
                adjList.append(self.grid[click[0]+1][click[1]-1])
                adjList.append(self.grid[click[0]+1][click[1]+1])
                return adjList
            elif loc == "BS":
                adjList.append(self.grid[click[0]][click[1]-1])
                adjList.append(self.grid[click[0]][click[1]+1])
                adjList.append(self.grid[click[0] - 1][click[1]])
                adjList.append(self.grid[click[0] - 1][click[1] - 1])
                adjList.append(self.grid[click[0] - 1][click[1] + 1])
                return adjList
        # If we get this far we know it's not a corner or a side so we have 8
        # adjacent cells, create a list and return them
        if loc == None:
            adjList.append(self.grid[click[0]][click[1]-1])
            adjList.append(self.grid[click[0]][click[1]+1])
            adjList.append(self.grid[click[0]+1][click[1]])
            adjList.append(self.grid[click[0]-1][click[1]])
            adjList.append(self.grid[click[0]-1][click[1] + 1])
            adjList.append(self.grid[click[0]-1][click[1] - 1])
            adjList.append(self.grid[click[0]+1][click[1] + 1])
            adjList.append(self.grid[click[0]+1][click[1] - 1])
            return adjList

    def clearCell(self, click: tuple):
        self[click[0],click[1]].imageFile = None
        self[click[0],click[1]].img = None
        self[click[0],click[1]].type = ''
        self[click[0],click[1]].collection = []

    def clearCells(self):
        for rows in self.grid:
            for rects in rows:
                rects.imageFile = None
                rects.img = None
                rects.type = ''
                rects.collection = []

    def __isCorner(self, click: tuple)->str:
        if click[0]==0 and click[1]==0:
            corner="UL"
            return corner
        elif click[0]==self.__rows - 1 and click[1]==self.__cols - 1:
            corner="BR"
            return corner
        elif click[0]==self.__rows -1 and click[1]==0:
            corner="BL"
            return corner
        elif click[0]==0 and click[1]==self.__cols - 1:
            corner="UR"
            return corner
        else:
            return None

    def __isSide(self, click: tuple)->str:
        # "LS","RS","TS","BS"
        #We have to exclude corners here
        if click[0] in range(1,self.__rows) and click[1] == 0:
            return "LS"
        elif click[0] in range(1,self.__rows) and click[1] ==  self.__cols -1:
            return "RS"
        elif click[0] == 0 and click[1] in range(1, self.__cols):
            return "TS"
        elif click[0] == self.__rows-1 and click[1] in range(1,self.__cols):
            return "BS"
        else:
            return None

class Cell(Rectangle):
    count=0 #class variable
    def __init__(self,Pt1: Point,Pt2: Point,imageFile=None):
        super().__init__(Pt1,Pt2)
        self.setWidth(3)
        self.setOutline("black")
        Cell.count += 1
        self.cellNum = Cell.count
        self.imageFile = imageFile
        self.img = None
        if self.imageFile != None:
            self.setGraphicFile(self.imageFile)
        self.type = ''
        self.collection = []

    def __lt__(self, other):
        return self.cellNum < other.cellNum

    def setGraphicFile(self,graphic_file: str):
        self.imageFile = graphic_file
        self.img=Image(self.getCenter(), self.imageFile)

    def drawImage(self,win: GraphWin):
        self.img.draw(win)

    def undrawImage(self):
        self.img.undraw()

class InvalidConstruction(Exception):
    '''Exception raised for invalid construction of Grid object.'''
    def __init__(self,message = None):
        if message is None:
            self.message = "The Grid must be able to create a minimum of a 2x2 matrix."
        super(InvalidConstruction,self).__init__(self.message)

def test():
    import time
    w = 500
    h = 200
    win = GraphWin("Test Grid",w,h)
    sizeofCell = 50
    outline = 'red'
    border = 1
    fill = "white"
    offset_h = 50
    offset_w = 0
    numbered = True
    myGrid = Grid(w,h,sizeofCell,outline,fill,border,offset_h,offset_w,numbered)
    myGrid.draw(win)
    print("Version: ", myGrid.version)
    win.getMouse()
    print(myGrid[0,0].getFill())
    print(myGrid[0,0].getOutline())
    pt = win.getMouse()
    loc = myGrid.getGridLocation(pt)
    tup = myGrid.getCellLocation(myGrid[loc])
    print("Cell Location: ", tup)
    print("Calling get Row:")
    myRows = myGrid.getRow(loc[0])
    myColors=[]
    for r in myRows:
        myColors.append(r.getFill())
        r.setFill("yellow")
    time.sleep(1)
    for i in range(len(myRows)):
        myRows[i].setFill(myColors[i])
    time.sleep(1)
    print("Calling get Row:")
    myCols = myGrid.getCol(loc[1])
    myColors = []
    for c in myCols:
        myColors.append(c.getFill())
        c.setFill("yellow")
    time.sleep(1)
    for i in range(len(myCols)):
        myCols[i].setFill(myColors[i])
    time.sleep(1)
    win.getMouse()

    win.close()

if __name__ == "__main__":
    test()