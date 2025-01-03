import itertools
from collections import defaultdict
from copy import deepcopy
from time import time

test_input_1 = [[*_] for _ in [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....',
]]

input_data = []

with open('data.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        input_data.append([*line])


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(char, end='')
        print('')


def expand_universe(stars_list):
    max_x = 0
    max_y = 0

    for x, y in stars_list:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    x_to_expand = [True for _ in range(max_x + 1)]
    y_to_expand = [True for _ in range(max_x + 1)]

    for x, y in stars_list:
        x_to_expand[x] = False
        y_to_expand[y] = False

    cur = 0
    for i, v in enumerate(x_to_expand):
        if v:
            cur += 1
        x_to_expand[i] = cur
    cur = 0
    for i, v in enumerate(y_to_expand):
        if v:
            cur += 1
        y_to_expand[i] = cur

    # print(x_to_expand)
    # print(y_to_expand)

    expanded = []
    for x, y in stars_list:
        expanded.append((x + x_to_expand[x], y + y_to_expand[y]))

    return expanded


def solve(grid):
    stars = []

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '#':
                stars.append((x, y))

    # print(stars)
    # pprint(grid)

    expanded = expand_universe(stars)

    distance_sum = 0
    for (x1, y1), (x2, y2) in itertools.combinations_with_replacement(expanded, 2):
        distance_sum += abs(x2 - x1) + abs(y2 - y1)

    return distance_sum


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    start = time()
    answer = solve(input_data)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# answer:   9734203
# time:     0.010972261428833008
