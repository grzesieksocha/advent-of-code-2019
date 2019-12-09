from intcode.computer import analyze
from intcode.computer import Logger
import sys


def solve_part_1():
    intcode = list(map(int, open(sys.path[0] + '/day_9/input.txt').read().split(sep=',')))
    logger = Logger('9')
    analyze(0, intcode, False, None, logger)

    with open('./log', 'w+') as file:
        file.write(logger.get_log())
