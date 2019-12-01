import fuel_calculator


def main():
    fuel_needed = 0
    with open('./input.txt', 'r') as f:
        for line in f:
            fuel_needed += fuel_calculator.count_fuel_needed(int(line), 0, True)

    print(fuel_needed)


main()
