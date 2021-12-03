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


def find_power_consumption(numbers_list):
    zeroes_counts = []
    ones_counts = []

    for i in range(len(numbers_list[0])):
        zeroes_counts.append(0)
        ones_counts.append(0)

    for number in numbers_list:
        for i, digit in enumerate(number):
            if digit == '0':
                zeroes_counts[i] += 1
            elif digit == '1':
                ones_counts[i] += 1
            else:
                raise AssertionError(f'Unexpected digit: {digit} in number: {number}')

    gamma_rate = ''
    epsilon_rate = ''

    for i in range(len(zeroes_counts)):
        if zeroes_counts[i] > ones_counts[i]:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    g, e = int(gamma_rate, 2), int(epsilon_rate, 2)

    return g, e, g*e


def main():
    test = find_power_consumption(test_list)
    print("test:", test)

    answer = find_power_consumption(numbers_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
