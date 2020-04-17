import turtle
import random
import math


def make_turtle(colr, sz, spd):
    t = turtle.Turtle()
    t.pensize(sz)
    t.color(colr)
    t.speed(spd)
    return t


def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def asteroid_creator(t):
    random_x = random.randint(-300, 300)
    random_y = random.randint(300, 320)
    t.speed(0)
    t.penup()
    t.seth(270)
    t.setpos(random_x, random_y)


def shuttle_initialize(t):
    t.speed(0)
    t.penup()
    t.seth(90)
    t.setpos(0, -300)


wn = make_window("limegreen", "Squares Everywhere!")
shuttle = make_turtle("blue", 3, 3)
asteroid = make_turtle("blue", 9, 3)


asteroid_creator(asteroid)
shuttle_initialize(shuttle)
life = 3


for i in range(2000):
    y_cor = asteroid.ycor()
    if y_cor <= -300:
        asteroid_creator(asteroid)
        life -= 1
    else:
        asteroid.fd(3)


    if life == 0:
        print("gameover")
        break


wn.write()


wn.mainloop()
