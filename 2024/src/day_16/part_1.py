import heapq
from collections import defaultdict
from time import time

test_reindeer_maze_1 = [[*_] for _ in [
    '###############',
    '#.......#....E#',
    '#.#.###.#.###.#',
    '#.....#.#...#.#',
    '#.###.#####.#.#',
    '#.#.#.......#.#',
    '#.#.#####.###.#',
    '#...........#.#',
    '###.#.#####.#.#',
    '#...#.....#.#.#',
    '#.#.#.###.#.#.#',
    '#.....#...#.#.#',
    '#.###.#.#.#.#.#',
    '#S..#.....#...#',
    '###############',
]]

test_reindeer_maze_2 = [[*_] for _ in [
    '#################',
    '#...#...#...#..E#',
    '#.#.#.#.#.#.#.#.#',
    '#.#.#.#...#...#.#',
    '#.#.#.#.###.#.#.#',
    '#...#.#.#.....#.#',
    '#.#.#.#.#.#####.#',
    '#.#...#.#.#.....#',
    '#.#.#####.#.###.#',
    '#.#.#.......#...#',
    '#.#.###.#####.###',
    '#.#.#...#.....#.#',
    '#.#.#.#####.###.#',
    '#.#.#.........#.#',
    '#.#.#.#########.#',
    '#S#.............#',
    '#################',
]]

reindeer_maze = []

with open('data.txt') as file:
    for line in file.read().splitlines():
        reindeer_maze.append([*line])


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
    start_dir = 1

    queue = []
    heapq.heappush(queue, (0, (start_x, start_y, start_dir)))

    visited_nodes = defaultdict(tuple)
    cost_to_node = defaultdict(lambda: 1_000_000_000)

    visited_nodes[(start_x, start_y, start_dir)] = ()
    cost_to_node[(start_x, start_y, start_dir)] = 0

    while queue:
        x, y, dir = heapq.heappop(queue)[1]

        # generate new possible moves
        new_moves = []
        new_x = x + directions[dir][0]
        new_y = y + directions[dir][1]
        if maze[new_y][new_x] != '#':
            new_moves.append((new_x, new_y, dir, 1))
        new_moves.append((x, y, (dir + 1) % 4, 1000))
        new_moves.append((x, y, (dir - 1) % 4, 1000))

        for n_x, n_y, n_dir, cost in new_moves:
            new_cost = cost_to_node[(x, y, dir)] + cost

            if (n_x, n_y, n_dir) not in cost_to_node or new_cost < cost_to_node[(n_x, n_y, n_dir)]:
                cost_to_node[(n_x, n_y, n_dir)] = new_cost
                priority = new_cost
                heapq.heappush(queue, (priority, (n_x, n_y, n_dir)))
                visited_nodes[(n_x, n_y, n_dir)] = (x, y, dir)

        if x == end_x and y == end_y:
            return min([cost_to_node[(end_x, end_y, _)] for _ in range(3)])


def main():
    test_1 = find_path(test_reindeer_maze_1)
    print('test_1:', test_1)

    test_2 = find_path(test_reindeer_maze_2)
    print('test_2:', test_2)

    start = time()
    answer = find_path(reindeer_maze)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
