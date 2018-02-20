from collections import defaultdict
from time import time

import math

test_input_1 = 140
input_data = 29_000_000


def solve(present_count):
    houses = defaultdict(lambda: 0)

    limit = present_count // int(math.log(present_count))

    for elf in range(1, limit):
        for house in range(elf, limit, elf):
            houses[house] = houses[house] + elf * 10

        if houses[elf] >= present_count:
            return elf


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    start = time()
    answer = solve(input_data)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
