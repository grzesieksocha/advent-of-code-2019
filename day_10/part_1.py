import sys
import copy


def clean(map_to_clean, checked_meteor, vector):
    map_height = len(map_to_clean)
    map_width = len(map_to_clean[0])

    remove_meteor = False
    x = checked_meteor[0]
    y = checked_meteor[1]
    while True:
        x = x + vector[0]
        y = y + vector[1]

        if x < 0 or x > map_width - 1 or y < 0 or y > map_height - 1:
            break

        if map_to_clean[y][x] == '#' and remove_meteor:
            map_to_clean[y][x] = '.'
        elif map_to_clean[y][x] == '#':
            remove_meteor = True

    return map_to_clean


def generate_map_with_visible_meteors(checked_meteor, galaxy_map):
    clean_map = copy.deepcopy(galaxy_map)

    x = checked_meteor[0]
    y = checked_meteor[1]
    clean_map[y][x] = '.'

    map_height = len(clean_map)
    map_width = len(clean_map[0])
    for x in range(map_width * -1, map_width):
        for y in range(map_height * -1, map_height):
            if (x, y) != (0, 0):
                clean(clean_map, checked_meteor, (x, y))

    return clean_map


def check_visible(point, galaxy_map):
    num_of_visible_meteors = 0
    map_with_visible_meteors = generate_map_with_visible_meteors(point, galaxy_map)

    for y, row in enumerate(map_with_visible_meteors):
        for x, checked_point in enumerate(row):
            if checked_point == '#':
                num_of_visible_meteors += 1
    return num_of_visible_meteors


def solve_part_1():
    galaxy_map = []
    with open(sys.path[0] + '/day_10/input.txt', 'r') as f:
        for line in f:
            galaxy_map.append(list(line.rstrip('\n')))

    num_of_visible_meteors = []
    for y, row in enumerate(galaxy_map):
        for x, checked_point in enumerate(row):
            if checked_point == '#':
                num_of_visible_meteors.append([(x, y), check_visible((x, y), galaxy_map)])

    max_number = 0
    point = None
    for pair in num_of_visible_meteors:
        if pair[1] > max_number:
            max_number = pair[1]
            point = pair[0]

    print(f'{max_number} in {point}')
