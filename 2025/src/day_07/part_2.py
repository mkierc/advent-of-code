from time import time

test_input_1 = [
    '.......S.......',
    '...............',
    '.......^.......',
    '...............',
    '......^.^......',
    '...............',
    '.....^.^.^.....',
    '...............',
    '....^.^...^....',
    '...............',
    '...^.^...^.^...',
    '...............',
    '..^...^.....^..',
    '...............',
    '.^.^.^.^.^...^.',
    '...............',
]

grid = []

with open('data.txt') as file:
    input_data = file.read().splitlines()
    for line in input_data:
        grid.append(line.split())


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(f'{char:2}', end='')
        print('')
    print()


def explode_grid(grid):
    new_grid = []
    for line in grid:
        new_grid.append([x for x in line])
    return new_grid


def solve(grid):
    grid = explode_grid(grid)
    grid[0][grid[0].index('S')] = 1

    for y, line in enumerate(grid):
        if y == 0:
            continue
        for x, character in enumerate(line):
            if grid[y - 1][x] not in ['.', '^'] and character == '.':
                grid[y][x] = grid[y - 1][x]
        for x, character in enumerate(line):
            if grid[y - 1][x] not in ['.', '^'] and character == '^':
                if grid[y][x - 1] == '.':
                    grid[y][x - 1] = 0
                if grid[y][x + 1] == '.':
                    grid[y][x + 1] = 0
                grid[y][x - 1] += grid[y - 1][x]
                grid[y][x + 1] += grid[y - 1][x]

    # pprint(grid)
    return sum([int(x) if x != '.' else 0 for x in grid[-1]])


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    start = time()
    answer = solve(input_data)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
