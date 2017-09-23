import random
import turtle


rand = lambda: random.randint(0, 255)


def coefs(eq_count, range):
    all_coef = list()
    while len(all_coef) <= eq_count:
        coef = {key: random.uniform(-range, range) for key in ['a', 'b', 'c', 'd', 'e', 'f']}
        coef['color'] = rand(), rand(), rand()
        if ((coef['a'] ** 2 + coef['d'] ** 2) < 1
            and (coef['b'] ** 2 + coef['e'] ** 2) < 1
            and (coef['a'] ** 2 + coef['b'] ** 2 + coef['d'] ** 2 + coef['e'] ** 2)
                < 1 + (coef['a'] * coef['e'] - coef['b'] * coef['d']) ** 2):
            all_coef.append(coef)
    return all_coef


def rendering(n, eq_count, it, x_res, y_res):
    pixels = {}
    coef = coefs(eq_count, 1)
    XMIN = -1.777
    XMAX = 1.777
    YMIN = -1
    YMAX = 1

    for num in range(0, n):
        newX = random.uniform(XMIN, XMAX)
        newY = random.uniform(YMIN, YMAX)
        for step in range(-20, it):
            i = random.randint(0, eq_count)
            newX = coef[i]['a'] * newX + coef[i]['b'] * newY + coef[i]['c']
            newY = coef[i]['d'] * newX + coef[i]['e'] * newY + coef[i]['f']
            if step >= 0:
                x1 = x_res - int(((XMAX - newX) / (XMAX - XMIN)) * x_res)
                y1 = y_res - int(((YMAX - newY) / (YMAX - YMIN)) * y_res)
                if x1 < x_res and y1 < y_res:
                    if not pixels.get((x1, y1)):
                        pixels[(x1, y1)] = {'color': (coef[i]['color']), 'counter': 1}
                    else:
                        pixels[(x1, y1)]['color'] = tuple(int((pixels[(x1, y1)]['color'][n] + coef[i]['color'][n]) / 2)
                                                          for n in range(3))
                        pixels[(x1, y1)]['counter'] += 1
    return pixels


def flame():
    my_turtle = turtle.Turtle()
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor('black')
    my_turtle.speed(10)
    my_turtle.penup()
    dots = rendering(100, 10, 100, 600, 600)
    for i in dots.keys():
        my_turtle.goto(i[0] - 400 / 2, i[1] - 300 / 2)
        my_turtle.color(dots[i]['color'])
        my_turtle.dot(2)

flame()
input()