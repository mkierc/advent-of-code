import statistics
from math import floor, ceil
from time import time, sleep

test_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
positions = []

with open("data.txt") as file:
    for number in file.read().split(','):
        positions.append(int(number))


def brute_align_crabs(_positions):
    a = min(_positions)
    b = max(_positions)

    n = 0
    min_cost = 9999999999999999
    for i in range(a, b):
        cost = 0
        for crab in _positions:
            distance = abs(crab - i)
            cost += (distance+1) * (distance/2)
        if cost < min_cost:
            min_cost = cost
            n = i

    return n, int(min_cost)


def analytical_align_crabs(_positions):
    a = min(_positions)
    b = max(_positions)

    while not a == b:
        a_cost = 0
        b_cost = 0
        for crab in _positions:
            distance = abs(crab - a)
            a_cost += (distance+1) * (distance/2)
            distance = abs(crab - b)
            b_cost += (distance+1) * (distance/2)
        # print(a, a_cost, b, b_cost)
        if a_cost < b_cost:
            b = floor((a+b)/2)
        else:
            a = ceil((a+b)/2)

    return b, int(b_cost)


def main():
    start = time()
    test = brute_align_crabs(test_positions)
    print("test:", test)
    print(f'time: {time() - start:.20f}')

    start = time()
    test = analytical_align_crabs(test_positions)
    print("test:", test)
    print(f'time: {time() - start:.20f}')

    start = time()
    answer = brute_align_crabs(positions)
    print("answer:", answer)
    print(f'time: {time() - start:.20f}')

    start = time()
    answer = analytical_align_crabs(positions)
    print("answer:", answer)
    print(f'time: {time() - start:.20f}')


if __name__ == "__main__":
    main()
