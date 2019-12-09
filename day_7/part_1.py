from intcode.computer import analyze
from itertools import permutations
import sys


def solve_part_1():
    intcode = list(map(int, open(sys.path[0] + '/day_7/input.txt').read().split(sep=',')))
    phase_sequences = permutations(range(5))
    signals = []
    for phase in phase_sequences:
        amp_a_output, index_b, intcode_b, last_signal_b = analyze(0, intcode, True, [phase[0], 0])
        amp_b_output, index_b, intcode_b, last_signal_b = analyze(0, intcode, True, [phase[1], amp_a_output])
        amp_c_output, index_b, intcode_b, last_signal_b = analyze(0, intcode, True, [phase[2], amp_b_output])
        amp_d_output, index_b, intcode_b, last_signal_b = analyze(0, intcode, True, [phase[3], amp_c_output])
        amp_e_output, index_b, intcode_b, last_signal_b = analyze(0, intcode, True, [phase[4], amp_d_output])

        signals.append(amp_e_output)
    return max(signals)
