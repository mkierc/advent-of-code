import re

digit_regex = re.compile(r'([a-g]+)')

test_digits = [
    'fdgacbe', 'cefdb', 'cefbgd', 'gcbe',
    'fcgedb', 'cgb', 'dgebacf', 'gc',
    'cg', 'cg', 'fdcagb', 'cbg',
    'efabcd', 'cedba', 'gadfec', 'cb',
    'gecf', 'egdcabf', 'bgf', 'bfgea',
    'gebdcfa', 'ecba', 'ca', 'fadegcb',
    'cefg', 'dcbef', 'fcge', 'gbcadfe',
    'ed', 'bcgafe', 'cdgba', 'cbgef',
    'gbdfcae', 'bgc', 'cg', 'cgb',
    'fgae', 'cfgab', 'fg', 'bagce',
]

digits = []

with open("data.txt") as file:
    for line in file.readlines():
        digits.extend(re.findall(digit_regex, line.split('|')[1]))


def count_digits(_digits):
    count = 0
    for digit in _digits:
        if len(digit) in [2, 3, 4, 7]:
            count += 1

    return count


def main():
    test = count_digits(test_digits)
    print("test:", test)

    answer = count_digits(digits)
    print("answer:", answer)


if __name__ == "__main__":
    main()
