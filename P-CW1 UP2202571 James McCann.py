from graphics import *

def main():
    patchsize, colour1, colour2, colour3 = getInputs()
    drawPatchwork(patchsize, colour1, colour2, colour3)

def getInputs():

    size_selected = False
    while size_selected == False:
        try:
            patchsize = int(input("Enter your desired patch size (5, 7, or 9): "))
            if patchsize != 5 and patchsize != 7 and patchsize != 9:
                raise ValueError
        except ValueError:
            print("ERROR: Invalid input, please enter a number from the list.")
        else:
            size_selected = True
        
    
    colour_list = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
    colours_used = []

    i = 1
    while i <= 3:

        print(f"Colours available: {colour_list}")
        colour_selected = input(f"Enter colour #{i}: ")

        if colour_selected in colour_list:
            colours_used.append(colour_selected)
            colour_list.remove(colour_selected)
            i += 1

        elif colour_selected not in colour_list:
            print("ERROR: Invalid input, please choose a colour from the list.")
    
    return patchsize, colours_used[0], colours_used[1], colours_used[2]

def drawPatchwork(patchsize, colour1, colour2, colour3):

    win = GraphWin("Patchwork", patchsize*100, patchsize*100)

    colourlayout5 = [[0,0,0,0,0], #0 = C1
                     [0,1,1,1,0], #1 = C2
                     [0,1,1,2,0], #2 = C3
                     [0,1,2,2,0],
                     [0,0,0,0,0]]
    
    colourlayout7 = [[0,0,0,0,0,0,0],
                     [0,1,1,1,1,1,0],
                     [0,1,1,1,1,2,0],
                     [0,1,1,1,2,2,0],
                     [0,1,1,2,2,2,0],
                     [0,1,2,2,2,2,0],
                     [0,0,0,0,0,0,0]]

    colourlayout9 = [[0,0,0,0,0,0,0,0,0],
                     [0,1,1,1,1,1,1,1,0],
                     [0,1,1,1,1,1,1,2,0],
                     [0,1,1,1,1,1,2,2,0],
                     [0,1,1,1,1,2,2,2,0],
                     [0,1,1,1,2,2,2,2,0],
                     [0,1,1,2,2,2,2,2,0],
                     [0,1,2,2,2,2,2,2,0],
                     [0,0,0,0,0,0,0,0,0]]

    patchlayout5 = [[0,0,0,0,0], #0 = F
                    [2,2,2,2,2], #1 = P
                    [0,1,1,0,0], #2 = U
                    [2,2,2,2,2],
                    [0,0,0,0,0]]
    
    patchlayout7 = [[0,0,0,0,0,0,0],
                    [2,2,2,2,2,2,2],
                    [0,1,1,1,1,0,0],
                    [2,2,2,2,2,2,2],
                    [0,1,1,0,0,0,0],
                    [2,2,2,2,2,2,2],
                    [0,0,0,0,0,0,0]]

    patchlayout9 = [[0,0,0,0,0,0,0,0,0],
                    [2,2,2,2,2,2,2,2,2],
                    [0,1,1,1,1,1,1,0,0],
                    [2,2,2,2,2,2,2,2,2],
                    [0,1,1,1,1,0,0,0,0],
                    [2,2,2,2,2,2,2,2,2],
                    [0,1,1,0,0,0,0,0,0],
                    [2,2,2,2,2,2,2,2,2],
                    [0,0,0,0,0,0,0,0,0]]

    if patchsize == 5:
        patchworkLoop(patchsize, colourlayout5, patchlayout5, colour1, colour2, colour3, win)
    
    elif patchsize == 7:
        patchworkLoop(patchsize, colourlayout7, patchlayout7, colour1, colour2, colour3, win)

    elif patchsize == 9:
        patchworkLoop(patchsize, colourlayout9, patchlayout9, colour1, colour2, colour3, win)

def patchworkLoop(patchsize, colourlayout, patchlayout, colour1, colour2, colour3, win):

    for y in range(patchsize):
        for x in range(patchsize):

            if colourlayout[x][y] == 0:
                colour = colour1
            
            elif colourlayout[x][y] == 1:
                colour = colour2
            
            elif colourlayout[x][y] == 2:
                colour = colour3

            drawPatch(patchlayout[y][x], colour, x, y, win)
            print(patchlayout[y][x])

            win.getMouse()

def drawPatch(patchdesign, colour, x, y, win):

    if patchdesign == 0:
        patchZero(colour, x, y, win)
    
    elif patchdesign == 1:
        patchOne(colour, x, y, win)

    elif patchdesign == 2:
        patchTwo(colour, x, y, win)

def patchZero(colour, x, y, win):

    x *= 100
    y *= 100

    #for outline
    outline = Rectangle(Point(x,y),Point(x+100,y+100))
    outline.draw(win)

    x1 = x + 90 #for horizontal rectangle
    y1 = y + 10
    x2 = x
    y2 = y + 20

    x3 = x + 80 #for vertical rectangle
    y3 = y + 100

    for _ in range(5):
        reccy = Rectangle(Point(x1, y1), Point(x2, y2))
        reccy.setFill(colour)
        reccy.setOutline(colour)

        reccy2 = Rectangle(Point(x1, y1), Point(x3, y3))
        reccy2.setFill(colour)
        reccy2.setOutline(colour)

        reccy.draw(win)
        reccy2.draw(win)

        x1 -= 20
        y1 += 20

        x2 = x2
        y2 += 20

        x3 -= 20
        y3 = y3

def patchOne(colour, x, y, win):

    x *= 100
    y *= 100

    for j in range(10):
        
        if j % 2 == 0:

            for i in range(4):
                
                x1 = 25*i + x
                y1 = 10*j + y
                x2 = 25*i + x + 25
                y2 = 10*j + y + 10

                reccy = Rectangle(Point(x1, y1), Point(x2, y2))
                reccy.setFill(colour)
                reccy.draw(win)

        elif j % 2 != 0:

            for i in range(5):

                x1 = 20*i + x
                y1 = 10*j + y
                x2 = 20*i + x + 20
                y2 = 10*j + y + 10

                reccy = Rectangle(Point(x1, y1), Point(x2, y2))
                if i != 1 and i != 3:
                    reccy.setFill(colour)
                reccy.draw(win)

def patchTwo(colour, x, y, win):
    patchsqr = Rectangle(Point(x*100,y*100),Point((x*100)+100,(y*100)+100))
    patchsqr.setFill(colour)
    patchsqr.draw(win)

main()