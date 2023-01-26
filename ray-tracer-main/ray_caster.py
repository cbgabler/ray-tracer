from cast import *
import commandline
from sys import *


def main():
    commandline.parse_command_line(argv)


def float_default(string, default):
    try:
        return float(string)
    except:
        return default


def get_sphere(string):
    value_list = string.split()

    try:
        x = float(value_list[0])
        y = float(value_list[1])
        z = float(value_list[2])
        radius = float(value_list[3])
        r = float(value_list[4])
        g = float(value_list[5])
        b = float(value_list[6])
        ambient = float(value_list[7])
        diffuse = float(value_list[8])
        specular = float(value_list[9])
        roughness = float(value_list[10])

        return data.Sphere(data.Point(x, y, z), radius, data.Color(r, g, b), data.Finish(ambient,
                                                                                         diffuse, specular, roughness))

    except:
        print('Error')


def get_sphere_list(file_name):
    line_count = 0

    sphere_list = []
    in_file = open(file_name, 'r')
    for line in in_file:
        line_count += 1
        sphere = get_sphere(line)
        try:
            sphere_list.append(sphere)
        except:
            print('malformed sphere on line' + line_count + '... skipping')

    return sphere_list


if __name__ == '__main__':
    main()