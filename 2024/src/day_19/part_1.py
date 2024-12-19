import heapq
import re
from time import time

test_towels = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']

test_patterns = [
    'brwrr',
    'bggr',
    'gbbr',
    'rrbgbr',
    'ubwu',
    'bwurrg',
    'brgr',
    'bbrgwb',
]

towels = []
patterns = []

with open('data.txt') as file:
    t, p = file.read().split('\n\n')

    for towel in t.split(', '):
        towels.append(towel)
    for pattern in p.splitlines():
        patterns.append(pattern)


def is_possible(towel_list, pattern):
    queue = []
    heapq.heappush(queue, '')

    partially_matching = set()

    while queue:
        print(queue)
        current = heapq.heappop(queue)

        if current == pattern:
            return True

        for towel in towel_list:
            substring = current + towel
            if substring == pattern[:len(substring)] and substring not in partially_matching:
                heapq.heappush(queue, substring)
                partially_matching.add(substring)

    return False


def solve(towel_list, pattern_list):
    possible_count = 0

    towel_list = sorted(towel_list, key=len, reverse=True)

    for pattern in pattern_list:
        if is_possible(towel_list, pattern):
            possible_count += 1

    return possible_count


def main():
    test_1 = solve(test_towels, test_patterns)
    print('test_1:', test_1)

    start = time()
    answer = solve(towels, patterns)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()

# answer:       255
# simple bfs:   1.0990588665008545
