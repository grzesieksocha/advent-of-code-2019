import sys
from day_3.distance_measure import path_creator, find_intersections_for, get_min_distance_from_center_for_points


def solve_part_2():
    paths = []
    with open(sys.path[0] + '/day_3/input.txt') as f:
        for line in f.readlines():
            paths.append(line.split(sep=','))

    path1 = path_creator(paths[0])
    path2 = path_creator(paths[1])

    intersections = find_intersections_for(path1, path2)

    steps = []
    for intersection in intersections:
        key1 = path1.index(intersection) + 1
        key2 = path2.index(intersection) + 1
        steps.append(key1 + key2)

    return min(steps)
