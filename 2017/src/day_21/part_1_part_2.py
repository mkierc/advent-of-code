from collections import defaultdict

test_input_1 = [
    '../.# => ##./#../...',
    '.#./..#/### => #..#/..../..../#..#'
]

with open('data.txt') as file:
    input_data = file.read().splitlines()


def extend(basic_rules):
    def rotate_2(rule):
        return rule[1] + rule[4] + '/' + \
               rule[0] + rule[3]

    def rotate_3(rule):
        return rule[2] + rule[6] + rule[10] + '/' + \
               rule[1] + rule[5] + rule[9] + '/' + \
               rule[0] + rule[4] + rule[8]

    def flip_3(rule):
        return rule[2] + rule[1] + rule[0] + '/' + \
               rule[6] + rule[5] + rule[4] + '/' + \
               rule[10] + rule[9] + rule[8]

    extended_rules = defaultdict()

    for basic_rule in basic_rules:
        before, after = basic_rule.split(' => ')
        # 2x2 -> 3x3
        if len(before) == 5:
            # just rotate 4 times
            for _ in range(4):
                extended_rules[before] = after
                before = rotate_2(before)
        # 3x3 -> 4x4
        else:
            # rotate the rules 3 times
            for _ in range(3):
                extended_rules[before] = after
                before = rotate_3(before)
            # mirror once
            extended_rules[before] = after
            before = flip_3(before)
            # rotate the mirrored version 3 times
            for _ in range(3):
                extended_rules[before] = after
                before = rotate_3(before)

    return extended_rules


def enhance_2(grid, rules):
    enhanced = []
    size = len(grid) // 2

    for i in range(size):
        line1 = ''
        line2 = ''
        line3 = ''
        for j in range(size):
            before = grid[i * 2][j * 2:(j + 1) * 2] + '/' + \
                     grid[i * 2 + 1][j * 2:(j + 1) * 2]
            after = rules[before].split('/')
            line1 += after[0]
            line2 += after[1]
            line3 += after[2]
        enhanced.append(line1)
        enhanced.append(line2)
        enhanced.append(line3)
    return enhanced


def enhance_3(grid, rules):
    enhanced = []
    size = len(grid) // 3

    for i in range(size):
        line1, line2, line3, line4 = '', '', '', ''
        for j in range(size):
            before = grid[i * 3][j * 3:(j + 1) * 3] + '/' + \
                     grid[i * 3 + 1][j * 3:(j + 1) * 3] + '/' + \
                     grid[i * 3 + 2][j * 3:(j + 1) * 3]
            after = rules[before].split('/')
            line1 += after[0]
            line2 += after[1]
            line3 += after[2]
            line4 += after[3]
        enhanced.append(line1)
        enhanced.append(line2)
        enhanced.append(line3)
        enhanced.append(line4)
    return enhanced


def generate(rules, steps):
    seed = [
        '.#.',
        '..#',
        '###'
    ]

    # extend the rules to take care of rotated/mirrored patterns
    extended_rules = extend(rules)

    # do n rounds of enhancing
    for _ in range(steps):
        if (len(seed) % 2) == 0:
            seed = enhance_2(seed, extended_rules)
        else:
            seed = enhance_3(seed, extended_rules)

    # count the pixels
    pixel_count = 0
    for rule in seed:
        for char in rule:
            if char == '#':
                pixel_count += 1

    return pixel_count


def main():
    test_1 = generate(test_input_1, 2)
    print('test_1:', test_1)

    answer = generate(input_data, 5)
    print('part_1:', answer)

    answer = generate(input_data, 18)
    print('part_2:', answer)


if __name__ == '__main__':
    main()
