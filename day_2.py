from day_2.part_1 import solve_part_1
from day_2.part_2 import solve_part_2


def main():
    part_1_solution = solve_part_1()
    part_2_solution = solve_part_2()

    print(f'day 2 - part 1: {part_1_solution}')
    print(f'day 2 - part 2: {100 * part_2_solution[0] + part_2_solution[1]}')


main()
