import collections
Point = collections.namedtuple('Point', 'x y')

colors = ['blue', 'red', 'green', 'brown', 'yellow', 'violet', 'orange']


def is_not_int(s):
    try:
        int(s)
        return False
    except ValueError:
        return True


def input_coord():
    x = input('Input coord X: ')
    while is_not_int(x):
        x = input('Input correct coord X: ')
    y = input('Input coord Y: ')
    while is_not_int(y):
        y = input('Input correct coord Y: ')
    return Point(int(x), int(y))


def input_color():
    color = input("Input color: ")
    while color not in colors:
        color = input("Color not found. Please repeat: ")
    return str(color)


def input_parameter(figure):
    if figure == 'circle':
        parameter_str = "radius"
    else:
        parameter_str = "side length"
    parameter = input("Input {}: ".format(parameter_str))
    while is_not_int(parameter):
        parameter = input('Input correct {}: '.format(parameter_str))
    return int(parameter)
