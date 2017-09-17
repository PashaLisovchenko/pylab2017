import argparse
import turtle


def analysis(text):
    dct = {}
    for i in text:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct

myWin = turtle.Screen()


def sectors(turtle, text):
    dct = analysis(text)
    len_dct = len(dct)
    radius = 150
    sector = 360 / len(text)
    percentages = []
    step = 20
    colors = ['blue', 'red', 'green', 'brown', 'yellow', 'violet', 'orange']
    for key in dct:
        percentages.append(dct[key] * sector)

        turtle.penup()
        turtle.setpos(200, 200 - step)
        step = step + 20
        turtle.pendown()
        turtle.color(colors[len_dct-1])
        turtle.begin_fill()

        turtle.dot()
        turtle.write(key + " - ", True, font=("Arial", 10, "normal"))
        turtle.write(str(dct[key]) + " time(-s)", True, font=("Arial", 10, "normal"))

        turtle.end_fill()
        turtle.penup()
        len_dct = len_dct - 1

    left = 90
    rollingPercent = 0
    turtle.home()
    len_dct1 = len(dct)
    for percent in percentages:
        rollingPercent += percent
        turtle.pendown()
        turtle.color(colors[len_dct1-1])
        turtle.begin_fill()

        turtle.fd(radius)
        turtle.left(left)
        turtle.circle(radius, percent)
        turtle.left(left)
        turtle.home()
        turtle.left(rollingPercent)

        turtle.end_fill()
        turtle.penup()
        len_dct1 = len_dct1 - 1


def rays(turtle, text):
    colors = ['blue', 'red', 'green', 'brown', 'yellow', 'violet', 'orange']
    dct = analysis(text)
    len_dct = len(dct)
    radius = 75
    sector = 360 / len_dct
    rollingPercent = 0
    for key in dct:
        rollingPercent += sector
        turtle.pendown()
        turtle.color(colors[len_dct - 1])

        if radius * dct[key] > radius:
            m = (radius * dct[key]) / radius
            for i in range(int(m)):
                turtle.fd(radius)
                turtle.circle(2)
        else:
            turtle.fd(radius * dct[key])
            turtle.circle(2)

        turtle.penup()

        turtle.write(key, True, font=("Arial", 10, "normal"))
        turtle.home()
        turtle.left(rollingPercent)

        turtle.penup()
        len_dct = len_dct - 1


parser = argparse.ArgumentParser()
parser.add_argument('dtype', choices=['sectors', 'rays'])
parser.add_argument('-text', type=str, nargs='+')
args = parser.parse_args('sectors -text hello hello world hello world nice to meet you'.split())
dict_args = vars(args)

types = {
    sectors.__name__: sectors,
    rays.__name__: rays
}

my_turtle = turtle.Turtle()
text = dict_args["text"]
types[dict_args["dtype"]](my_turtle, text)

myWin.exitonclick()
