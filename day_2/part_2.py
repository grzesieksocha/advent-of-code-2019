from intcode.computer import analyze
import sys


def solve_part_2():
    base_intcode = list(map(int, open(sys.path[0] + '/day_2/input.txt').read().split(sep=',')))
    noun = 0
    verb = 0
    for i in range(100):
        for j in range(100):
            intcode = base_intcode.copy()
            intcode[1] = i
            intcode[2] = j
            if analyze(intcode)[0] == 19690720:
                noun = i
                verb = j

    return noun, verb
