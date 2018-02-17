from itertools import chain, combinations
from time import time

test_input_1 = [20, 15, 10, 5, 5]

with open('data.txt') as file:
    input_data = [int(x) for x in file.readlines()]


def solve(containers, volume):
    # find **all** combinations of the containers, eg. [0, 1, 2] -> [[], [0], [1], [2], [0,1], [0,2], [1,2], [0,1,2]]
    container_combinations = chain.from_iterable(combinations(containers, size) for size in range(len(containers) + 1))

    # find which of those container combinations can hold exactly the expected volume
    accepted_combinations = []
    for combination in container_combinations:
        if sum(combination) == volume:
            accepted_combinations.append(combination)

    # find the combination with least containers used
    minimum_container_count = min([len(x) for x in accepted_combinations])

    # find how many of accepted combinations use that many containers
    minimal_combination_counter = 0
    for combination in accepted_combinations:
        if len(combination) == minimum_container_count:
            minimal_combination_counter += 1

    return minimal_combination_counter


def main():
    test_1 = solve(test_input_1, 25)
    print('test_1:', test_1)

    start = time()
    answer = solve(input_data, 150)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
