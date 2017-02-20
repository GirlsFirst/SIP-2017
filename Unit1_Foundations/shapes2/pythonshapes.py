from turtle import *
import math

john = Turtle()

setup(500,300)
x_pos = -250
y_pos = -150

john.penup()
john.setposition(x_pos,y_pos)

def drawShape(sides, length):

    #john = Turtle()
    ex_angle = 180-((180*(sides-2)/sides))
    john.pendown()
    john.speed(10)

    #john.begin_fill()
    for x in range(sides):

        john.right(ex_angle)
        john.forward(length)

    #john.end_fill()

def tessalate(sides, length, x, y):

    xloc = x
    yloc = y

    in_rads = math.radians(180/sides)
    degree_tan = math.tan(in_rads)
    apothem = int(length/(2*degree_tan))
    height = apothem*2

    for columns in range(10):
        # Draw one full coulumn.
        for row in range(10):

            drawShape(sides, length)

            john.penup()
            john.left(90)
            john.forward(height)
            john.right(90)

        # Get into position for the next column.
        john.penup()
        x = xloc + (height)*(columns+1)

        if columns % 2 == 0:
            y = yloc - apothem
        else:
            y = yloc

        john.setposition(x, y)


tessalate(6,20, x_pos, y_pos)




#john.setposition(150,150)
#print(john.position())
#john.speed(3)
#john.pensize(10)
#john.pencolor("black")
#john.down()
#john.forward(20)
#john.stamp()


# Close Window
exitonclick()
