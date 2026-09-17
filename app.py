import turtle
from turtle import *
t=Turtle()
t.shape('turtle')
def square(x):
    t.forward(x)
    t.right(90)
    t.forward(x) 
    t.right(90)
    t.forward(x)
    t.right(90)
    t.forward(x)
#square(200)
def triangle(x):
    t.forward(x)
    t.right(120)
    t.forward(x)
    t.right(120)
    t.forward(x)
 #triangle(200)
def right_triangle(x):
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.right(135)
    t.forward(x)
#right_triangle
def rectangle():
    t.forward(125)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(125)
    t.right(90)
    t.forward(100)
#rectangle()
#for i in range(3):
    #print(i)
def square():
    for i in range (4):
        t.forward(200)
        t.left(90)
#square()
def triangle():
    for i in range(3):
        t.forward(300)
        t.left(120)
#triangle()
def squares():
    for i in range (59,60):
        for i in range (4):
            t.forward(300)
            t.left(90)
        t.right(5)
squares()