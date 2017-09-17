from dz5_consolePaint import gen
import turtle
import json

dct = {
    'open': {
        'file_view': "Enter name file: ",
        'file_change': "Enter name file_change: ",
    },
    'save': {
        'file': "Enter name file: ",
    },
    'draw': {
        'circle': {
            'coord': (),
            'color': "",
            'r': 0,
        },
        'square': {
            'coord': (),
            'color': "",
            'length': 0,
        }
    },
    'exit': ''
}


def analyzer(command, *args):
    if command[0] == 'save':
        save(command, args[0])
    if command[0] == 'draw':
        draw(command)
    if command[0] == 'open':
        open_file(command)


def draw(command):
    t = turtle.Turtle()
    if command[1] == 'circle':
        t.penup()
        t.setpos(command[2])
        t.pendown()
        t.color(command[3])
        t.begin_fill()
        t.circle(command[4])
        t.end_fill()
    else:
        t.penup()
        t.setpos(command[2])
        t.pendown()
        t.color(command[3])
        t.begin_fill()
        t.fd(command[4])
        t.left(90)
        t.fd(command[4])
        t.left(90)
        t.fd(command[4])
        t.left(90)
        t.fd(command[4])
        t.end_fill()


def save(command, save_command):
    filename = command[2]
    with open(filename, 'w') as f:
        json.dump(save_command, f)


def open_file(command):
    filename = command[2]
    try:
        with open(filename, 'r') as f:
            json_data = json.load(f)
            for comm in json_data:
                analyzer(comm)
            return json_data
    except FileNotFoundError:
        print("File Not Found")


cli = gen.console(dct)
save_command = []

while True:
    command = next(cli)
    print(command)
    if command[0] == 'exit':
        break
    else:
        if command[0] == 'draw':
            save_command.append(command)
        if command[1] == 'file_change':
            j = open_file(command)
            try:
                for comm in j:
                    save_command.append(comm)
                continue
            except TypeError:
                continue
        analyzer(command, save_command)
        if command[0] == 'save':
            print("Clear buffer")
            save_command = []
