from copy import deepcopy
from time import time

test_input_1 = [
    '..@@.@@@@.',
    '@@@.@.@.@@',
    '@@@@@.@.@@',
    '@.@@@@..@.',
    '@@.@@@@.@@',
    '.@@@@@@@.@',
    '.@.@.@.@@@',
    '@.@@@.@@@@',
    '.@@@@@@@@.',
    '@.@.@@@.@.',
]

with open('data.txt') as file:
    input_data = file.read().splitlines()


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(char, end='')
        print('')


def extend_grid(grid: list, extent: int, character: str):
    new_grid = deepcopy(grid)
    width = len(grid[0])

    for i, line in enumerate(new_grid):
        padding = character * extent
        line = padding + line + padding
        new_grid[i] = line

    for i in range(extent):
        new_grid.insert(0, character * int(width + 2 * extent))
    for i in range(extent):
        new_grid.append(character * int(width + 2 * extent))

    return new_grid


def solve(grid):
    extent = 1
    pad = '.'
    extended = extend_grid(grid, extent, pad)
    redrawn = []
    removed = []
    for y in range(len(extended)):
        redrawn.append([])
        removed.append([])
        for x in range(len(extended[0])):
            redrawn[y].append(pad)
            removed[y].append(pad)

    total_count = 0

    while True:
        current_count = 0
        for y, line in enumerate(extended[extent:-extent], start=extent):
            for x, character in enumerate(line[extent:-extent], start=extent):
                if character == '@':
                    redrawn[y][x] = '@'
                    removed[y][x] = '@'

                    adjacents = [
                        extended[y - 1][x - 1],
                        extended[y - 1][x],
                        extended[y - 1][x + 1],
                        extended[y][x - 1],
                        extended[y][x + 1],
                        extended[y + 1][x - 1],
                        extended[y + 1][x],
                        extended[y + 1][x + 1]
                    ]

                    if adjacents.count('@') < 4:
                        redrawn[y][x] = 'X'
                        removed[y][x] = '.'
                        current_count += 1
        total_count += current_count

        # pprint(redrawn)
        extended = deepcopy(removed)
        if current_count == 0:
            break

    return total_count


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    start = time()
    answer = solve(input_data)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
