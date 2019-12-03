import sys
from day_3.distance_measure import path_creator, find_intersections_for, get_min_distance_from_center_for_points


def solve_part_1():
    paths = []
    with open(sys.path[0] + '/day_3/input.txt') as f:
        for line in f.readlines():
            paths.append(line.split(sep=','))

    return get_min_distance_from_center_for_points(
        find_intersections_for(
            path_creator(paths[0]),
            path_creator(paths[1])
        )[0]
    )
