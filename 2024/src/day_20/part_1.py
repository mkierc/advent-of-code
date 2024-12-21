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


def find_path(maze):
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0

    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == 'S':
                start_x, start_y = x, y
            elif char == 'E':
                end_x, end_y = x, y

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

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
            return cost_to_node[(end_x, end_y)]


def find_all_cheats(maze, cheat_lower_bound):
    width = len(maze[0])
    height = len(maze)

    obstacle_list = []
    for y, line in enumerate(maze[1:height - 1], start=1):
        for x, char in enumerate(line[1:width - 1], start=1):
            if char == '#':
                obstacle_list.append((x, y))

    # we don't actually need to find pair, because a cheat of length 2 ns needs to start before we hit a wall,
    # and end up behind a wall, so can pass through 1-thick walls, not 2 thick, or we'd hit the wall on 3rd ns
    # obstacle_pairs = set()
    # for x, y in obstacle_list:
    #     if (x + 1, y) in obstacle_list:
    #         obstacle_pairs.add(((x, y), (x + 1, y)))
    #     if (x, y + 1) in obstacle_list:
    #         obstacle_pairs.add(((x, y), (x, y + 1)))

    true_result = find_path(maze)

    cheated_results = defaultdict(lambda: 0)
    for i, obstacle in enumerate(obstacle_list):
        x_1, y_1 = obstacle
        current_maze = deepcopy(maze)
        current_maze[y_1][x_1] = '1'

        cheated_result = find_path(current_maze)
        if cheated_result < true_result:
            cheated_results.update({true_result - cheated_result: cheated_results[true_result - cheated_result] + 1})
            print('\r', i, '/', len(obstacle_list), end='')
            # print(true_result, '-', cheated_result, '=', (true_result - cheated_result))
            # pprint(current_maze)

    print(sorted(cheated_results.items(), key=lambda _: _[0]))
    return sum([v for k, v in cheated_results.items() if k >= cheat_lower_bound])


def main():
    start = time()
    test_1 = find_all_cheats(test_racetrack, 0)
    print('test_1:', test_1)
    print('time:', time() - start)

    start = time()
    answer = find_all_cheats(racetrack, 100)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# 9324 too high
# 2141 too high

# todo: move to quicker solution from 2nd part without retracing entire path every cycle
# answer:                       1338
# bfs, retrace every cycle      227.48951125144958 s
