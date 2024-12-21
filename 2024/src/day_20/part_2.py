import heapq
from collections import defaultdict
from copy import deepcopy
from time import time

test_racetrack = [[*_] for _ in [
    '###############',
    '#...#...#.....#',
    '#.#.#.#.#.###.#',
    '#S#...#.#.#...#',
    '#######.#.#.###',
    '#######.#.#...#',
    '#######.#.###.#',
    '###..E#...#...#',
    '###.#######.###',
    '#...###...#...#',
    '#.#####.#.###.#',
    '#.#...#.#.#...#',
    '#.#.#.#.#.#.###',
    '#...#...#...###',
    '###############',
]]

racetrack = []

with open('data.txt') as file:
    for line in file.read().splitlines():
        racetrack.append([*line])


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(char, end='')
        print('')


directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def find_cheats(x, y, cheat_length_limit, maze):
    width = len(maze[0])
    height = len(maze)

    queue = []
    heapq.heappush(queue, (0, (x, y)))

    visited_nodes = defaultdict(tuple)
    cost_to_node = defaultdict(lambda: 1_000_000_000)

    visited_nodes[(x, y)] = ()
    cost_to_node[(x, y)] = 0

    while queue:
        x, y = heapq.heappop(queue)[1]

        # generate new possible moves
        new_moves = []
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            if 0 < new_x < width - 1 and 0 < new_y < height - 1:
                new_moves.append((new_x, new_y))

        for n_x, n_y in new_moves:
            cost = 1
            new_cost = cost_to_node[(x, y)] + cost

            if (n_x, n_y) not in cost_to_node or new_cost < cost_to_node[(n_x, n_y)]:
                if new_cost <= cheat_length_limit:
                    priority = new_cost
                    heapq.heappush(queue, (priority, (n_x, n_y)))
                    visited_nodes[(n_x, n_y)] = (x, y)
                    cost_to_node[(n_x, n_y)] = new_cost
                    visited_nodes[(n_x, n_y)] = (x, y)

    cheats = {}

    for (x, y), cost in cost_to_node.items():
        if maze[y][x] != '#':
            cheats.update({(x, y): cost})

    return cheats


def find_path(maze):
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0

    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == 'S':
                start_x, start_y = x, y
            elif char == 'E':
                end_x, end_y = x, y

    queue = []
    heapq.heappush(queue, (0, (start_x, start_y)))

    visited_nodes = defaultdict(tuple)
    cost_to_node = defaultdict(lambda: 1_000_000_000)

    visited_nodes[(start_x, start_y)] = ()
    cost_to_node[(start_x, start_y)] = 0

    while queue:
        x, y = heapq.heappop(queue)[1]

        # generate new possible moves
        new_moves = []
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            if maze[new_y][new_x] != '#':
                new_moves.append((new_x, new_y))

        for n_x, n_y in new_moves:
            cost = 1
            new_cost = cost_to_node[(x, y)] + cost

            if (n_x, n_y) not in cost_to_node or new_cost < cost_to_node[(n_x, n_y)]:
                cost_to_node[(n_x, n_y)] = new_cost
                priority = new_cost
                heapq.heappush(queue, (priority, (n_x, n_y)))
                visited_nodes[(n_x, n_y)] = (x, y)

        if x == end_x and y == end_y:
            path = {}
            current = x, y
            while current:
                path.update({current: cost_to_node[current]})
                current = visited_nodes[current]

            return path, cost_to_node[(end_x, end_y)]


def find_all_cheats(maze, cheat_lower_bound):
    width = len(maze[0])
    height = len(maze)

    obstacle_list = []
    for y, line in enumerate(maze[1:height - 1], start=1):
        for x, char in enumerate(line[1:width - 1], start=1):
            if char == '#':
                obstacle_list.append((x, y))

    path, actual_cost = find_path(maze)
    # print(path)

    cheated_results = defaultdict(lambda: 0)
    i = 0
    for (x, y), cost in path.items():
        if i % 100 == 0:
            print('\r', i, '/', len(path.keys()), end='')
        i += 1
        potential_cheat_list = find_cheats(x, y, 20, maze)
        # print(potential_cheat_list)

        for (n_x, n_y), n_cost in potential_cheat_list.items():
            if cost + n_cost < path[(n_x, n_y)]:
                cheat_length = path[(n_x, n_y)] - (cost + n_cost)
                # print('x,y', x, y, 'nx, ny:', n_x, n_y, 'npath', path[(n_x, n_y)], 'cost', cost, 'n_cost', n_cost, 'cheat', cheat_length)
                cheated_results.update({cheat_length: cheated_results[cheat_length] + 1})

    cheat_list = sorted(cheated_results.items(), key=lambda _: _[0])
    print(cheat_list)
    return sum([v for k, v in cheated_results.items() if k >= cheat_lower_bound])


def main():
    start = time()
    test_1 = find_all_cheats(test_racetrack, 50)
    print('test_1:', test_1)
    print('time:', time() - start)

    start = time()
    answer = find_all_cheats(racetrack, 100)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# 1213787 too high (lower bound set to example value 50 instead of 100)
# answer:           975376
# bfs yet again...  19.00635576248169 s
