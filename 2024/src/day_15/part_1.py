import itertools
from collections import defaultdict
from copy import deepcopy
from time import time

test_warehouse_1 = [[*_] for _ in [
    '########',
    '#..O.O.#',
    '##@.O..#',
    '#...O..#',
    '#.#.O..#',
    '#...O..#',
    '#......#',
    '########',
]]

test_moves_1 = '<^^>>>vv<v>>v<<'

test_warehouse_2 = [[*_] for _ in [
    '##########',
    '#..O..O.O#',
    '#......O.#',
    '#.OO..O.O#',
    '#..O@..O.#',
    '#O#..O...#',
    '#O..O..O.#',
    '#.OO.O.OO#',
    '#....O...#',
    '##########',
]]

test_moves_2 = '''<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

warehouse = []
moves = []

with open('data.txt') as file:
    a, b = file.read().split('\n\n')
    for line in a.splitlines():
        warehouse.append([*line])
    for move in b:
        moves.append(move)


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(char, end='')
        print('')


def solve(warehouse_map, move_list):
    width = len(warehouse_map[0])
    height = len(warehouse_map)

    # locate start
    cur_x, cur_y = (0, 0)
    for y, line in enumerate(warehouse_map):
        for x, char in enumerate(line):
            if char == '@':
                cur_x, cur_y = x, y

    pprint(warehouse_map)

    # simulate
    for i, move in enumerate(move_list):
        # print(move, i, 'x', cur_x, 'y', cur_y)
        # if i >= 31:
        #     input()

        # ignore new lines, todo: better parsing of input!
        if move == '\n':
            continue

        # todo: use mapping from ('^', '>', 'v', '<') to (d_x, d_y) pairs to deduplicate code
        elif move == '^':
            if warehouse_map[cur_y - 1][cur_x] == '.':
                warehouse_map[cur_y][cur_x] = '.'
                cur_y = cur_y - 1
                warehouse_map[cur_y][cur_x] = '@'
            elif warehouse_map[cur_y - 1][cur_x] == '#':
                pass
            elif warehouse_map[cur_y - 1][cur_x] == 'O':
                obstacles = []
                for i in range(cur_y - 1, -1, -1):
                    if warehouse_map[i][cur_x] == 'O':
                        obstacles.append((cur_x, i))
                    elif warehouse_map[i][cur_x] == '.':
                        obstacles.append((cur_x, i))
                        break
                    elif warehouse_map[i][cur_x] == '#':
                        obstacles = []
                        break
                if obstacles:
                    first_x, first_y = obstacles[0]
                    last_x, last_y = obstacles[-1]
                    warehouse_map[last_y][last_x] = 'O'
                    warehouse_map[first_y][first_x] = '.'
                    warehouse_map[cur_y][cur_x] = '.'
                    cur_y = cur_y - 1
                    warehouse_map[cur_y][cur_x] = '@'

        elif move == '>':
            if warehouse_map[cur_y][cur_x + 1] == '.':
                warehouse_map[cur_y][cur_x] = '.'
                cur_x = cur_x + 1
                warehouse_map[cur_y][cur_x] = '@'
            elif warehouse_map[cur_y][cur_x + 1] == '#':
                pass
            elif warehouse_map[cur_y][cur_x + 1] == 'O':
                obstacles = []
                for i in range(cur_x + 1, width):
                    if warehouse_map[cur_y][i] == 'O':
                        obstacles.append((i, cur_y))
                    elif warehouse_map[cur_y][i] == '.':
                        obstacles.append((i, cur_y))
                        break
                    elif warehouse_map[cur_y][i] == '#':
                        obstacles = []
                        break
                if obstacles:
                    first_x, first_y = obstacles[0]
                    last_x, last_y = obstacles[-1]
                    warehouse_map[last_y][last_x] = 'O'
                    warehouse_map[first_y][first_x] = '.'
                    warehouse_map[cur_y][cur_x] = '.'
                    cur_x = cur_x + 1
                    warehouse_map[cur_y][cur_x] = '@'

        elif move == 'v':
            if warehouse_map[cur_y + 1][cur_x] == '.':
                warehouse_map[cur_y][cur_x] = '.'
                cur_y = cur_y + 1
                warehouse_map[cur_y][cur_x] = '@'
            elif warehouse_map[cur_y + 1][cur_x] == '#':
                pass
            elif warehouse_map[cur_y + 1][cur_x] == 'O':
                obstacles = []
                for i in range(cur_y + 1, height):
                    if warehouse_map[i][cur_x] == 'O':
                        obstacles.append((cur_x, i))
                    elif warehouse_map[i][cur_x] == '.':
                        obstacles.append((cur_x, i))
                        break
                    elif warehouse_map[i][cur_x] == '#':
                        obstacles = []
                        break
                if obstacles:
                    first_x, first_y = obstacles[0]
                    last_x, last_y = obstacles[-1]
                    warehouse_map[last_y][last_x] = 'O'
                    warehouse_map[first_y][first_x] = '.'
                    warehouse_map[cur_y][cur_x] = '.'
                    cur_y = cur_y + 1
                    warehouse_map[cur_y][cur_x] = '@'

        elif move == '<':
            if warehouse_map[cur_y][cur_x - 1] == '.':
                warehouse_map[cur_y][cur_x] = '.'
                cur_x = cur_x - 1
                warehouse_map[cur_y][cur_x] = '@'
            elif warehouse_map[cur_y][cur_x - 1] == '#':
                pass
            elif warehouse_map[cur_y][cur_x - 1] == 'O':
                obstacles = []
                for i in range(cur_x - 1, -1, -1):
                    if warehouse_map[cur_y][i] == 'O':
                        obstacles.append((i, cur_y))
                    elif warehouse_map[cur_y][i] == '.':
                        obstacles.append((i, cur_y))
                        break
                    elif warehouse_map[cur_y][i] == '#':
                        obstacles = []
                        break
                if obstacles:
                    first_x, first_y = obstacles[0]
                    last_x, last_y = obstacles[-1]
                    warehouse_map[last_y][last_x] = 'O'
                    warehouse_map[first_y][first_x] = '.'
                    warehouse_map[cur_y][cur_x] = '.'
                    cur_x = cur_x - 1
                    warehouse_map[cur_y][cur_x] = '@'

    pprint(warehouse_map)

    gps_sum = 0
    for y, line in enumerate(warehouse_map):
        for x, char in enumerate(line):
            if char == 'O':
                gps_sum += 100 * y + x

    return gps_sum


def main():
    test_1 = solve(test_warehouse_1, test_moves_1)
    print('test_1:', test_1)

    test_2 = solve(test_warehouse_2, test_moves_2)
    print('test_2:', test_2)

    start = time()
    answer = solve(warehouse, moves)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
