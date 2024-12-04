from copy import deepcopy
from time import time

test_input_1 = [
    'MMMSXXMASM',
    'MSAMXMSMSA',
    'AMXSXMAAMM',
    'MSAMASMSMX',
    'XMASAMXAMM',
    'XXAMMXXAMA',
    'SMSMSASXSS',
    'SAXAMASAAA',
    'MAMMMXMMMM',
    'MXMXAXMASX',
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
    for y in range(len(extended)):
        redrawn.append([])
        for x in range(len(extended[0])):
            redrawn[y].append(pad)

    count = 0
    for y, line in enumerate(extended[extent:-extent], start=extent):
        for x, character in enumerate(line[extent:-extent], start=extent):
            if character == 'X':
                if extended[y - 1][x] == 'M' and extended[y - 2][x] == 'A' and extended[y - 3][x] == 'S':
                    redrawn[y][x] = 'X'
                    redrawn[y - 1][x] = 'M'
                    redrawn[y - 2][x] = 'A'
                    redrawn[y - 3][x] = 'S'
                    count += 1
                if extended[y - 1][x - 1] == 'M' and extended[y - 2][x - 2] == 'A' and extended[y - 3][x - 3] == 'S':
                    redrawn[y][x] = 'X'
                    redrawn[y - 1][x - 1] = 'M'
                    redrawn[y - 2][x - 2] = 'A'
                    redrawn[y - 3][x - 3] = 'S'
                    count += 1
                if extended[y][x - 1] == 'M' and extended[y][x - 2] == 'A' and extended[y][x - 3] == 'S':
                    redrawn[y][x] = 'X'
                    redrawn[y][x - 1] = 'M'
                    redrawn[y][x - 2] = 'A'
                    redrawn[y][x - 3] = 'S'
                    count += 1
                if extended[y - 1][x + 1] == 'M' and extended[y - 2][x + 2] == 'A' and extended[y - 3][x + 3] == 'S':
                    redrawn[y][x] = 'X'
                    redrawn[y - 1][x + 1] = 'M'
                    redrawn[y - 2][x + 2] = 'A'
                    redrawn[y - 3][x + 3] = 'S'
                    count += 1
                if extended[y + 1][x] == 'M' and extended[y + 2][x] == 'A' and extended[y + 3][x] == 'S':
                    redrawn[y][x] = 'X'
                    redrawn[y + 1][x] = 'M'
                    redrawn[y + 2][x] = 'A'
                    redrawn[y + 3][x] = 'S'
                    count += 1
                if extended[y + 1][x + 1] == 'M' and extended[y + 2][x + 2] == 'A' and extended[y + 3][x + 3] == 'S':
                    redrawn[y][x] = 'X'
                    redrawn[y + 1][x + 1] = 'M'
                    redrawn[y + 2][x + 2] = 'A'
                    redrawn[y + 3][x + 3] = 'S'
                    count += 1
                if extended[y][x + 1] == 'M' and extended[y][x + 2] == 'A' and extended[y][x + 3] == 'S':
                    redrawn[y][x] = 'X'
                    redrawn[y][x + 1] = 'M'
                    redrawn[y][x + 2] = 'A'
                    redrawn[y][x + 3] = 'S'
                    count += 1
                if extended[y + 1][x - 1] == 'M' and extended[y + 2][x - 2] == 'A' and extended[y + 3][x - 3] == 'S':
                    redrawn[y][x] = 'X'
                    redrawn[y + 1][x - 1] = 'M'
                    redrawn[y + 2][x - 2] = 'A'
                    redrawn[y + 3][x - 3] = 'S'
                    count += 1

    pprint(redrawn)
    return count


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    start = time()
    answer = solve(input_data)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
