import heapq
from collections import defaultdict
from time import time

test_corrupted_coords = [
    (5, 4),
    (4, 2),
    (4, 5),
    (3, 0),
    (2, 1),
    (6, 3),
    (2, 4),
    (1, 5),
    (0, 6),
    (3, 3),
    (2, 6),
    (5, 1),
    (1, 2),
    (5, 5),
    (2, 5),
    (6, 5),
    (1, 4),
    (0, 4),
    (6, 4),
    (1, 1),
    (6, 1),
    (1, 0),
    (0, 5),
    (1, 6),
    (2, 0),
]
corrupted_coords = []

with open('data.txt') as file:
    for line in file.read().splitlines():
        a, b = line.split(',')
        corrupted_coords.append((int(a), int(b)))


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(char, end='')
        print('')


def find_all_paths(corrupted, width, height, fallen_count):
    # add border
    start_x, start_y = 1, 1
    width, height = width + 2, height + 2
    end_x, end_y = width - 2, height - 2

    memory_space = []
    memory_space.append([*('#' * width)])
    for i in range(1, height - 1):
        line = ['#', *('.' * (width - 2)), '#']
        memory_space.append(line)
    memory_space.append([*('#' * width)])

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    # todo: try adding all corrupted bytes, and remove them from last to first - maybe that way it's faster?
    for i, (x, y) in enumerate(corrupted):
        if i < fallen_count:
            memory_space[y + 1][x + 1] = '#'

    # pprint(memory_space)

    for i, (x, y) in enumerate(corrupted[fallen_count:], fallen_count):
        memory_space[y + 1][x + 1] = '#'

        queue = []
        heapq.heappush(queue, (0, (start_x, start_y)))

        visited_nodes = defaultdict(set)
        cost_to_node = defaultdict(lambda: 0)

        visited_nodes[(start_x, start_y)] = set()
        cost_to_node[(start_x, start_y)] = 0

        reachable = False

        while queue:
            x, y = heapq.heappop(queue)[1]

            if x == end_x and y == end_y:
                reachable = True
                break

            # generate new possible moves
            new_moves = []
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if memory_space[new_y][new_x] != '#':
                    new_moves.append((new_x, new_y))

            for n_x, n_y in new_moves:
                cost = 1
                new_cost = cost_to_node[(x, y)] + cost

                if (n_x, n_y) not in cost_to_node or new_cost < cost_to_node[(n_x, n_y)]:
                    cost_to_node[(n_x, n_y)] = new_cost
                    priority = new_cost
                    heapq.heappush(queue, (priority, (n_x, n_y)))
                    visited_nodes[(n_x, n_y)] = {(x, y)}

        if not reachable:
            return ','.join([str(_) for _ in corrupted[i]])


def main():
    test_1 = find_all_paths(test_corrupted_coords, 7, 7, 12)
    print('test_1:', test_1)

    start = time()
    answer = find_all_paths(corrupted_coords, 71, 71, 1024)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# answer:   46,23
# time:     9.658140659332275 s
