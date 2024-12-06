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

test_input_2 = [
    ['.', '.', '.', '.', '#', '.', '.', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.', '.', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '^', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '#', '.'],
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


def get_initial_params(grid):
    x = 0
    y = 0
    start_y = 0
    start_x = 0
    d_x = 0
    d_y = -1

    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == '^':
                start_y = y = i
                start_x = x = j

    # todo: faster collection
    step_list = []

    while grid[y][x] != ' ':
        # if next step is inside, continue going in that direction
        if grid[y + d_y][x + d_x] in ['.', '^']:
            x += d_x
            y += d_y
            step_list.append((y, x))
        # if next step is outside, continue going in that direction, but don't count?
        elif grid[y + d_y][x + d_x] == ' ':
            x += d_x
            y += d_y
        # if we'll hit a wall, turn right
        elif grid[y + d_y][x + d_x] == '#':
            if d_x == 0 and d_y == -1:
                d_x, d_y = 1, 0
            elif d_x == 1 and d_y == 0:
                d_x, d_y = 0, 1
            elif d_x == 0 and d_y == 1:
                d_x, d_y = -1, 0
            elif d_x == -1 and d_y == 0:
                d_x, d_y = 0, -1

    return start_y, start_x, step_list


def simulate_if_loops(start_y, start_x, grid):
    # todo: faster collection
    step_history = []

    y = start_y
    x = start_x
    d_y = -1
    d_x = 0

    while grid[y][x] != ' ':
        # if next step is inside, continue going in that direction
        if grid[y + d_y][x + d_x] in ['.', '^']:
            x += d_x
            y += d_y
            step_history.append((y, x))
            # if we've been at this position more than ~3~ 4 times
            # (start, step over, cross-over, loop back) == we're looping
        # if next step is outside == we're not looping
        elif grid[y + d_y][x + d_x] == ' ':
            return False
        # if we'll hit a wall, turn right
        elif grid[y + d_y][x + d_x] == '#':
            if step_history.count((y, x)) > 4:
                return True
            if d_x == 0 and d_y == -1:
                d_x, d_y = 1, 0
            elif d_x == 1 and d_y == 0:
                d_x, d_y = 0, 1
            elif d_x == 0 and d_y == 1:
                d_x, d_y = -1, 0
            elif d_x == -1 and d_y == 0:
                d_x, d_y = 0, -1


def solve(grid):
    grid = extend_grid(grid, 1, ' ')
    start_y, start_x, step_list = get_initial_params(grid)
    step_list = set(step_list)
    solution_set = set()

    counter = 0
    for step_y, step_x in step_list:
        new_grid = deepcopy(grid)
        new_grid[step_y][step_x] = '#'
        if simulate_if_loops(start_y, start_x, new_grid):
            print(step_y, step_x, '\t', counter, '/', len(step_list))
            solution_set.add((step_y, step_x))
        counter += 1

    return len(solution_set)


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    test_2 = solve(test_input_2)
    print('test_2:', test_2)

    start = time()
    answer = solve(input)
    print(f'time: {time() - start} s')
    print('answer:', answer)


if __name__ == '__main__':
    main()

# answer: 2162
# brute-force:             834.3863046169281 s
# loop-at-collisions:       82.4439351558685 s
