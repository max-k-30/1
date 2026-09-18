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
    for i in range (60):
        for i in range (4):
            t.forward(300)
            t.left(90)
        t.right(5)
#squares()
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.right(y)
#square(100,90)
def double_squares(x):
    length=25
    for i in range(x):
        square(length,90)
        length = length*2 
#double_squares(5)
def double_squaress(x):
    length=25
    for i in range(x):
        square(length,90)
        length += 25 
#double_squares(20)
def squares(x):
    length = 5
    for i in range(x):
        square(length,90)
        length += 5
        t.right(5)
#squaress(60)
def star(x):
    for i in range(5):
        t.forward(x)
        t.right(144)
#star(200)
def stars(x):
    length = 10
    for i in range (x):
        star(length)
        length += 10
        t.right(5)
stars(60)