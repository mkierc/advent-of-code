import heapq
import itertools
import re
from copy import copy
from time import time
from typing import List

levels_regex = r'(\d+)'

test_data = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''

test_springs = []

for line in test_data.splitlines():
    r, nums = line.split(' ')
    nums = re.findall(levels_regex, nums)
    test_springs.append([r, *nums])

springs = []

with (open("data.txt") as file):
    for line in file.readlines():
        r, nums = line.split(' ')
        nums = re.findall(levels_regex, nums)
        springs.append([r, *nums])


def build_regex(checksum):
    regex = r'\.*'
    for n in checksum:
        regex += fr'#{{{n}}}\.+'
    regex = regex[:-1] + '*'
    return regex


def count_combinations(record: str, checksum: List[int]):
    regex = build_regex(checksum)
    # print(regex)

    indexes = [i for i, char in enumerate(record) if char == '?']
    # print(indexes)

    count = 0
    for combo in itertools.combinations_with_replacement(['#', '.'], len(indexes)):
        for permu in set(itertools.permutations(combo)):
            current_record = record
            for i, n in enumerate(indexes):
                current_record = current_record[:n] + permu[i] + current_record[n + 1:]
            # print(current_record)
            match = re.fullmatch(regex, current_record)
            # print(regex, current_record, match)
            if match:
                count += 1

    print(record, count)

    return count


def a_over_b(dots, spaces):
    # list of dot "change" values available  5 -> [1, 1, 1, 1, 1, 2, 2, 3, 4, 5]
    dot_list = []
    for i in range(1, dots + 1):
        dot_list.extend([i for _ in range(dots // i)])

    combos = set()
    for length in range(0, len(dot_list) + 1):
        for combo in itertools.combinations(dot_list, length):
            # either fill all slots, leave either first/last empty, or both empty
            if len(combo) in [spaces, spaces - 1, spaces - 2]:
                if sum(combo) == dots:
                    combos.add(combo)

    # print(combos)

    perms = set()
    for combo in combos:
        for perm in itertools.permutations(combo):
            if len(perm) == spaces:
                perms.add(perm)
            elif len(perm) == spaces - 1:
                perms.add((0, *perm))
                perms.add((*perm, 0))
            else:
                perms.add((0, *perm, 0))

    return perms


def match(spring, template):
    if len(spring) != len(template):
        raise NotImplementedError(f'lengths should match: {len(spring)} != {len(template)}')

    for i in range(len(spring)):
        if spring[i] == '#' and template[i] == '#':
            continue
        if spring[i] == '.' and template[i] == '.':
            continue
        if spring[i] == '?' and template[i] in ['#', '.']:
            continue
        return False
    return True


def generate_combinations(spring: str, checksum: List[int]):
    """
    this approach is waaay too slow to be feasible, especially on case 180:
    ??#?.???.#??..???? 1,1

    we have 18 slots for [1, 1] that keep cycling over 2**18 times, even though there's obviously only 1 solution...
    """
    hashes = ['#' * x for x in checksum]

    free_dots = len(spring) - sum(checksum)

    # print(base)
    # print(hashes)
    # print(free_dots)

    # how many ways to distribute {free_dots} of chars into {len(hashes) + 1} slots?
    # 7 free_dots, 5 slots
    # 7, 0, 0, 0, 0
    # 6, 1, 0, 0, 0

    count = 0
    for dot_combo in a_over_b(free_dots, len(hashes) + 1):
        template = ''
        for i, hash in enumerate(hashes):
            template += '.' * dot_combo[i]
            template += hashes[i]
        template += '.' * dot_combo[-1]

        # print(spring, template, free_dots, len(hashes) + 1, end=' ')
        # print(match(spring, template))
        if match(spring, template):
            count += 1

    return count


def count_possible(spring: str, checksum: List[int]):
    start = spring, checksum
    queue = []
    heapq.heappush(queue, start)

    count = 0

    while queue:
        current_spring, current_checksum = heapq.heappop(queue)

        # if we exhausted all checksums, check if all springs are accounted for
        if not current_checksum:
            if "#" not in current_spring:
                count += 1
            continue

        # if we've exhausted springs, check if all checksums are accounted for
        if not current_spring:
            if not current_checksum:
                count += 1
            continue

        current_char = current_spring[0]
        rest = current_spring[1:]

        # if current spring record is damaged ('?'), add two possibilities into the queue
        if current_char == '?':
            heapq.heappush(queue, ('.' + rest, current_checksum))
            heapq.heappush(queue, ('#' + rest, current_checksum))
            continue

        # if current spring is operational ('.'), put the rest of springs into the queue
        if current_char == '.':
            heapq.heappush(queue, (rest, current_checksum))

        checksum_value = current_checksum[0]

        # if current spring is damaged ('#')
        if current_char == '#':

            # skip, if there's fewer springs left to check than in checksum
            if len(current_spring) < checksum_value:
                continue

            # skip, if there's an operational spring within next block of continuous damaged springs
            if "." in current_spring[:checksum_value]:
                continue

            # skip, if there's a damaged spring outside the range of current checksum
            if len(current_spring) > checksum_value and current_spring[checksum_value] == "#":
                continue

            # put the rest of the spring minus length of current spring, and rest of checksums to the queue
            heapq.heappush(queue, (current_spring[checksum_value + 1:], current_checksum[1:]))

    return count


def solve(spring_list):
    count = 0
    for i, spring in enumerate(spring_list):
        record, checksum = spring[0], [int(_) for _ in spring[1:]]

        # print(i, '/', len(spring_list), record, end=' ')
        # current = generate_combinations(record, checksum)
        current = count_possible(record, checksum)
        # print(current)
        count += current
    return count


def main():
    # print(generate_combinations(13, [2, 2, 6]))
    # print(generate_combinations(14, [1, 1, 3]))
    # print(generate_combinations('#?????????#????', [1, 3, 2, 2]))

    # print(count_combinations(test_springs[-1][0], test_springs[-1][1:]))

    start = time()
    test_1 = solve(test_springs)
    print('test_1:', test_1)
    print('time:', time() - start)

    start = time()
    answer = solve(springs)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# test:                         21
# brute-force combinations:     1.170896053314209 s
# dfs with queue:               0.000997543334960 s

# answer:                       7490
# brute-force combinations:     NOPE
# dfs with queue:               0.067815065383911 s
