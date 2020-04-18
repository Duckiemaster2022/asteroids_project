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
    asteroid.shape("circle")
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


def init_laser():
    laser.shape("square")
    laser.shapesize(0.2, 1)
    laser.pu()
    laser.seth(90)
    laser.sety(shuttle.ycor())
    laser.sety(shuttle.ycor())


def spaceship_laser():
    laser.hideturtle()
    laser.setx(shuttle.xcor())
    laser.setx(shuttle.xcor())
    laser.sety(shuttle.ycor())
    laser.sety(shuttle.ycor())
    laser.showturtle()
    laser.fd(1)


def init_life_meter():
    life_meter.pu()
    life_word_display.pu()
    life_meter.setpos(-295, 300)
    life_word_display.setpos(-338, 300)
    life_word_display.write("Lives", font=("Arial", 11, "normal"))
    life_word_display.setpos(-305, 300)
    life_word_display.write(" : ", font=("Arial", 11, "normal"))


wn = make_window("black", "Squares Everywhere!")
shuttle = make_turtle("lightslategrey", 3, 5)
asteroid = make_turtle("dimgray", 3, 1)
logo_t = make_turtle("blue", 3, 3)
logo_tu = make_turtle("blue", 3, 3)
life_meter = make_turtle("lime", 3, 3)
laser = make_turtle("red", 1, 5)
life_word_display = make_turtle("lime", 3, 3)
DELTAX = 10


logo(logo_t, logo_tu)
asteroid_creator(asteroid)
shuttle_initialize(shuttle)
init_laser()
init_life_meter()
life = 3

while True:

    wn.listen()
    wn.onkeypress(spaceship_moving_a, "a")
    wn.onkeypress(spaceship_moving_d, "d")
    wn.onkeypress(spaceship_laser, "space")

    y_cor = asteroid.ycor()
    y_cor_20 = asteroid.ycor() + 10
    y_cor_min_20 = asteroid.ycor() - 10
    x_cor_20 = asteroid.xcor() + 10
    x_cor_min_20 = asteroid.xcor() - 10
    x_cor_laser = laser.xcor()
    y_cor_laser = laser.ycor()
    y_cor_shuttle = shuttle.ycor()

    if y_cor_laser <= y_cor_20 and y_cor_laser >= y_cor_min_20 and \
            x_cor_laser <= x_cor_20 and x_cor_laser >= x_cor_min_20:
        asteroid.hideturtle()
        asteroid_creator(asteroid)
        laser.hideturtle()

    if y_cor_laser > y_cor_shuttle and y_cor_laser <= 300:
        laser.fd(5)
    else:
        laser.hideturtle()

    if y_cor <= -300:
        asteroid_creator(asteroid)
        life_meter.clear()
        life -= 1
    else:
        asteroid.fd(4)

    if life == 0:
        print("gameover")
        life_meter.write("0", font=("Arial", 10, "normal"))
        break

    life_meter.write(life, font=("Arial", 10, "normal"))



