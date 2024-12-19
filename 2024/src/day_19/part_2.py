import heapq
from collections import defaultdict
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


def count_combinations(towel_list, pattern_to_match):
    queue = []
    heapq.heappush(queue, '')

    partially_matching = defaultdict(list)

    while queue:
        current_substring = heapq.heappop(queue)

        if current_substring == pattern_to_match:
            continue

        for towel in towel_list:
            new_substring = current_substring + towel
            if new_substring == pattern_to_match[:len(new_substring)]:
                if current_substring not in partially_matching[new_substring]:
                    heapq.heappush(queue, new_substring)
                    partially_matching.update({new_substring: [*partially_matching[new_substring], current_substring]})

    retrace_queue = []
    heapq.heappush(retrace_queue, pattern_to_match)

    # leaf nodes have a child count of 1
    child_count = {'': 1}

    while retrace_queue:
        current = heapq.heappop(retrace_queue)
        children = partially_matching[current]

        # if we know the children count for all the children of current, sum them and set as count of current:
        if set(children).issubset(set(child_count.keys())):
            current_count = 0
            for child in children:
                current_count += child_count[child]
            child_count.update({current: current_count})
        # otherwise, we add back to retrace queue the uncounted ones, to find out their respective number of children
        else:
            for child in children:
                if child not in child_count.keys():
                    heapq.heappush(retrace_queue, child)
            heapq.heappush(retrace_queue, current)

    return child_count[pattern_to_match]


def solve(towel_list, pattern_list):
    towel_list = sorted(towel_list, key=len, reverse=True)
    possible_count = 0

    for pattern in pattern_list:
        possible_count += count_combinations(towel_list, pattern)

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

# 15708393309 too low (had the first-case filter [0:1] on pattern list...)

# answer:               621820080273474
# bfs + bfs retrace     3.2173655033111572 s
