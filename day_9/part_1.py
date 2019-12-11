from intcode.computer import analyze
import sys


def solve_part_1():
    intcode = list(map(int, open(sys.path[0] + '/day_9/input.txt').read().split(sep=',')))
    analyze(0, intcode)
