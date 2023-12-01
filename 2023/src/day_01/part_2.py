import re

test_list = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]

line_list = []

with open("data.txt") as file:
    for line in file.readlines():
        line_list.append(line)

number_substitutions = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

number_regex = re.compile('(?=([1-9]|one|two|three|four|five|six|seven|eight|nine|zero))')


def calibrate_line(line):
    number_list = []

    all_numbers = re.findall(number_regex, line)
    for num in all_numbers:
        if str(num).isnumeric():
            number_list.append(int(num))
        else:
            number_list.append(number_substitutions[num])

    return int(f'{number_list[0]}{number_list[-1]}')


def calibrate(lines):
    number_sum = 0
    for line in lines:
        number_sum += calibrate_line(line)
    return number_sum


def main():
    test = calibrate(test_list)
    print("test:", test)

    answer = calibrate(line_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
