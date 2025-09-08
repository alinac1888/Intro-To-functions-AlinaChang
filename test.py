import turtle
from turtle import *
t=turtle
t.shape('turtle')
t.forward(200)
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    square(200)