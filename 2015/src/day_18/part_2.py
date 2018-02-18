from collections import defaultdict
from time import time

test_input_1 = [
    '.#.#.#',
    '...##.',
    '#....#',
    '..#...',
    '#.#..#',
    '####..'
]

with open('data.txt') as file:
    input_data = file.read().splitlines()


# debugging helper method
def pretty_print_grid(dictionary, width, height):
    for x in range(width):
        for y in range(height):
            print(dictionary[(x, y)], end='')
        print()
    print()


def solve(initial_grid, steps):
    width, height = len(initial_grid), len(initial_grid[0])

    # initialize a dictionary
    current_grid = defaultdict(lambda: '.')
    for x in range(width):
        for y in range(height):
            if initial_grid[x][y] == '#':
                current_grid[(x, y)] = '#'

    def count_neighbors(a, b):
        return [
            current_grid[(a - 1, b - 1)],
            current_grid[(a - 1, b)],
            current_grid[(a - 1, b + 1)],
            current_grid[(a, b - 1)],
            current_grid[(a, b + 1)],
            current_grid[(a + 1, b - 1)],
            current_grid[(a + 1, b)],
            current_grid[(a + 1, b + 1)]
        ].count('#')

    # simulate the "game of life" on the dictionary
    for i in range(steps):
        new_grid = defaultdict(lambda: '.')

        # "break" the board before simulation step
        current_grid[0, 0] = '#'
        current_grid[0, width-1] = '#'
        current_grid[height-1, 0] = '#'
        current_grid[height-1, width-1] = '#'

        for x in range(width):
            for y in range(height):
                # count neighbors
                neighbor_count = count_neighbors(x, y)

                # apply rules
                if current_grid[(x, y)] == '#':
                    if neighbor_count == 2:
                        new_grid[(x, y)] = '#'
                    elif neighbor_count == 3:
                        new_grid[(x, y)] = '#'
                    else:
                        new_grid[(x, y)] = '.'
                else:
                    if neighbor_count == 3:
                        new_grid[(x, y)] = '#'
                    else:
                        new_grid[(x, y)] = '.'

        # "break" the new board after simulation step
        new_grid[0, 0] = '#'
        new_grid[0, width-1] = '#'
        new_grid[height-1, 0] = '#'
        new_grid[height-1, width-1] = '#'

        current_grid = new_grid

    return list(current_grid.values()).count('#')


def main():
    test_1 = solve(test_input_1, 5)
    print('test_1:', test_1)

    start = time()
    answer = solve(input_data, 100)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
