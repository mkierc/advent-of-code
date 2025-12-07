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

with open('data.txt') as file:
    input_data = file.read().splitlines()


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(char, end='')
        print('')
    print()


def solve(grid):
    start_index = grid[0].index('S')
    grid[0] = grid[0][:start_index] + '|' + grid[0][start_index + 1:]

    count = 0
    for y, line in enumerate(grid):
        if y == 0:
            continue
        for x, character in enumerate(line):
            if grid[y - 1][x] == '|' and character =='.':
                grid[y] = grid[y][:x] + '|' + grid[y][x + 1:]
            elif grid[y - 1][x] == '|' and character == '^':
                grid[y] = grid[y][:x-1] + '|^|' + grid[y][x + 2:]
                count += 1

    # pprint(grid)
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
