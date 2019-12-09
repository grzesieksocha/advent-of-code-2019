from itertools import permutations
from intcode.computer import analyze
from intcode.computer import Logger
import sys


def solve_part_2():
    intcode = list(map(int, open(sys.path[0] + '/day_7/input.txt').read().split(sep=',')))
    phase_sequences = permutations([5, 6, 7, 8, 9])
    signals = []

    intcode_a = intcode.copy()
    intcode_b = intcode.copy()
    intcode_c = intcode.copy()
    intcode_d = intcode.copy()
    intcode_e = intcode.copy()

    logger_a = Logger('A')
    logger_b = Logger('B')
    logger_c = Logger('C')
    logger_d = Logger('D')
    logger_e = Logger('E')

    for phase in phase_sequences:
        e_signals = []
        index_a = 0
        input_a = [phase[0], 0]
        index_b = 0
        index_c = 0
        index_d = 0
        index_e = 0
        first_inputs = True
        test_completed = False
        run = 1
        while not test_completed:
            logger_a.add_log(f'Run: {run}\n')
            logger_b.add_log(f'Run: {run}\n')
            logger_c.add_log(f'Run: {run}\n')
            logger_d.add_log(f'Run: {run}\n')
            logger_e.add_log(f'Run: {run}\n')
            amp_a_output, index_a, intcode_a, last_signal_a = analyze(index_a, intcode_a, True, input_a, logger_a)

            if first_inputs:
                input_b = [phase[1], amp_a_output]
            else:
                input_b = [amp_a_output]

            amp_b_output, index_b, intcode_b, last_signal_b = analyze(index_b, intcode_b, True, input_b, logger_b)
            if first_inputs:
                input_c = [phase[2], amp_b_output]
            else:
                input_c = [amp_b_output]

            amp_c_output, index_c, intcode_c, last_signal_c = analyze(index_c, intcode_c, True, input_c, logger_c)
            if first_inputs:
                input_d = [phase[3], amp_c_output]
            else:
                input_d = [amp_c_output]

            amp_d_output, index_d, intcode_d, last_signal_d = analyze(index_d, intcode_d, True, input_d, logger_d)
            if first_inputs:
                input_e = [phase[4], amp_d_output]
            else:
                input_e = [amp_d_output]

            amp_e_output, index_e, intcode_e, test_completed = analyze(index_e, intcode_e, True, input_e, logger_e)
            run += 1
            e_signals.append(amp_e_output)
            first_inputs = False
            input_a = [amp_e_output]

        signals.append(max(e_signals))

        with open('./Log A', 'w+') as file:
            file.write(logger_a.get_log())

        with open('./Log B', 'w+') as file:
            file.write(logger_b.get_log())

    return max(signals)
