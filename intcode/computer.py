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


def get_key(mode, intcode, instruction_pointer, offset, relative_base):
    if mode == 0:  # position
        key = intcode[instruction_pointer + offset]
    elif mode == 1:  # immediate
        key = instruction_pointer + offset
    else:  # relative
        key = relative_base + intcode[instruction_pointer + offset]

    return key


def get_value(mode, intcode, instruction_pointer, offset, relative_base):
    return intcode[get_key(mode, intcode, instruction_pointer, offset, relative_base)]


def analyze(
        instruction_pointer: int,
        relative_base: int,
        intcode: list,
        automatic_mode: bool = False,
        inputs=None,
        logger: Logger = None
):
    if inputs is None:
        inputs = []

    input_number = 0
    while instruction_pointer <= len(intcode):
        log = ''
        opcode, first_mode, second_mode, third_mode = define_mode(intcode[instruction_pointer])
        log += f'Intcode = {intcode}\n'
        log += f'Instruction = {intcode[instruction_pointer]}\n'
        log += f'Opcode = {opcode}; m1:{first_mode}, m2:{second_mode}, m3:{third_mode}\n'

        if opcode == 99:
            log += f'Break\n'
            return 0, instruction_pointer, relative_base, True

        if opcode == 1 or opcode == 2:
            num_one = get_value(first_mode, intcode, instruction_pointer, 1, relative_base)
            num_two = get_value(second_mode, intcode, instruction_pointer, 2, relative_base)

            if opcode == 1:
                result = num_one + num_two
            else:
                result = num_one * num_two

            key = get_key(third_mode, intcode, instruction_pointer, 3, relative_base)
            intcode[key] = result
            log += f'Operation = {result} into {key}\n'
            instruction_pointer += 4
        elif opcode == 3:
            if automatic_mode:
                insert = inputs.pop(0)
                intcode[intcode[instruction_pointer + 1]] = insert
                log += f'Operation = {insert} into {intcode[instruction_pointer + 1]}\n'
                input_number += 1
            else:
                manual_input = int(input("Provide input: "))
                key = get_key(first_mode, intcode, instruction_pointer, 1, relative_base)
                intcode[key] = manual_input

                log += f'User input {manual_input} into {key}\n'

            instruction_pointer += 2
        elif opcode == 4:
            num_one = get_value(first_mode, intcode, instruction_pointer, 1, relative_base)

            if automatic_mode:
                instruction_pointer += 2
                log += f'Output = {num_one}\n'
                return num_one, instruction_pointer, relative_base, False
            else:
                print(num_one)
            instruction_pointer += 2
        elif opcode == 5 or opcode == 6:
            num_one = get_value(first_mode, intcode, instruction_pointer, 1, relative_base)
            num_two = get_value(second_mode, intcode, instruction_pointer, 2, relative_base)

            if (opcode == 5 and num_one != 0) or (opcode == 6 and num_one == 0):
                instruction_pointer = num_two
                log += f'New pointer = {num_two}\n'
            else:
                instruction_pointer += 3
        elif opcode == 7 or opcode == 8:
            num_one = get_value(first_mode, intcode, instruction_pointer, 1, relative_base)
            num_two = get_value(second_mode, intcode, instruction_pointer, 2, relative_base)

            key = get_key(third_mode, intcode, instruction_pointer, 3, relative_base)
            if (opcode == 7 and num_one < num_two) or (opcode == 8 and num_one == num_two):
                intcode[key] = 1
                log += f'Operation = 1 into {key}\n'
            else:
                intcode[key] = 0
                log += f'Operation = 0 into {key}\n'

            instruction_pointer += 4
        elif opcode == 9:
            num_one = get_value(first_mode, intcode, instruction_pointer, 1, relative_base)

            relative_base += num_one
            log += f'New relative base value {relative_base}\n'

            instruction_pointer += 2
        log += '\n\n'
        if logger:
            logger.add_log(log)

    return 0, instruction_pointer, relative_base, True


def define_mode(instruction: int):
    instruction = str(instruction).zfill(5)
    return int(instruction[3:]), int(instruction[2]), int(instruction[1]), int(instruction[0])
