# Authors: Brooke Tardugno and Kaitlin McDonough
# Filename: 1010FinalProject.py
# Description: This program will simulate the game, "1010!" We will use sac graphics, grid, random, and shape classes to
#              play this game. Multiple windows are used to display instructions, play the game, display the final
#              score, and say goodbye to the user.
# Input: User input is mouse clicks throughout the game which will be explained to the user in the instructions
# Output: Outputs include opening and closing windows, filling background color of rectangles, changing score,
#         displaying chosen shapes in a grid, and clearing rows and columns if the user fills them.

from sac_graphics import *
from grid import Grid
from shapes import Lshape, Bcube, Vline, Hline, SingleCube
import random

# this function will check which rectangle is clicked or if the quit button is clicked and return a boolean value
def isClicked(point: Point, rect: Rectangle) -> bool:
    if point != None:
        px, py = point.getX(), point.getY()
        p1, p2, = rect.getP1(), rect.getP2()
        if p1.getX() <= px <= p2.getX() and p1.getY() <= py <= p2.getY():
            return True
        else:
            return False
    return False


# this function check rows in the row list to see if a row is filled or not
def checkRow(rlist) -> bool:
    for cell in rlist:
        if cell.getFill() == 'white':
            return False
    return True


# this function will clear the rows in the row list
def checkRows(grid, clearlist):
    for i in range(10):
        rlist = grid.getRow(i)
        if checkRow(rlist):
            clearlist.extend(rlist)
    return clearlist


# this function check columns in the row list to see if a column is filled or not
def checkCol(clist) -> bool:
    for cell in clist:
        if cell.getFill() == 'white':
            return False
    return True


# this function will clear the columns in the column list
def checkCols(grid, clearlist):
    for i in range(10):
        clist = grid.getCol(i)
        if checkCol(clist):
            clearlist.extend(clist)
    return clearlist


# this function will check if each shape is legal or is able to be placed in the grid
def isLegal(grid, x, y, shape) -> bool:
    if shape == 'Lshape':
        if grid[x, y].getFill() != 'white':
            return False
        elif x + 3 > 9:
            return False
        elif y + 1 > 9:
            return False
        elif grid[x + 1, y].getFill() != 'white':
            return False
        elif grid[x + 2, y].getFill() != 'white':
            return False
        elif grid[x + 3, y].getFill() != 'white':
            return False
        elif grid[x + 3, y + 1].getFill() != 'white':
            return False
        else:
            return True
    if shape == 'Hline':
        if grid[x, y].getFill() != 'white':
            return False
        elif y + 4 > 9:
            return False
        elif grid[x, y + 1].getFill() != 'white':
            return False
        elif grid[x, y + 2].getFill() != 'white':
            return False
        elif grid[x, y + 3].getFill() != 'white':
            return False
        elif grid[x, y + 4].getFill() != 'white':
            return False
        else:
            return True
    if shape == 'Vline':
        if grid[x, y].getFill() != 'white':
            return False
        elif x + 4 > 9:
            return False
        elif grid[x + 1, y].getFill() != 'white':
            return False
        elif grid[x + 2, y].getFill() != 'white':
            return False
        elif grid[x + 3, y].getFill() != 'white':
            return False
        elif grid[x + 4, y].getFill() != 'white':
            return False
        else:
            return True
    if shape == 'SingleCube':
        if grid[x, y].getFill() != 'white':
            return False
        else:
            return True
    if shape == 'Bcube':
        if grid[x, y].getFill() != 'white':
            return False
        elif x + 1 > 9:
            return False
        elif y + 1 > 9:
            return False
        elif grid[x + 1, y].getFill() != 'white':
            return False
        elif grid[x + 1, y + 1].getFill() != 'white':
            return False
        elif grid[x, y + 1].getFill() != 'white':
            return False
        else:
            return True


def main():
    w, h = 500, 700
    # create first window and display features
    win = GraphWin("Instructions", w, h)
    win.setBackground("pink")
    welcome = Text(Point(w / 2, h / 4), "Welcome to 1010!")
    welcome.setSize(35)
    welcome.setStyle('bold')
    welcome.draw(win)
    instructions = Text(Point(w / 2, 275), "How to Play:\n\nIn this game you will be given 3 shapes to choose from. "
                                           "You must select a \nshape and place it in the grid. The goal is to clear "
                                           "rows and columns in \norder to earn points and continue the game. Shapes "
                                           "may not overlap in \nthe grid. And be careful, once there is no place for "
                                           "the given shapes to go,\n you lost and must press the quit button to "
                                           "forfeit the game.")
    instructions.setSize(15)
    instructions.draw(win)
    GL = Text(Point(w / 2, 400), "Press the play button to begin. Good luck!")
    GL.setSize(20)
    GL.setStyle("bold")
    GL.draw(win)
    play = Rectangle(Point(150, 475), Point(350, 575))
    play.draw(win)
    playText = Text(Point(w / 2, 525), "PLAY")
    playText.setSize(15)
    playText.draw(win)
    mp = win.getMouse()
    if mp:
        # if play is pressed
        if isClicked(mp, play):
            win.close()
            sizeofCell = 50
            outline = "grey"
            border = 1
            offset_h = 0
            offset_w = 200
            fill = "white"
            win = GraphWin("1010!", w, h)
            win.setBackground(color_rgb(220, 220, 220))

            myGrid = Grid(w=w, h=h, sizeofCell=sizeofCell,
                          cellOutlineColor=outline, cellFillColor=fill,
                          cellBorder=border, offset_h=offset_h, offset_w=offset_w)

            myGrid.draw(win)

            # Create rectangles to store shapes and score
            rec1 = Rectangle(Point(0, 40), Point(166, 200))
            rec1.draw(win)
            rec2 = Rectangle(Point(166, 40), Point(333, 200))
            rec2.draw(win)
            rec3 = Rectangle(Point(333, 40), Point(500, 200))
            rec3.draw(win)
            # score text
            player_score = Text(Point(200, 20), "SCORE:")
            player_score.setStyle("bold")
            player_score.setSize(20)
            player_score.setTextColor("Blue")
            player_score.draw(win)
            score = 0
            # display current score
            current_score = Text(Point(270, 20), '0')
            current_score.setStyle("bold")
            current_score.setSize(20)
            current_score.draw(win)
            currentShapes = [0, 0, 0]
            clearlist = []
            # rectangle for user to quit if pressed
            qrect = Rectangle(Point(10, 5), Point(40, 35))
            qrect.setFill("light blue")
            qrect.draw(win)
            qtext = Text(Point(25, 20), "QUIT")
            qtext.draw(win)
            run = True
        # if play is not pressed
        else:
            win.close()
            score = "N/A"
            run = False
        # start while loop
        while run:
            if currentShapes[0] == 0 and currentShapes[1] == 0 and currentShapes[2] == 0:
                currentShapes.clear()
                # SHAPE FOR BOX 1
                x = rec1.getCenter().getX()
                y = rec1.getCenter().getY()
                # center shape
                l_shape_rec1 = Lshape(x - 12.5, y - 50, "blue")
                h_line_rec1 = Hline(x - 62.5, y - 12.5, "pink")
                v_line_rec1 = Vline(x - 12.5, y - 62.5, "green")
                cube_rec1 = SingleCube(x - 12.5, y - 12.5, "red")
                b_cube_rec1 = Bcube(x - 25, y - 25, "purple")
                shapes = ["Lshape", "Hline", "Vline", "SingleCube", "Bcube"]
                type1 = random.choice(shapes)

                # display randomly chosen shape in rectangle 1
                if type1 == "Vline":
                    currentShapes.append(v_line_rec1)
                    v_line_rec1.draw(win)
                elif type1 == "SingleCube":
                    currentShapes.append(cube_rec1)
                    cube_rec1.draw(win)
                elif type1 == "Hline":
                    currentShapes.append(h_line_rec1)
                    h_line_rec1.draw(win)
                elif type1 == "Lshape":
                    currentShapes.append(l_shape_rec1)
                    l_shape_rec1.draw(win)
                elif type1 == "Bcube":
                    currentShapes.append(b_cube_rec1)
                    b_cube_rec1.draw(win)

                # SHAPE FOR BOX 2
                x2 = rec2.getCenter().getX()
                y2 = rec2.getCenter().getY()
                # center shape
                l_shape_rec2 = Lshape(x2 - 12.5, y2 - 50, "blue")
                h_line_rec2 = Hline(x2 - 62.5, y2 - 12.5, "pink")
                v_line_rec2 = Vline(x2 - 12.5, y2 - 62.5, "green")
                cube_rec2 = SingleCube(x2 - 12.5, y2 - 12.5, "red")
                b_cube_rec2 = Bcube(x2 - 25, y2 - 25, "purple")

                shapes = ["Lshape", "Hline", "Vline", "SingleCube", "Bcube"]
                type2 = random.choice(shapes)

                # display randomly chosen shape in rectangle 2
                if type2 == "Vline":
                    currentShapes.append(v_line_rec2)
                    v_line_rec2.draw(win)
                elif type2 == "SingleCube":
                    currentShapes.append(cube_rec2)
                    cube_rec2.draw(win)
                elif type2 == "Hline":
                    currentShapes.append(h_line_rec2)
                    h_line_rec2.draw(win)
                elif type2 == "Lshape":
                    currentShapes.append(l_shape_rec2)
                    l_shape_rec2.draw(win)
                elif type2 == "Bcube":
                    currentShapes.append(b_cube_rec2)
                    b_cube_rec2.draw(win)

                # SHAPE FOR BOX 3
                x3 = rec3.getCenter().getX()
                y3 = rec3.getCenter().getY()
                # center shape
                l_shape_rec3 = Lshape(x3 - 12.5, y3 - 50, "blue")
                h_line_rec3 = Hline(x3 - 62.5, y3 - 12.5, "pink")
                v_line_rec3 = Vline(x3 - 12.5, y3 - 62.5, "green")
                cube_rec3 = SingleCube(x3 - 12.5, y3 - 12.5, "red")
                b_cube_rec3 = Bcube(x3 - 25, y3 - 25, "purple")

                shapes = ["Lshape", "Hline", "Vline", "SingleCube", "Bcube"]
                type3 = random.choice(shapes)

                # display randomly chosen shape in rectangle 3
                if type3 == "Vline":
                    currentShapes.append(v_line_rec3)
                    v_line_rec3.draw(win)
                elif type3 == "SingleCube":
                    currentShapes.append(cube_rec3)
                    cube_rec3.draw(win)
                elif type3 == "Hline":
                    currentShapes.append(h_line_rec3)
                    h_line_rec3.draw(win)
                elif type3 == "Lshape":
                    currentShapes.append(l_shape_rec3)
                    l_shape_rec3.draw(win)
                elif type3 == "Bcube":
                    currentShapes.append(b_cube_rec3)
                    b_cube_rec3.draw(win)

            # if rectangle 1 is clicked
            mp = win.getMouse()
            if isClicked(mp, qrect):
                win.close()
                run = False
            elif isClicked(mp, rec1):
                rec1.setFill(color_rgb(202, 225, 255))
                if currentShapes[0] != 0 and currentShapes[0].type == 'SingleCube':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP.getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'SingleCube'):
                            myGrid[location].setFill("red")
                            cube_rec1.undraw()
                            currentShapes[0] = 0
                    # if user doesn't click in grid
                    else:
                        rec1.setFill(color_rgb(220, 220, 220))
                elif currentShapes[0] != 0 and currentShapes[0].type == 'Lshape':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP.getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Lshape'):
                            myGrid[location].setFill("blue")
                            myGrid[x + 1, y].setFill("blue")
                            myGrid[x + 2, y].setFill("blue")
                            myGrid[x + 3, y].setFill("blue")
                            myGrid[x + 3, y + 1].setFill("blue")
                            l_shape_rec1.undraw()
                            currentShapes[0] = 0
                        # if user doesn't click in grid
                        else:
                            rec1.setFill(color_rgb(220, 220, 220))
                elif currentShapes[0] != 0 and currentShapes[0].type == 'Vline':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP.getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Vline'):
                            myGrid[location].setFill("green")
                            myGrid[x + 1, y].setFill("green")
                            myGrid[x + 2, y].setFill("green")
                            myGrid[x + 3, y].setFill("green")
                            myGrid[x + 4, y].setFill("green")
                            v_line_rec1.undraw()
                            currentShapes[0] = 0
                        # if user doesn't click in grid
                        else:
                            rec1.setFill(color_rgb(220, 220, 220))
                elif currentShapes[0] != 0 and currentShapes[0].type == 'Hline':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP.getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Hline'):
                            myGrid[location].setFill("pink")
                            myGrid[x, y + 1].setFill("pink")
                            myGrid[x, y + 2].setFill("pink")
                            myGrid[x, y + 3].setFill("pink")
                            myGrid[x, y + 4].setFill("pink")
                            h_line_rec1.undraw()
                            currentShapes[0] = 0
                        # if user doesn't click in grid
                        else:
                            rec1.setFill(color_rgb(220, 220, 220))
                elif currentShapes[0] != 0 and currentShapes[0].type == 'Bcube':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Bcube'):
                            myGrid[location].setFill("purple")
                            myGrid[x + 1, y].setFill("purple")
                            myGrid[x + 1, y + 1].setFill("purple")
                            myGrid[x, y + 1].setFill("purple")
                            b_cube_rec1.undraw()
                            currentShapes[0] = 0
                        # if user doesn't click in grid
                        else:
                            rec1.setFill(color_rgb(220, 220, 220))
                rec1.setFill(color_rgb(220, 220, 220))
                clearlist = checkRows(myGrid, clearlist)
                clearlist = checkCols(myGrid, clearlist)
                for cell in clearlist:
                    cell.setFill("white")
                    score += 1
                    current_score.setText(str(score))
                clearlist.clear()

            # if rectangle 2 is clicked
            elif isClicked(mp, rec2):
                rec2.setFill(color_rgb(202, 225, 255))
                if currentShapes[1] != 0 and currentShapes[1].type == 'SingleCube':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'SingleCube'):
                            myGrid[location].setFill("red")
                            cube_rec2.undraw()
                            currentShapes[1] = 0
                    # if user doesn't click in grid
                    else:
                        rec2.setFill(color_rgb(220, 220, 220))
                elif currentShapes[1] != 0 and currentShapes[1].type == 'Lshape':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Lshape'):
                            myGrid[location].setFill("blue")
                            myGrid[x + 1, y].setFill("blue")
                            myGrid[x + 2, y].setFill("blue")
                            myGrid[x + 3, y].setFill("blue")
                            myGrid[x + 3, y + 1].setFill("blue")
                            l_shape_rec2.undraw()
                            currentShapes[1] = 0
                    # if user doesn't click in grid
                    else:
                        rec2.setFill(color_rgb(220, 220, 220))
                elif currentShapes[1] != 0 and currentShapes[1].type == 'Vline':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Vline'):
                            myGrid[location].setFill("green")
                            myGrid[x + 1, y].setFill("green")
                            myGrid[x + 2, y].setFill("green")
                            myGrid[x + 3, y].setFill("green")
                            myGrid[x + 4, y].setFill("green")
                            v_line_rec2.undraw()
                            currentShapes[1] = 0
                    # if user doesn't click in grid
                    else:
                        rec2.setFill(color_rgb(220, 220, 220))
                elif currentShapes[1] != 0 and currentShapes[1].type == 'Hline':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Hline'):
                            myGrid[location].setFill("pink")
                            myGrid[x, y + 1].setFill("pink")
                            myGrid[x, y + 2].setFill("pink")
                            myGrid[x, y + 3].setFill("pink")
                            myGrid[x, y + 4].setFill("pink")
                            h_line_rec2.undraw()
                            currentShapes[1] = 0
                    # if user doesn't click in grid
                    else:
                        rec2.setFill(color_rgb(220, 220, 220))
                elif currentShapes[1] != 0 and currentShapes[1].type == 'Bcube':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Bcube'):
                            myGrid[location].setFill("purple")
                            myGrid[x + 1, y].setFill("purple")
                            myGrid[x + 1, y + 1].setFill("purple")
                            myGrid[x, y + 1].setFill("purple")
                            b_cube_rec2.undraw()
                            currentShapes[1] = 0
                    # if user doesn't click in grid
                    else:
                        rec2.setFill(color_rgb(220, 220, 220))
                rec2.setFill(color_rgb(220, 220, 220))
                clearlist = checkRows(myGrid, clearlist)
                clearlist = checkCols(myGrid, clearlist)
                for cell in clearlist:
                    cell.setFill("white")
                    score += 1
                    current_score.setText(str(score))
                clearlist.clear()
            # if rectangle 3 is clicked
            elif isClicked(mp, rec3):
                rec3.setFill(color_rgb(202, 225, 255))
                if currentShapes[2] != 0 and currentShapes[2].type == 'SingleCube':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'SingleCube'):
                            myGrid[location].setFill("red")
                            cube_rec3.undraw()
                            currentShapes[2] = 0
                    # if user doesn't click in grid
                    else:
                        rec3.setFill(color_rgb(220, 220, 220))
                elif currentShapes[2] != 0 and currentShapes[2].type == 'Lshape':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Lshape'):
                            myGrid[location].setFill("blue")
                            myGrid[x + 1, y].setFill("blue")
                            myGrid[x + 2, y].setFill("blue")
                            myGrid[x + 3, y].setFill("blue")
                            myGrid[x + 3, y + 1].setFill("blue")
                            l_shape_rec3.undraw()
                            currentShapes[2] = 0
                    # if user doesn't click in grid
                    else:
                        rec3.setFill(color_rgb(220, 220, 220))
                elif currentShapes[2] != 0 and currentShapes[2].type == 'Vline':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Vline'):
                            myGrid[location].setFill("green")
                            myGrid[x + 1, y].setFill("green")
                            myGrid[x + 2, y].setFill("green")
                            myGrid[x + 3, y].setFill("green")
                            myGrid[x + 4, y].setFill("green")
                            v_line_rec3.undraw()
                            currentShapes[2] = 0
                    # if user doesn't click in grid
                    else:
                        rec3.setFill(color_rgb(220, 220, 220))
                elif currentShapes[2] != 0 and currentShapes[2].type == 'Hline':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Hline'):
                            myGrid[location].setFill("pink")
                            myGrid[x, y + 1].setFill("pink")
                            myGrid[x, y + 2].setFill("pink")
                            myGrid[x, y + 3].setFill("pink")
                            myGrid[x, y + 4].setFill("pink")
                            h_line_rec3.undraw()
                            currentShapes[2] = 0
                    # if user doesn't click in grid
                    else:
                        rec3.setFill(color_rgb(220, 220, 220))
                elif currentShapes[2] != 0 and currentShapes[2].type == 'Bcube':
                    gridMP = win.getMouse()
                    # make sure user clicks in grid
                    if gridMP. getY() > 200:
                        location = myGrid.getGridLocation(gridMP)
                        x = location[0]
                        y = location[1]
                        if isLegal(myGrid, x, y, 'Bcube'):
                            myGrid[location].setFill("purple")
                            myGrid[x + 1, y].setFill("purple")
                            myGrid[x + 1, y + 1].setFill("purple")
                            myGrid[x, y + 1].setFill("purple")
                            b_cube_rec3.undraw()
                            currentShapes[2] = 0
                    # if user doesn't click in grid
                    else:
                        rec3.setFill(color_rgb(220, 220, 220))
                rec3.setFill(color_rgb(220, 220, 220))
                clearlist = checkRows(myGrid, clearlist)
                clearlist = checkCols(myGrid, clearlist)
                for cell in clearlist:
                    cell.setFill("white")
                    score += 1
                    current_score.setText(str(score))
                clearlist.clear()
        win.close()
        # show game over window and display score
        win = GraphWin("Game Over", w, h)
        win.setBackground('light blue')
        GO = Text(Point(250, 150), "GAME OVER")
        GO.setSize(30)
        GO.setTextColor("red")
        GO.setStyle("bold")
        GO.draw(win)
        result = Text(Point(250, 300), "Your score was: " + str(score))
        result.setSize(20)
        result.setStyle("bold")
        result.draw(win)
        win.getMouse()
        win.close()
        # Goodbye window
        win = GraphWin("Bye!", w, h)
        win.setBackground("light blue")
        Bye = Text(Point(w / 2, h / 2), "Bye-Bye!")
        Bye.setSize(30)
        Bye.draw(win)
        time.sleep(3)
        win.close()


if __name__ == "__main__":
    main()
