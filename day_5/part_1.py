from intcode.computer import analyze
import sys


def solve_part_1():
    intcode = list(map(int, open(sys.path[0] + '/day_5/input.txt').read().split(sep=',')))
    return analyze(intcode)
