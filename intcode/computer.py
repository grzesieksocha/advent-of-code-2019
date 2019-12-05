

def analyze(intcode: list) -> list:
    instruction_pointer = 0
    while instruction_pointer <= len(intcode):
        opcode, first_mode, second_mode, third_mode = define_mode(intcode[instruction_pointer])

        if opcode == 99:
            break

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
            instruction_pointer += 4
        elif opcode == 3:
            intcode[intcode[instruction_pointer + 1]] = int(input("Provide input: "))
            instruction_pointer += 2
        elif opcode == 4:
            if first_mode == 0:
                num_one = intcode[intcode[instruction_pointer + 1]]
            else:
                num_one = intcode[instruction_pointer + 1]

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
            else:
                intcode[intcode[instruction_pointer + 3]] = 0

            instruction_pointer += 4

        # print(instruction_pointer)
    return intcode


def define_mode(instruction: int):
    instruction = str(instruction).zfill(5)
    return int(instruction[3:]), int(instruction[2]), int(instruction[1]), int(instruction[0])