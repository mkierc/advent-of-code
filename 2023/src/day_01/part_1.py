test_list = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
]

line_list = []

with open("data.txt") as file:
    for line in file.readlines():
        line_list.append(line)


def calibrate_line(line):
    number_list = []
    for i in line:
        if i.isnumeric():
            number_list.append(i)

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
