#TurtleGraphics.py
#Name:Ryan Meegan
#Date:Feb 16 2025
#Assignment:Turtle

import turtle #needed generally but not in CodeHS

def drawSquare(myTurtle, size):
    for _ in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides, size):
    for _ in range(sides):
        myTurtle.forward(size)
        myTurtle.right(360 / sides)

def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 100)
    myTurtle.begin_fill()
    
    if corner == 2:  # Top Right
        myTurtle.penup()
        myTurtle.forward(50)
        myTurtle.pendown()
        drawSquare(myTurtle, 50)
        
    elif corner == 3:  # Bottom Left 
        myTurtle.penup()
        myTurtle.right(90)  
        myTurtle.pendown()
        myTurtle.forward(50)  
        myTurtle.left(90)  
        myTurtle.forward(50)  
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.right(90)
        myTurtle.forward(50)
        
    myTurtle.end_fill()
    
def squaresInSquares(myTurtle, num):
    size = 200
    for i in range(num):
        myTurtle.penup()
        myTurtle.goto(-size / 2, size / 2)
        myTurtle.pendown()
        drawSquare(myTurtle, size)
        size *= 0.75
        

def main():
    myTurtle = turtle.Turtle()
    myTurtle.hideturtle() #hides the default turtle in CodeHS
    # drawPolygon(myTurtle, 5, 100) #draws a pentagon
    # drawPolygon(myTurtle, 8, 100) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    
if __name__ == "__main__":
    main()
