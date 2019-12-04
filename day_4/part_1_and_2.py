def is_six_digit(number: int):
    return 100000 < number <= 999999


def has_two_same_adjacent_digits(number: int):
    number = str(number)
    for pos, digit in enumerate(number):
        if pos + 1 == len(number):
            return False
        if int(digit) == int(number[pos + 1]):
            return True


def has_two_same_adjacent_digits_not_grouped(number: int):
    number = str(number)
    small_repeat = False
    repeated_number = number[0]
    repeat_count = 1
    for pos, digit in enumerate(number):
        if pos + 1 == len(number):
            return small_repeat or repeat_count == 2

        if int(digit) == int(number[pos + 1]):
            if number[pos + 1] == repeated_number:
                repeat_count += 1
        else:
            if repeat_count == 2:
                small_repeat = True
            repeated_number = number[pos + 1]
            repeat_count = 1


def digits_never_decrease(number: int):
    number = str(number)
    for pos, digit in enumerate(number):
        if pos + 1 == len(number):
            return True
        if int(digit) > int(number[pos + 1]):
            return False


def solve_part_1():
    count = 0
    for number in range(767253)[273025:]:
        if is_six_digit(number) and has_two_same_adjacent_digits(number) and digits_never_decrease(number):
            count += 1

    return count


def solve_part_2():
    count = 0
    for number in range(767253)[273025:]:
        if is_six_digit(number) and digits_never_decrease(number) and has_two_same_adjacent_digits_not_grouped(number):
            count += 1

    return count
