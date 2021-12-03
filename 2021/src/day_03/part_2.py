import copy

test_list = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

numbers_list = []

with open("data.txt") as file:
    for line in file.read().splitlines():
        numbers_list.append(line)


def find_life_support_rating(numbers_list):
    oxygen_list = copy.deepcopy(numbers_list)
    co2_list = copy.deepcopy(numbers_list)

    iteration = 0
    while not len(oxygen_list) == 1:

        zeroes_count = 0
        ones_count = 0

        for number in oxygen_list:
            if number[iteration] == '0':
                zeroes_count += 1
            elif number[iteration] == '1':
                ones_count += 1
            else:
                raise AssertionError(f'Unexpected digit: {number[iteration]} in number: {number}')

        new_oxygen_list = []

        if zeroes_count > ones_count:
            for number in oxygen_list:
                if number[iteration] == '0':
                    new_oxygen_list.append(number)
        else:
            for number in oxygen_list:
                if number[iteration] == '1':
                    new_oxygen_list.append(number)

        oxygen_list = new_oxygen_list
        iteration = iteration + 1

    iteration = 0
    while not len(co2_list) == 1:

        zeroes_count = 0
        ones_count = 0

        for number in co2_list:
            if number[iteration] == '0':
                zeroes_count += 1
            elif number[iteration] == '1':
                ones_count += 1
            else:
                raise AssertionError(f'Unexpected digit: {number[iteration]} in number: {number}')

        new_co2_list = []

        if zeroes_count <= ones_count:
            for number in co2_list:
                if number[iteration] == '0':
                    new_co2_list.append(number)
        else:
            for number in co2_list:
                if number[iteration] == '1':
                    new_co2_list.append(number)

        co2_list = new_co2_list
        iteration = iteration + 1

    oxy, co2 = int(str(oxygen_list)[2:-2], 2), int(str(co2_list)[2:-2], 2)

    return oxygen_list, co2_list, oxy, co2, oxy*co2


def main():
    test = find_life_support_rating(test_list)
    print("test:", test)

    answer = find_life_support_rating(numbers_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
