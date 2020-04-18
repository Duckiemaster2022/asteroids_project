import random
import turtle


def reset_postion(t):
    t.pu()
    t.setpos(0, 0)
    t.pd()


def logo(t, tu):
    t.hideturtle()
    tu.hideturtle()
    t.pu()
    t.setpos(0, 150)
    tu.setpos(0, 150)
    t.pd()
    t.seth(45)
    t.circle(-90, extent=95)
    tu.setpos(-100, 150)
    reset_postion(tu)
    tu.circle(150, extent=-40)
    reset_postion(tu)
    tu.seth(-10)
    tu.circle(160, extent=50)
    tu.seth(90)
    tu.fd(20)
    tu.lt(90)
    tu.fd(15)
    tu.pu()
    tu.setpos(0, 128)
    tu.pd()
    tu.circle(30, extent=-175)
    tu.seth(-45)
    tu.back(-45)


def make_turtle(colr, sz, spd):
    t = turtle.Turtle()
    t.pensize(sz)
    t.color(colr)
    t.speed(spd)
    t.hideturtle()
    return t


def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def asteroid_creator(t):
    asteroid.showturtle()
    random_x = random.randint(-300, 300)
    random_y = random.randint(300, 320)
    t.speed(0)
    t.penup()
    t.seth(270)
    t.setpos(random_x, random_y)


def shuttle_initialize(t):
    shuttle.showturtle()
    t.speed(3)
    t.penup()
    t.seth(90)
    t.setpos(0, -250)


def spaceship_moving_d():
    shuttle.setx(shuttle.xcor() + DELTAX)


def spaceship_moving_a():
    shuttle.setx(shuttle.xcor() - DELTAX)


# logo(logo_t, logo_tu)

wn = make_window("limegreen", "Squares Everywhere!")
shuttle = make_turtle("blue", 3, 3)
asteroid = make_turtle("blue", 3, 9)
logo_t = make_turtle("blue", 3, 3)
logo_tu = make_turtle("blue", 3, 3)
test = make_turtle("blue", 3, 3)
DELTAX = 20

asteroid_creator(asteroid)
shuttle_initialize(shuttle)
life = 3

for i in range(2000):

    wn.listen()
    wn.onkeypress(spaceship_moving_a, "a")
    wn.onkeypress(spaceship_moving_d, "d")

    y_cor = asteroid.ycor()
    if y_cor <= -300:
        asteroid_creator(asteroid)
        life -= 1

    else:
        asteroid.fd(3)

    if life == 0:
        print("gameover")
        break

wn.mainloop()
