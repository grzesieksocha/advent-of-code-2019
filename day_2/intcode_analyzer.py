def analyze(intcode: list) -> list:
    instruction_pointer = 0
    while instruction_pointer <= len(intcode):
        if intcode[instruction_pointer] == 99:
            break

        num_one = intcode[intcode[instruction_pointer + 1]]
        num_two = intcode[intcode[instruction_pointer + 2]]
        if intcode[instruction_pointer] == 1:
            intcode[intcode[instruction_pointer + 3]] = num_one + num_two
        elif intcode[instruction_pointer] == 2:
            intcode[intcode[instruction_pointer + 3]] = num_one * num_two

        instruction_pointer += 4

    return intcode
