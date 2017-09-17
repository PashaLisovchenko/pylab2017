from dz5_consolePaint import param


def console(dct):
    while True:
        buffer_command = []
        command = input("Enter command ({}) : ".format((",").join(dct.keys())))
        try:
            while command not in dct.keys():
                command = input("Error repeat command ({}) : ".format((",").join(dct.keys())))
            buffer_command.append(command)
            v_command = input("Enter command '{}' ({}) : ".format(command, (",").join(dct[command].keys())))
            while v_command not in dct[command].keys():
                v_command = input("Error repeat command '{}' ({}) : ".format(command, (",").join(dct[command].keys())))
            buffer_command.append(v_command)
            try:
                print("Enter parameter '{}' ({}) : ".format(v_command, (",").join(dct[command][v_command].keys())))
                for key in dct[command][v_command].keys():
                    if key == "coord":
                        point = param.input_coord()
                        buffer_command.append(point)
                    elif key == "color":
                        color = param.input_color()
                        buffer_command.append(color)
                    else:
                        parameter = param.input_parameter(v_command)
                        buffer_command.append(parameter)
                yield buffer_command
            except AttributeError:
                file = input(dct[command][v_command])
                buffer_command.append(file)
                yield buffer_command
        except AttributeError:
            buffer_command.append(command)
            yield buffer_command