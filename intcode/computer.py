class Logger:
    def __init__(self, name=''):
        if name != '':
            self.text = f'Logger for {name}\n\n'
        else:
            self.text = ''

    def add_log(self, text):
        self.text += text

    def get_log(self):
        return self.text


def analyze(
        instruction_pointer: int,
        intcode: list,
        automatic_mode: bool = False,
        inputs=None,
        logger: Logger = None
):
    if inputs is None:
        inputs = []

    if logger is None:
        logger = Logger()

    input_number = 0
    while instruction_pointer <= len(intcode):
        log = ''
        opcode, first_mode, second_mode, third_mode = define_mode(intcode[instruction_pointer])
        log += f'Intcode = {intcode}\n'
        log += f'Opcode = {opcode}; m1:{first_mode}, m2:{second_mode}, m3:{third_mode}\n'

        if opcode == 99:
            log += f'Break\n'
            return 0, instruction_pointer, intcode, True

        if opcode == 1 or opcode == 2:
            if first_mode == 0:
                num_one = intcode[intcode[instruction_pointer + 1]]
            else:
                num_one = intcode[instruction_pointer + 1]

            if second_mode == 0:
                num_two = intcode[intcode[instruction_pointer + 2]]
            else:
                num_two = intcode[instruction_pointer + 2]

            if opcode == 1:
                result = num_one + num_two
            else:
                result = num_one * num_two

            intcode[intcode[instruction_pointer + 3]] = result
            log += f'Operation = {result} into {intcode[instruction_pointer + 3]}\n'
            instruction_pointer += 4
        elif opcode == 3:
            if automatic_mode:
                insert = inputs.pop(0)
                intcode[intcode[instruction_pointer + 1]] = insert
                log += f'Operation = {insert} into {intcode[instruction_pointer + 1]}\n'
                input_number += 1
            else:
                intcode[intcode[instruction_pointer + 1]] = int(input("Provide input: "))

            instruction_pointer += 2
        elif opcode == 4:
            if first_mode == 0:
                num_one = intcode[intcode[instruction_pointer + 1]]
            else:
                num_one = intcode[instruction_pointer + 1]

            if automatic_mode:
                instruction_pointer += 2
                log += f'Output = {num_one}\n'
                return num_one, instruction_pointer, intcode, False
            else:
                print(num_one)
            instruction_pointer += 2
        elif opcode == 5 or opcode == 6:
            if first_mode == 0:
                num_one = intcode[intcode[instruction_pointer + 1]]
            else:
                num_one = intcode[instruction_pointer + 1]

            if second_mode == 0:
                num_two = intcode[intcode[instruction_pointer + 2]]
            else:
                num_two = intcode[instruction_pointer + 2]

            if (opcode == 5 and num_one != 0) or (opcode == 6 and num_one == 0):
                instruction_pointer = num_two
                log += f'New pointer = {num_two}\n'
            else:
                instruction_pointer += 3
        elif opcode == 7 or opcode == 8:
            if first_mode == 0:
                num_one = intcode[intcode[instruction_pointer + 1]]
            else:
                num_one = intcode[instruction_pointer + 1]

            if second_mode == 0:
                num_two = intcode[intcode[instruction_pointer + 2]]
            else:
                num_two = intcode[instruction_pointer + 2]

            if (opcode == 7 and num_one < num_two) or (opcode == 8 and num_one == num_two):
                intcode[intcode[instruction_pointer + 3]] = 1
                log += f'Operation = 1 into {intcode[instruction_pointer + 3]}\n'
            else:
                intcode[intcode[instruction_pointer + 3]] = 0
                log += f'Operation = 0 into {intcode[instruction_pointer + 3]}\n'

            instruction_pointer += 4
        log += '\n\n'
        logger.add_log(log)

    return 0, instruction_pointer, intcode, True


def define_mode(instruction: int):
    instruction = str(instruction).zfill(5)
    return int(instruction[3:]), int(instruction[2]), int(instruction[1]), int(instruction[0])
