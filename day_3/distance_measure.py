def path_creator(movements: list) -> list:
    x = 0
    y = 0
    all_points = []
    for move in movements:
        direction = move[0]
        steps = int(move[1:])

        if direction == 'R':
            for step in range(steps):
                x += 1
                all_points.append((x, y))

        elif direction == 'D':
            for step in range(steps):
                y -= 1
                all_points.append((x, y))

        elif direction == 'U':
            for step in range(steps):
                y += 1
                all_points.append((x, y))

        elif direction == 'L':
            for step in range(steps):
                x -= 1
                all_points.append((x, y))

    return all_points


def find_intersections_for(path1: list, path2: list) -> set:
    intersections = []
    for point in set(path1):

        if point in set(path2):
            intersections.append(point)

    return set(intersections)


def get_min_distance_from_center_for_points(points: set) -> int:
    distances = []
    for point in points:
        distances.append(abs(point[0]) + abs(point[1]))

    return min(distances)
