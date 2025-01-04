import heapq
import re
from time import time
from typing import Tuple, List

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


def memoized(function, dictionary={}):
    def inner(v1, v2):
        if (v1, v2) not in dictionary:
            dictionary[(v1, v2)] = function(v1, v2)
        return dictionary[(v1, v2)]

    return inner


def count_possible_queue(spring: str, checksum: List[int]):
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


@memoized
def count_possible(spring: str, checksum: Tuple[int]):
    count = 0

    # if we exhausted all checksums, check if all springs are accounted for
    if not checksum:
        if "#" not in spring:
            return 1
        return 0

    # if we've exhausted springs, check if all checksums are accounted for
    if not spring:
        if not checksum:
            return 1
        return 0

    current_char = spring[0]
    rest = spring[1:]
    checksum_value = checksum[0]

    # if current spring record is damaged ('?'), add two possibilities into the queue
    if current_char == '?':
        count += count_possible('.' + rest, checksum)
        count += count_possible('#' + rest, checksum)

    # if current spring is operational ('.'), put the rest of springs into the queue
    elif current_char == '.':
        count += count_possible(rest, checksum)

    # if current spring is damaged ('#')
    elif current_char == '#':

        # skip, if there's fewer springs left to check than in checksum
        if len(spring) < checksum_value:
            return 0

        # skip, if there's an operational spring within next block of continuous damaged springs
        if "." in spring[:checksum_value]:
            return 0

        # skip, if there's a damaged spring outside the range of current checksum
        if len(spring) > checksum_value and spring[checksum_value] == "#":
            return 0

        # put the rest of the spring minus length of current spring, and rest of checksums to the queue
        count += count_possible(spring[checksum_value + 1:], checksum[1:])

    return count


def solve(spring_list):
    count = 0
    for i, spring in enumerate(spring_list):
        record = '?'.join([spring[0] for _ in range(5)])
        checksum = [int(_) for _ in spring[1:]] * 5

        # print(i, '/', len(spring_list), record, end=' ')
        # current = count_possible_queue(record, checksum)
        current = count_possible(record, tuple(checksum))
        # print(current)
        count += current
    return count


def main():
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

# test:                     525152
# dfs with queue:           2.928140878677368 s
# memoized-recursive dfs:   0.001994848251342 s

# answer:                   65607131946466
# dfs with queue:           NOPE
# memoized-recursive dfs:   0.735033273696899 s
