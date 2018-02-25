from collections import defaultdict
from time import time

initial_data = [
    [20151125, 18749137, 17289845, 30943339, 10071777, 33511524],
    [31916031, 21629792, 16929656, 7726640, 15514188, 4041754],
    [16080970, 8057251, 1601130, 7981243, 11661866, 16474243],
    [24592653, 32451966, 21345942, 9380097, 10600672, 31527494],
    [77061, 17552253, 28094349, 6899651, 9250759, 31663883],
    [33071741, 6796745, 25397450, 24659492, 1534922, 27995004]
]
test_data = (6, 6)
input_data = (2981, 3075)


# generate successive positions diagonally:
# 1: [1, 1],
# 2: [2, 1], [1, 2],
# 3: [3, 1], [2, 2], [1, 3]
# 4: [4, 1], [3, 2], [2, 3], [1, 4]
# 5: ...
def diagonal_generator():
    for diagonal in range(1, 10000):
        for y in range(1, diagonal + 1):
            x = diagonal + 1 - y
            yield (x, y)


def solve(numbers):
    number_board = defaultdict(int)

    position = diagonal_generator()
    current_position = next(position)

    number_board[current_position] = 20151125

    while current_position != numbers:
        next_code = (number_board[current_position] * 252533) % 33554393
        current_position = next(position)
        number_board[current_position] = next_code

    return number_board[current_position]


def main():
    test_1 = solve((6, 6))
    print('test_1:', test_1, "\nexpect:", 27995004)

    start = time()
    answer = solve(input_data)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
