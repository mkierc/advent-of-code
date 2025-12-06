from copy import deepcopy
from itertools import pairwise
from time import time

test_ranges = [
    (3, 5),
    (10, 14),
    (16, 20),
    (12, 18),
]

test_ranges_2 = [(104123582918543, 104720320730834),
                 (104123582918543, 104968750841600),
                 (104440211495288, 104968750841600),
                 (104440211495288, 105256379383318),
                 (104720320730834, 104968750841600),
                 (105256379383318, 105846682600140)]

test_numbers = [
    1,
    5,
    8,
    11,
    17,
    32,
]

ranges = []
numbers = []

with open('data.txt') as file:
    input_data = file.read().split()
    for line in input_data:
        if '-' in line:
            x, y = line.split('-')
            ranges.append((int(x), int(y)))
        else:
            numbers.append(int(line))


def merge(ranges):
    ranges.sort()

    been_merged = True

    while been_merged:
        been_merged = False

        for a, b in pairwise(ranges):
            a1, a2 = a
            b1, b2 = b
            if a2 >= b1:
                index = ranges.index(a)
                ranges.remove(a)
                ranges.remove(b)
                ranges.insert(index, (a1, max(a2, b2)))
                been_merged = True
                # print(len(ranges), a1, a2, b1, b2, ranges)
                break
    return ranges


def count_ranges(ranges):
    count = 0
    merged = merge(ranges)

    for a, b in merged:
        count += b - a + 1
    return count


def main():
    test_1 = count_ranges(test_ranges)
    print('test_1:', test_1)

    test_2 = count_ranges(test_ranges_2)
    print('test_2:', test_2)

    start = time()
    answer = count_ranges(ranges)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
