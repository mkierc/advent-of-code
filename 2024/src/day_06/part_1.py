from copy import deepcopy
from time import time

test_input_1 = [
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
]

input = []

with open('data.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        input.append([*line])


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(char, end='')
        print('')


def extend_grid(grid: list, extent: int, character: str):
    new_grid = deepcopy(grid)
    width = len(grid[0])

    for i, line in enumerate(new_grid):
        padding = [*(character * extent)]
        line = padding + line + padding
        new_grid[i] = [*line]

    for i in range(extent):
        new_grid.insert(0, [*(character * int(width + 2 * extent))])
    for i in range(extent):
        new_grid.append([*(character * int(width + 2 * extent))])

    return new_grid


def solve(grid):
    grid = extend_grid(grid, 1, ' ')
    x = 0
    y = 0
    d_x = 0
    d_y = -1

    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == '^':
                y = i
                x = j

    while grid[y][x] != ' ':
        # if next step is inside, continue going in that direction
        if grid[y+d_y][x+d_x] in ['.', '^']:
            x += d_x
            y += d_y
            grid[y][x] = '^'
        # if next step is outside, continue going in that direction, but don't count?
        elif grid[y+d_y][x+d_x] == ' ':
            x += d_x
            y += d_y
        # if we'll hit a wall, turn right
        elif grid[y+d_y][x+d_x] == '#':
            if d_x == 0 and d_y == -1:
                d_x, d_y = 1, 0
            elif d_x == 1 and d_y == 0:
                d_x, d_y = 0, 1
            elif d_x == 0 and d_y == 1:
                d_x, d_y = -1, 0
            elif d_x == -1 and d_y == 0:
                d_x, d_y = 0, -1

    pprint(grid)

    counter = 0
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == '^':
                counter += 1

    return counter


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    start = time()
    answer = solve(input)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
