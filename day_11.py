from day_11.part_1 import solve_part_1


def main():
    print(f'day 11 - part 1:')
    colors = solve_part_1(0)
    print(len(set(colors.keys())))

    print(f'day 11 - part 2:')
    colors = solve_part_1(1)

    with open('./picture.txt', 'w') as file:
        for x in range(-10, 50):
            for y in range(-10, 50):
                if (x, y) in colors:
                    if colors[(x, y)] == 0:
                        paint = ' '
                    else:
                        paint = 'X'
                else:
                    paint = ' '

                file.write(paint)
            file.write('\n')


main()
