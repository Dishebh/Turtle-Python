#!/bin/python3

from turtle import *
from random import randint

speed(10)
penup()
goto(-140,140)
for step in range(0,15):
  write(step, align="center")
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
ada = Turtle()
ada.color("red")
ada.shape("turtle")
ada.penup()
ada.goto(-160,100)
ada.pendown()

ada1 = Turtle()
ada1.color("blue")
ada1.shape("turtle")
ada1.penup()
ada1.goto(-160,70)
ada1.pendown()

for turn in range(0,100):
  ada.forward(randint(1,5))
  ada1.forward(randint(1,5))