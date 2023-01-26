import collisions
import vector_math
import data


def convert_to_int(number):
    num = int(number * 255)
    if num > 255:
        return 255
    else:
        return num

def cast_ray(ray, sphere_list, color, light, point):
    collisions_list = collisions.find_intersection_points(sphere_list, ray)
    if collisions_list:
        smallest_dist = vector_math.length_vector(vector_math.difference_vector(collisions_list[0][1], ray.pt))
        sphere = collisions_list[0][0]
        smallest_index = 0
        for i in range(len(collisions_list)):
            if vector_math.length_vector(vector_math.difference_vector(collisions_list[i][1], ray.pt)) < smallest_dist:
                smallest_index = i
                smallest_dist = vector_math.length_vector(vector_math.difference_vector(collisions_list[i][1], ray.pt))
                sphere = collisions_list[i][0]
        normal = collisions.sphere_normal_at_point(collisions_list[smallest_index][0],
                                                   collisions_list[smallest_index][1])
        scalar = vector_math.scale_vector(normal, .01)
        pe = vector_math.translate_point(collisions_list[smallest_index][1], scalar)
        light_dir = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.pt))
        dot_vector1 = vector_math.dot_vector(normal, light_dir)
        reflect_vector = vector_math.difference_vector(light_dir, vector_math.scale_vector(normal, (2 * dot_vector1)))
        vector_dir = vector_math.normalize_vector(vector_math.vector_from_to(point, pe))
        specular = vector_math.dot_vector(reflect_vector, vector_dir)
        r = 0
        g = 0
        b = 0

        # find the correct color of the spheres, shadows, and finishes
        if dot_vector1 > 0:
            pe_ray = data.Ray(pe, light_dir)
            ray_intersections = collisions.find_intersection_points(sphere_list, pe_ray)
            if ray_intersections == []:
                r = r + dot_vector1*light.color.r*sphere.color.r*color.r*sphere.finish.diffuse
                g = g + dot_vector1*light.color.g*sphere.color.g*color.g*sphere.finish.diffuse
                b = b + dot_vector1*light.color.b*sphere.color.b*color.b*sphere.finish.diffuse

                if specular > 0:
                    r = r + light.color.r*sphere.finish.specular*(specular**(1.0/sphere.finish.roughness))
                    g = g + light.color.g*sphere.finish.specular*(specular**(1.0/sphere.finish.roughness))
                    b = b + light.color.b*sphere.finish.specular*(specular**(1.0/sphere.finish.roughness))
        r = r + sphere.color.r*color.r*sphere.finish.ambient
        g = g + sphere.color.g*color.g*sphere.finish.ambient
        b = b + sphere.color.b*color.b*sphere.finish.ambient

        # cases if color values > 1
        if r > 1:
            r = 1
        if g > 1:
            g = 1
        if b > 1:
            b = 1

        return data.Color(r, g, b)
    else:
        return data.Color(1, 1, 1)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
    image = open("image.ppm", "w")
    image.write("P3\n")
    image.write(str(width) + " " + str(height) + "\n")
    image.write("255\n")
    x_calc = (max_x - min_x)/float(width)
    y_calc = (max_y - min_y)/float(height)
    for h in range(height):
        for w in range(width):
            x = min_x + x_calc * w
            y = max_y - y_calc * h
            z = 0
            ray = data.Ray(eye_point, vector_math.difference_point(data.Point(x, y, z), eye_point))
            color_output = cast_ray(ray, sphere_list, color, light, eye_point)
            image.write(str(convert_to_int(color_output.r)) + " ")
            image.write(str(convert_to_int(color_output.g)) + " ")
            image.write(str(convert_to_int(color_output.b)) + "\n")
    image.close()
