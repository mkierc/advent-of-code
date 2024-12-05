import re
from functools import cmp_to_key
from itertools import combinations
from time import time

order_regex = r'(\d+)\|(\d+)'
update_regex = r'\d+'

test_ordering = [
    (47, 53),
    (97, 13),
    (97, 61),
    (97, 47),
    (75, 29),
    (61, 13),
    (75, 53),
    (29, 13),
    (97, 29),
    (53, 29),
    (61, 53),
    (97, 53),
    (61, 29),
    (47, 13),
    (75, 47),
    (97, 75),
    (47, 61),
    (75, 61),
    (47, 29),
    (75, 13),
    (53, 13),
]

test_updates = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47],
]

ordering = []
updates = []

with open('data.txt') as file:
    input_data = file.read().splitlines()
    for line in input_data:
        if '|' in line:
            a, b = re.findall(order_regex, line)[0]
            ordering.append((int(a), int(b)))
        elif ',' in line:
            numbers = [int(_) for _ in re.findall(update_regex, line)]
            updates.append(numbers)


def is_correct(number_list, ordering):
    for a, b in combinations(number_list, 2):
        if (a, b) not in ordering:
            return False
    return True


def comparator(ordering):
    def cmp(a, b):
        if (a, b) in ordering:
            return 1
        elif a == b:
            return 0
        else:
            return -1
    return cmp


def solve(ordering, updates):
    sum = 0
    for update in updates:
        if not is_correct(update, ordering):
            sorted_update = sorted(update, key=cmp_to_key(comparator(ordering)))
            sum += sorted_update[len(sorted_update)//2]
    return sum


def main():
    pass
    test_1 = solve(test_ordering, test_updates)
    print('test_1:', test_1)

    start = time()
    answer = solve(ordering, updates)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
