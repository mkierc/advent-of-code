from time import time

test_ranges = [
    (3, 5),
    (10, 14),
    (16, 20),
    (12, 18),
]

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


def solve(ranges, numbers):
    count = 0
    for number in numbers:
        for a, b in ranges:
            if a <= number <= b:
                count += 1
                break

    return count


def main():
    test_1 = solve(test_ranges, test_numbers)
    print('test_1:', test_1)

    start = time()
    answer = solve(ranges, numbers)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
