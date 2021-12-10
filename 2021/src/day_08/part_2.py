import re

digit_regex = re.compile(r'([a-g]+)')

test_digits = [
    [['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb'], ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']],
    [['edbfga', 'begcd', 'cbg', 'gc', 'gcadebf', 'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec'], ['fcgedb', 'cgb', 'dgebacf', 'gc']],
    [['fgaebd', 'cg', 'bdaec', 'gdafb', 'agbcfd', 'gdcbef', 'bgcad', 'gfac', 'gcb', 'cdgabef'], ['cg', 'cg', 'fdcagb', 'cbg']],
    [['fbegcd', 'cbd', 'adcefb', 'dageb', 'afcb', 'bc', 'aefdc', 'ecdab', 'fgdeca', 'fcdbega'], ['efabcd', 'cedba', 'gadfec', 'cb']],
    [['aecbfdg', 'fbg', 'gf', 'bafeg', 'dbefa', 'fcge', 'gcbea', 'fcaegb', 'dgceab', 'fcbdga'], ['gecf', 'egdcabf', 'bgf', 'bfgea']],
    [['fgeab', 'ca', 'afcebg', 'bdacfeg', 'cfaedg', 'gcfdb', 'baec', 'bfadeg', 'bafgc', 'acf'], ['gebdcfa', 'ecba', 'ca', 'fadegcb']],
    [['dbcfg', 'fgd', 'bdegcaf', 'fgec', 'aegbdf', 'ecdfab', 'fbedc', 'dacgb', 'gdcebf', 'gf'], ['cefg', 'dcbef', 'fcge', 'gbcadfe']],
    [['bdfegc', 'cbegaf', 'gecbf', 'dfcage', 'bdacg', 'ed', 'bedf', 'ced', 'adcbefg', 'gebcd'], ['ed', 'bcgafe', 'cdgba', 'cbgef']],
    [['egadfb', 'cdbfeg', 'cegd', 'fecab', 'cgb', 'gbdefca', 'cg', 'fgcdab', 'egfdb', 'bfceg'], ['gbdfcae', 'bgc', 'cg', 'cgb']],
    [['gcafb', 'gcf', 'dcaebfg', 'ecagb', 'gf', 'abcdeg', 'gaef', 'cafbge', 'fdbac', 'fegbdc'], ['fgae', 'cfgab', 'fg', 'bagce']],
]

digits = []

with open("data.txt") as file:
    for line in file.readlines():
        input_digits = re.findall(digit_regex, line.split('|')[0])
        output_digits = re.findall(digit_regex, line.split('|')[1])
        digits.append([input_digits, output_digits])


def calculate_sum_of_output(_digits):
    # segment analysis
    #   0:      1:      2:      3:      4:       5:      6:      7:      8:      9:
    #  aaaa    ....    aaaa    aaaa    ....     aaaa    aaaa    aaaa    aaaa    aaaa
    # b    c  .    c  .    c  .    c  b    c   b    .  b    .  .    c  b    c  b    c
    # b    c  .    c  .    c  .    c  b    c   b    .  b    .  .    c  b    c  b    c
    #  ....    ....    dddd    dddd    dddd     dddd    dddd    ....    dddd    dddd
    # e    f  .    f  e    .  .    f  .    f   .    f  e    f  .    f  e    f  .    f
    # e    f  .    f  e    .  .    f  .    f   .    f  e    f  .    f  e    f  .    f
    #  gggg    ....    gggg    gggg    ....     gggg    gggg    ....    gggg    gggg
    #   6       2       5       5       4        5       6       3       7       6

    output = []

    for a, b in _digits:
        code = ''
        mapping = dict()
        for digit in a + b:
            if len(digit) == 2:
                mapping.update({'1': set(digit)})
            elif len(digit) == 3:
                mapping.update({'7': set(digit)})
            elif len(digit) == 4:
                mapping.update({'4': set(digit)})
            elif len(digit) == 7:
                mapping.update({'8': set(digit)})
        mapping.update({'4-1': mapping['4'] - mapping['1']})
        for digit in a + b:
            if len(digit) not in [2, 3, 4, 7]:
                if len(digit) == 6:
                    if mapping['1'].issubset(set(digit)):  # 0 or 9
                        if mapping['4-1'].issubset(set(digit)):
                            mapping.update({'9': set(digit)})
                        else:
                            mapping.update({'0': set(digit)})
                    else:
                        mapping.update({'6': set(digit)})
                elif len(digit) == 5:
                    if not mapping['1'].issubset(set(digit)):  # 2 or 5
                        if mapping['4-1'].issubset(set(digit)):
                            mapping.update({'5': set(digit)})
                        else:
                            mapping.update({'2': set(digit)})
                    else:
                        mapping.update({'3': set(digit)})
        for digit in b:
            for k, v in mapping.items():
                if set(digit) == v:
                    code += k
        output.append(int(code))

    return sum(output)


def main():
    test = calculate_sum_of_output(test_digits)
    print("test:", test)

    answer = calculate_sum_of_output(digits)
    print("answer:", answer)


if __name__ == "__main__":
    main()
