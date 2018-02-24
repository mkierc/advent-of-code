from functools import reduce
from itertools import combinations, chain
from operator import mul
from time import time

test_input = {
    1, 2, 3, 4, 5, 7, 8, 9, 10, 11
}

input_data = {
    1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113
}


def solve(package_list: set, package_split: int):
    group_weight = sum(package_list) // package_split

    # find the size of smallest group that can sum up to the expected group weight
    smallest_group_possible = 0
    temporary_weight = 0
    for package in sorted(package_list, reverse=True):
        if temporary_weight < group_weight:
            temporary_weight += package
            smallest_group_possible += 1

    possible_divides = []
    for group_size in range(smallest_group_possible, len(package_list)):
        for combination in (x for x in combinations(package_list, group_size) if sum(x) == group_weight):
            quantum_entaglement = reduce(mul, combination, 1)
            possible_divides.append((group_size, quantum_entaglement))

        # if we found a combination within current group size, don't continue searching in bigger groups
        if possible_divides:
            break

    return sorted(possible_divides)[0][1]


def main():
    test_1 = solve(test_input, 3)
    print('test_1:', test_1)
    test_2 = solve(test_input, 4)
    print('test_2:', test_2)

    start = time()
    part_1 = solve(input_data, 3)
    print('part_1:', part_1)
    print('time:', time() - start)
    start = time()
    part_2 = solve(input_data, 4)
    print('part_2:', part_2)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
