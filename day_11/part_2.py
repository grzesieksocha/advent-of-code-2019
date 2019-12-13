import sys
from operator import itemgetter
from math import atan2, hypot


def solve_part_2(station):
    galaxy_map = []
    with open(sys.path[0] + '/day_10/input.txt', 'r') as f:
        for line in f:
            galaxy_map.append(list(line.rstrip('\n')))

    meteors = get_meteors(galaxy_map, station)
    q1, q2, q3, q4 = split_into_quadrants(meteors)

    shots = 0
    result = None
    while len(q1) > 0 or len(q2) > 0 or len(q3) > 0 or len(q4) > 0:
        q1, result, shots = shoot(q1, result, shots)
        q2, result, shots = shoot(q2, result, shots)
        q3, result, shots = shoot(q3, result, shots)
        q4, result, shots = shoot(q4, result, shots)

    print(result[0][0] + station[0], station[1] - result[0][1])
    print((result[0][0] + station[0]) * 100 + (station[1] - result[0][1]))


def get_meteors(galaxy_map, station):
    map_height = len(galaxy_map)
    map_width = len(galaxy_map[0])

    meteors = [
        [
            (x - station[0], station[1] - y),
            atan2(station[1] - y, x - station[0]),
            hypot(x - station[0], station[1] - y)
        ]
        for y in range(map_height)
        for x in range(map_width)
        if galaxy_map[y][x] == '#'
    ]

    meteors.pop(meteors.index([(0, 0), 0.0, 0.0]))
    return meteors


def split_into_quadrants(meteors):
    q1 = []
    q2 = []
    q3 = []
    q4 = []

    for meteor in meteors:
        if meteor[0][0] >= 0 and meteor[0][1] > 0:
            q1.append(meteor)
        if meteor[0][0] > 0 and meteor[0][1] <= 0:
            q2.append(meteor)
        if meteor[0][0] <= 0 and meteor[0][1] < 0:
            q3.append(meteor)
        if meteor[0][0] < 0 and meteor[0][1] >= 0:
            q4.append(meteor)

    q1.sort(key=itemgetter(2))
    q1.sort(key=itemgetter(1), reverse=True)

    q2.sort(key=itemgetter(2))
    q2.sort(key=itemgetter(1), reverse=True)

    q3.sort(key=itemgetter(2))
    q3.sort(key=itemgetter(1), reverse=True)

    q4.sort(key=itemgetter(2))
    q4.sort(key=itemgetter(1), reverse=True)

    return q1, q2, q3, q4


def shoot(q1, result, shots):
    last_shot = None

    for key, meteor in enumerate(q1):
        if last_shot is None or last_shot != meteor[1]:
            shots += 1
            if shots == 200:
                result = meteor
            q1[key] = None
            last_shot = meteor[1]

    q1 = list(filter(None, q1))

    return q1, result, shots
