from data import *
from ray_caster import *

command_list = ["-eye", "-view", "-light", "-ambient"]


def not_com(value):
    for x in command_list:
        if x == value:
            return False
    return True


def parse_command_line(argv):
    if len(argv) < 1:
        print("usage: python ray_caster.py <filename> [-eye x y z][-view\
min_x max_x min_y max_y width height][-light x y z r g b] [-ambient r g b]")
        exit()

    file_name = argv[1]

    light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
    eye_point = Point(0.0, 0.0, -14.0)
    min_x = -10
    max_x = 10
    min_y = -7.5
    max_y = 7.5
    width = 512
    height = 384
    ambient_light = Color(1.0, 1.0, 1.0)
    sphere_list = get_sphere_list(file_name)

    for i in range(len(argv)):
        if argv[i] == "-eye":
            if i + 1 < len(argv) and not_com(argv[i + 1]):
                eye_point.pt.x = float_default(argv[i + 1], eye_point.pt.x)
            else:
                print("Issue in -eye arg 1")
            if i + 2 < len(argv) and not_com(argv[i + 2]):
                eye_point.pt.y = float_default(argv[i + 2], eye_point.pt.y)
            else:
                print("Issue in -eye arg 2")
            if i + 3 < len(argv) and not_com(argv[i + 3]):
                eye_point.pt.z = float_default(argv[i + 3], eye_point.pt.z)
            else:
                print("Issue in -eye arg 3")

    for i in range(len(argv)):
        if argv[i] == "-view":
            if i + 1 < len(argv) and not_com(argv[i + 1]):
                min_x = float_default(argv[i + 1], min_x)
            else:
                print("Issue in -eye arg 1")
            if i + 2 < len(argv) and not_com(argv[i + 2]):
                max_x = float_default(argv[i + 2], max_x)
            else:
                print("Issue in -view arg 2")
            if i + 3 < len(argv) and not_com(argv[i + 3]):
                min_y = float_default(argv[i + 3], min_y)
            else:
                print("Issue in -view arg 3")
            if i + 4 < len(argv) and not_com(argv[i + 4]):
                max_y = float_default(argv[i + 4], max_y)
            else:
                print("Issue in -view arg 4")
            if i + 5 < len(argv) and not_com(argv[i + 5]):
                width = int(float_default(argv[i + 5], width))
            else:
                print("Issue in -view arg 5")
            if i + 6 < len(argv) and not_com(argv[i + 6]):
                height = int(float_default(argv[i + 6], height))
            else:
                print("Issue in -view arg 6")

    for i in range(len(argv)):
        if argv[i] == "-light":
            if i + 1 < len(argv) and not_com(argv[i + 1]):
                light.pt.x = float_default(argv[i + 1], light.pt.x)
            else:
                print("Issue in -light arg 1")
            if i + 2 < len(argv) and not_com(argv[i + 2]):
                light.pt.y = float_default(argv[i + 2], light.pt.y)
            else:
                print("Issue in -light arg 2")
            if i + 3 < len(argv) and not_com(argv[i + 3]):
                light.pt.z = float_default(argv[i + 3], light.pt.z)
            else:
                print("Issue in -light arg 3")
            if i + 4 < len(argv) and not_com(argv[i + 4]):
                light.color.r = float_default(argv[i + 4], light.color.r)
            else:
                print("Issue in -light arg 4")
            if i + 5 < len(argv) and not_com(argv[i + 5]):
                light.color.g = float_default(argv[i + 5], light.color.g)
            else:
                print("Issue in -light arg 5")
            if i + 6 < len(argv) and not_com(argv[i + 6]):
                light.color.b = float_default(argv[i + 6], light.color.b)
            else:
                print("Issue in -light arg 6")

    for i in range(len(argv)):
        if argv[i] == "-ambient":
            if i + 1 < len(argv) and not_com(argv[i + 1]):
                ambient_light.color.r = float_default(argv[i + 1], ambient_light.color.r)
            else:
                print("Issue in -amb arg 1")
            if i + 2 < len(argv) and not_com(argv[i + 2]):
                ambient_light.color.g = float_default(argv[i + 2], ambient_light.color.g)
            else:
                print("Issue in -amb arg 2")
            if i + 3 < len(argv) and not_com(argv[i + 3]):
                ambient_light.color.b = float_default(argv[i + 3], ambient_light.color.b)
            else:
                print("Issue in -light arg 3")

    cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point,
                  sphere_list, ambient_light, light)