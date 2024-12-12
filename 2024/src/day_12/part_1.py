import itertools
from collections import defaultdict
from copy import deepcopy

test_input_1 = [[*_] for _ in [
    'AAAA',
    'BBCD',
    'BBCC',
    'EEEC',

]]

test_input_2 = [[*_] for _ in [
    'RRRRIICCFF',
    'RRRRIICCCF',
    'VVRRRCCFFF',
    'VVRCCCJFFF',
    'VVVVCJJCFE',
    'VVIVCCJJEE',
    'VVIIICJJEE',
    'MIIIIIJJEE',
    'MIIISIJEEE',
    'MMMISSJEEE',

]]

input_data = []

with open('data.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        input_data.append([*line])


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


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(char, end='')
        print('')


def flood_fill(x, y, grid, char):
    old_char = grid[y][x]
    grid[y][x] = char

    if grid[y][x - 1] == old_char:
        flood_fill(x - 1, y ,grid, char)
    if grid[y - 1][x] == old_char:
        flood_fill(x, y - 1, grid, char)
    if grid[y + 1][x] == old_char:
        flood_fill(x, y + 1, grid, char)
    if grid[y][x + 1] == old_char:
        flood_fill( x + 1, y,grid, char)


def define_new_regions(grid, extent):
    substituted = []
    current_substitute_number = 0

    for y, line in enumerate(grid[extent:-extent], start=extent):
        for x, character in enumerate(line[extent:-extent], start=extent):
            if grid[y][x] not in substituted:
                flood_fill(x, y, grid, current_substitute_number)
                substituted.append(current_substitute_number)
                current_substitute_number += 1


def solve(grid):
    extent = 1
    pad = '.'
    extended = extend_grid(grid, extent, pad)

    area = defaultdict(int)
    perimeter = defaultdict(int)

    define_new_regions(extended, 1)

    for y, line in enumerate(extended[extent:-extent], start=extent):
        for x, character in enumerate(line[extent:-extent], start=extent):
            area.update({character: area[character] + 1})
            for d_x, d_y in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                if extended[y + d_y][x + d_x] != character:
                    perimeter.update({character: perimeter[character] + 1})

    score = 0
    for k, v in area.items():
        score += v * perimeter[k]
    return score


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    test_2 = solve(test_input_2)
    print('test_2:', test_2)

    answer = solve(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
