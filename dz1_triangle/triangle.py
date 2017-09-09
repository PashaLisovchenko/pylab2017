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


def sierpinski_triangle(my_points, **kwargs):
    my_triangle = turtle.Turtle()
    if 'method' in kwargs:
        if kwargs['method'] == 'chaos':
            chaos_method(my_triangle, my_points)
        elif kwargs['method'] == 'iter':
            pass
            # iterative(my_triangle, my_points)
    else:
        chaos_method(my_triangle, my_points)

my_points = [[-200, -100], [0, 100], [200, -100]]
sierpinski_triangle(my_points)
