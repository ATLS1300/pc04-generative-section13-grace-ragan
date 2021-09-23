"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Grace Ragan

********* HEY, READ THIS FIRST **********

The following code creates a generative art piece of spirographs.
There are two seperate turtles that create 2 hexagonal and 1 octogonal spirographs.
Additionally, the spirographs are randomized to show a different color each time the
code is run. This code is meant to evoke a joyful and playful reaction.

"""
import turtle
import math
import random
turtle.colormode(255)


turtle1 = turtle.Turtle()
turtle2= turtle.Turtle()

pinkPalette = ("pink","HotPink","DeepPink","PaleVioletRed")
purplePalette = ("Fuchsia","Violet","Magenta")
bluePalette = ("RoyalBlue","DodgerBlue","DeepSkyBlue")

panel = turtle.Screen()
w = 700 
h = 700 
panel.setup(width=w, height=h) 
panel.bgcolor("snow")


turtle1.shape("circle")
turtle1.speed(50)
turtle1.up()

size = 75
sides = 6
angle = 360/sides

inc = 30
numInt = int(360/inc)
innerCirc = 20

turtle1.goto(0,0)
# the following for loop creates a hexagonal spirograph each time the code is run.
for iteration in range (0,20):
    turtle1.down()
    for iteration1 in range (10):
        turtle1.forward(75)
        turtle1.right(45)
        # the following code is randomized to generate a different color from the pink pallete each time the code runs.
        color1 = random.choice(pinkPalette)
        turtle1.color(color1)
    turtle1.up()
    turtle1.forward(10)
    turtle1.right(36)
turtle1.up()
turtle1.up()

turtle1.goto(0,150)
turtle1.down()
# the following for loop creates a hexagonal spirograph each time the code is run.
size = 75
sides = 6
angle = 360/sides

inc = 30
numInt = int(360/inc)
innerCirc = 20

for iteration in range (0,20):
    turtle1.down()
    for iteration1 in range (10):
        turtle1.forward(90)
        turtle1.right(43)
        # the following code is randomized to generate a different color from the purple palette each time the code runs.
        color2 = random.choice(purplePalette) 
        turtle2.color(color2)
    turtle1.up()
    turtle1.forward(20)
    turtle1.right(34)
    turtle1.up()

turtle2.speed(50)
turtle2.shape("square")
turtle2.down()
turtle2.goto(-150,0)

# the following for loop creates an octogonal spirograph each time the code runs.
size = 75
sides = 8
angle = 360/sides

inc = 30
numInt = int(360/inc)
innerCirc = 20

for iteration in range (0,20):
    turtle2.down()
    for iteration1 in range (10):
        turtle2.forward(100)
        turtle2.right(42)
        # the following code is randomized to generate a different color from the blue palette each time the code runs.
        color3 = random.choice(bluePalette)
        turtle2.color(color3)
    turtle2.up()
    turtle2.forward(25)
    turtle2.right(33)

panel.update()
turtle.done()
