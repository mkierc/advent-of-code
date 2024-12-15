import heapq
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

# test_moves_2 = '^<<<<<'

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


def find_obstacles(x, y, direction, warehouse_map) -> set[tuple[int, int]]:
    obstacles = set()

    queue = []
    heapq.heappush(queue, (x, y))

    while queue:
        cur_x, cur_y = heapq.heappop(queue)
        # print(cur_x, cur_y, queue, obstacles)

        if direction == '^':
            if warehouse_map[cur_y - 1][cur_x] == '[':
                obstacles.add((cur_x, cur_y - 1))
                obstacles.add((cur_x + 1, cur_y - 1))
                heapq.heappush(queue, (cur_x, cur_y - 1))
                heapq.heappush(queue, (cur_x + 1, cur_y - 1))
            elif warehouse_map[cur_y - 1][cur_x] == ']':
                obstacles.add((cur_x, cur_y - 1))
                obstacles.add((cur_x - 1, cur_y - 1))
                heapq.heappush(queue, (cur_x, cur_y - 1))
                heapq.heappush(queue, (cur_x - 1, cur_y - 1))
            elif warehouse_map[cur_y - 1][cur_x] == '#':
                obstacles = []
                break
        elif direction == 'v':
            if warehouse_map[cur_y + 1][cur_x] == '[':
                obstacles.add((cur_x, cur_y + 1))
                obstacles.add((cur_x + 1, cur_y + 1))
                heapq.heappush(queue, (cur_x, cur_y + 1))
                heapq.heappush(queue, (cur_x + 1, cur_y + 1))
            elif warehouse_map[cur_y + 1][cur_x] == ']':
                obstacles.add((cur_x, cur_y + 1))
                obstacles.add((cur_x - 1, cur_y + 1))
                heapq.heappush(queue, (cur_x, cur_y + 1))
                heapq.heappush(queue, (cur_x - 1, cur_y + 1))
            elif warehouse_map[cur_y + 1][cur_x] == '#':
                obstacles = []
                break
    return obstacles


def solve(warehouse_map, move_list):
    new_warehouse_map = []

    # locate start & resize map
    cur_x, cur_y = (0, 0)
    for y, line in enumerate(warehouse_map):
        new_line = ''
        for x, char in enumerate(line):
            if char == '@':
                new_line += '@.'
                cur_x, cur_y = 2 * x, y
            elif char == '#':
                new_line += '##'
            elif char == '.':
                new_line += '..'
            elif char == 'O':
                new_line += '[]'
        new_warehouse_map.append([*new_line])

    width = len(new_warehouse_map[0])
    height = len(new_warehouse_map)

    pprint(warehouse_map)
    pprint(new_warehouse_map)

    # simulate
    for i, move in enumerate(move_list):
        print(move, i, 'x', cur_x, 'y', cur_y)
        # if i >= 31:
        #   input()

        # ignore new lines, todo: better parsing of input!
        if move == '\n':
            continue

        # todo: use mapping from ('^', '>', 'v', '<') to (d_x, d_y) pairs to deduplicate code
        elif move == '^':
            if new_warehouse_map[cur_y - 1][cur_x] == '.':
                new_warehouse_map[cur_y][cur_x] = '.'
                cur_y = cur_y - 1
                new_warehouse_map[cur_y][cur_x] = '@'
            elif new_warehouse_map[cur_y - 1][cur_x] == '#':
                pass
            elif new_warehouse_map[cur_y - 1][cur_x] in ['[', ']']:
                obstacles = find_obstacles(cur_x, cur_y, move, new_warehouse_map)
                if obstacles:
                    # clear old
                    warehouse_copy = deepcopy(new_warehouse_map)
                    for x, y in obstacles:
                        warehouse_copy[y][x] = '.'
                    # copy over
                    for x, y in obstacles:
                        warehouse_copy[y-1][x] = new_warehouse_map[y][x]
                    new_warehouse_map = warehouse_copy
                    new_warehouse_map[cur_y][cur_x] = '.'
                    cur_y = cur_y - 1
                    new_warehouse_map[cur_y][cur_x] = '@'

        elif move == '>':
            if new_warehouse_map[cur_y][cur_x + 1] == '.':
                new_warehouse_map[cur_y][cur_x] = '.'
                cur_x = cur_x + 1
                new_warehouse_map[cur_y][cur_x] = '@'
            elif new_warehouse_map[cur_y][cur_x + 1] == '#':
                pass
            elif new_warehouse_map[cur_y][cur_x + 1] in ['[', ']']:
                obstacles = []
                for i in range(cur_x + 1, width):
                    if new_warehouse_map[cur_y][i] in ['[', ']']:
                        obstacles.append((i, cur_y))
                    elif new_warehouse_map[cur_y][i] == '.':
                        obstacles.append((i, cur_y))
                        break
                    elif new_warehouse_map[cur_y][i] == '#':
                        obstacles = []
                        break
                if obstacles:
                    for x, y in obstacles:
                        if new_warehouse_map[y][x] == '[':
                            new_warehouse_map[y][x] = ']'
                        elif new_warehouse_map[y][x] == ']':
                            new_warehouse_map[y][x] = '['
                        elif new_warehouse_map[y][x] == '.':
                            new_warehouse_map[y][x] = ']'
                    new_warehouse_map[cur_y][cur_x] = '.'
                    cur_x = cur_x + 1
                    new_warehouse_map[cur_y][cur_x] = '@'

        elif move == 'v':
            if new_warehouse_map[cur_y + 1][cur_x] == '.':
                new_warehouse_map[cur_y][cur_x] = '.'
                cur_y = cur_y + 1
                new_warehouse_map[cur_y][cur_x] = '@'
            elif new_warehouse_map[cur_y + 1][cur_x] == '#':
                pass
            elif new_warehouse_map[cur_y + 1][cur_x] in ['[', ']']:
                obstacles = find_obstacles(cur_x, cur_y, move, new_warehouse_map)
                if obstacles:
                    # clear old
                    warehouse_copy = deepcopy(new_warehouse_map)
                    for x, y in obstacles:
                        warehouse_copy[y][x] = '.'
                    # copy over
                    for x, y in obstacles:
                        warehouse_copy[y+1][x] = new_warehouse_map[y][x]
                    new_warehouse_map = warehouse_copy
                    new_warehouse_map[cur_y][cur_x] = '.'
                    cur_y = cur_y + 1
                    new_warehouse_map[cur_y][cur_x] = '@'

        elif move == '<':
            if new_warehouse_map[cur_y][cur_x - 1] == '.':
                new_warehouse_map[cur_y][cur_x] = '.'
                cur_x = cur_x - 1
                new_warehouse_map[cur_y][cur_x] = '@'
            elif new_warehouse_map[cur_y][cur_x - 1] == '#':
                pass
            elif new_warehouse_map[cur_y][cur_x - 1] in ['[', ']']:
                obstacles = []
                for i in range(cur_x - 1, -1, -1):
                    if new_warehouse_map[cur_y][i] in ['[', ']']:
                        obstacles.append((i, cur_y))
                    elif new_warehouse_map[cur_y][i] == '.':
                        obstacles.append((i, cur_y))
                        break
                    elif new_warehouse_map[cur_y][i] == '#':
                        obstacles = []
                        break
                if obstacles:
                    for x, y in obstacles:
                        if new_warehouse_map[y][x] == '[':
                            new_warehouse_map[y][x] = ']'
                        elif new_warehouse_map[y][x] == ']':
                            new_warehouse_map[y][x] = '['
                        elif new_warehouse_map[y][x] == '.':
                            new_warehouse_map[y][x] = '['
                    new_warehouse_map[cur_y][cur_x] = '.'
                    cur_x = cur_x - 1
                    new_warehouse_map[cur_y][cur_x] = '@'

    pprint(new_warehouse_map)

    gps_sum = 0
    for y, line in enumerate(new_warehouse_map):
        for x, char in enumerate(line):
            if char == '[':
                gps_sum += 100 * y + x

    return gps_sum


def main():
    # test_1 = solve(test_warehouse_1, test_moves_1)
    # print('test_1:', test_1)

    # test_2 = solve(test_warehouse_2, test_moves_2)
    # print('test_2:', test_2)

    start = time()
    answer = solve(warehouse, moves)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
