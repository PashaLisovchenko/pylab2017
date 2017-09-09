import turtle
import random


def move(x, y, xn, yn):
    x = (x + xn) / 2
    y = (y + yn) / 2
    return x, y


def chaos_method(my_triangle, my_points):
    DOT_MARK_WIDTH = 2
    DRAW_SPEED = 10
    COUNT_DOT = 20000
    CHANCE_GET_IN_FP = 10
    CHANCE_GET_IN_SP = 20
    x = 0
    y = 0
    my_triangle.penup()
    my_triangle.setpos(x, y)
    my_triangle.pendown()
    my_triangle.speed(DRAW_SPEED)
    for i in range(COUNT_DOT):
        rand = random.randint(1, 30)
        if rand < CHANCE_GET_IN_FP:
            my_triangle.penup()
            x, y = move(x, y, my_points[0][0], my_points[0][1])
            my_triangle.setpos(x,y)
            my_triangle.pendown()
            my_triangle.dot(DOT_MARK_WIDTH)
        elif rand < CHANCE_GET_IN_SP:
            my_triangle.penup()
            x, y = move(x, y, my_points[1][0], my_points[1][1])
            my_triangle.setpos(x, y)
            my_triangle.pendown()
            my_triangle.dot(DOT_MARK_WIDTH)
        else:
            my_triangle.penup()
            x, y = move(x, y, my_points[2][0], my_points[2][1])
            my_triangle.setpos(x, y)
            my_triangle.pendown()
            my_triangle.dot(DOT_MARK_WIDTH)
    my_triangle.getscreen().mainloop()

def draw_triangle(points, my_turtle):
    my_turtle.up()
    my_turtle.goto(points[0][0],points[0][1])
    my_turtle.down()
    my_turtle.goto(points[1][0],points[1][1])
    my_turtle.goto(points[2][0],points[2][1])
    my_turtle.goto(points[0][0],points[0][1])


def get_mid(p1, p2):
    x = (p1[0] + p2[0]) / 2
    y = (p1[1] + p2[1]) / 2
    return x, y


def iterative(points, degree, my_turtle):
    draw_triangle(points, my_turtle)
    if degree > 0:
        iterative([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   degree-1, my_turtle)
        iterative([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                   degree-1, my_turtle)
        iterative([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                   degree-1, my_turtle)


def sierpinski_triangle(my_points, **kwargs):
    my_triangle = turtle.Turtle()
    if 'method' in kwargs:
        if kwargs['method'] == 'chaos':
            chaos_method(my_triangle, my_points)
        elif kwargs['method'] == 'iter':
            if 'degree' in kwargs:
                iterative(my_points, kwargs["degree"], my_triangle)
            else:
                iterative(my_points, 2, my_triangle)
    else:
        chaos_method(my_triangle, my_points)


my_points = [[-200, -100], [0, 200], [200, -100]]
myWin = turtle.Screen()
sierpinski_triangle(my_points, method="iter")
myWin.exitonclick()