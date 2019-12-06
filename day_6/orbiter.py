def count_orbits(orbits_map: list):
    orbits = {}
    for pair in orbits_map:
        orbited, orbiting = pair.split(')')
        if orbiting in orbits:
            orbits[orbiting].append(orbited)
        else:
            orbits[orbiting] = [orbited]

        if orbited in orbits:
            orbits[orbiting] += orbits[orbited]

        for previously_orbiting, previously_orbited in orbits.items():
            if orbiting in previously_orbited:
                orbits[previously_orbiting] += orbits[orbiting]

    count = 0
    for orbited in orbits.values():
        count += len(orbited)

    return count, orbits
