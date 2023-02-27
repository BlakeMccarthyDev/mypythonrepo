import turtle
import tkinter as tk
from turtle import Screen

window = tk.Tk()
canvas = tk.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)
tu = turtle.RawTurtle(canvas)
tu.hideturtle()
coords = (0, 0)
tu.speed(speed='fastest')

def TurtleActions():
    tu.penup()
    tu.goto(-300, 320)
    tu.pendown()
    tu.write("Grapher", move=False, align='left', font=("Arial", 60, "normal"))
    tu.penup()
    tu.goto(0, 0)
    tu.pendown()



    '''
    tu.left(90)
    tu.forward(300)
    tu.backward(600)
    tu.forward(300)
    tu.right(90)
    '''

    #region -- Write Grid

    #region -- Vertical Lines

    for  i in range(3):
        tu.forward(100)
        tu.left(90)
        tu.forward(300)
        tu.backward(600)
        tu.penup()
        tu.backward(40)
        tu.pendown()
        tu.write(str(i + 1), move=False, align="left", font=("Arial", 20, "normal"))
        tu.penup()
        tu.forward(40)
        tu.pendown()
        tu.forward(300)
        tu.right(90)
    tu.backward(300)

    tu.left(180)

    for i in range(3):
        tu.forward(100)
        tu.right(90)
        tu.forward(300)
        tu.backward(600)
        tu.penup()
        tu.backward(40)
        tu.write(("-" + str(i+1)), move=False, align="left", font=("Arial", 20, "normal"))
        tu.forward(40)
        tu.pendown()
        tu.forward(300)
        tu.left(90)
    tu.backward(300)

    #endregion -- Vertical Lines

    #region -- Horizontal Lines


    tu.right(90)
    for i in range(3):
        tu.forward(100)
        tu.left(90)
        tu.forward(300)
        tu.penup()
        tu.forward(40)
        tu.write(str(i+1), align='left', move=False, font=("Arial", 20, 'normal'))
        tu.backward(40)
        tu.pendown()
        tu.backward(600)
        tu.forward(300)
        tu.right(90)

    tu.backward(300)

    tu.left(180)

    for i in range(3):
        tu.forward(100)
        tu.right(90)
        tu.forward(300)
        tu.penup()
        tu.forward(40)
        tu.write(("-" + str(i+1)), align='left', move=False, font=("Arial", 20, 'normal'))
        tu.backward(40)
        tu.pendown()
        tu.backward(300)
        tu.left(180)
        tu.forward(300)
        tu.backward(300)
        tu.right(90)

    tu.backward(300)


    #endregion -- Horizontal Lines

    #endregion -- Write Grid

TurtleActions()


def plot(x, y):
    x *= 100
    y *= 100
    coords = (x, y)
    tu.penup()
    tu.goto(coords[0] - 10, coords[1])
    tu.pendown()
    tu.color("Red")
    tu.begin_fill()
    tu.circle(10)
    tu.end_fill()




window.mainloop()
