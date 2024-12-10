import heapq
from time import time

test_input_1 = [[*_] for _ in [
    '89010123',
    '78121874',
    '87430965',
    '96549874',
    '45678903',
    '32019012',
    '01329801',
    '10456732',
]]

input_data = []

with open('data.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        input_data.append([*line])


def next_nodes(current, visited, map, height, width):
    new_points = set()

    for d_x, d_y in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        x, y = current[0], current[1]
        new_x, new_y = current[0] + d_x, current[1] + d_y

        if 0 <= new_x < width and 0 <= new_y < height:
            if int(map[new_y][new_x]) == int(map[y][x]) + 1:
                if not (new_x, new_y) in visited:
                    new_points.add((new_x, new_y))

    return new_points


def find_paths_dfs(x, y, map):
    height = len(map)
    width = len(map[0])

    priority_queue = []
    heapq.heappush(priority_queue, (x, y))

    visited_nodes = set()
    visited_nodes.add((x, y))

    while priority_queue:
        # print(priority_queue)
        current_x, current_y = heapq.heappop(priority_queue)

        new_nodes = next_nodes((current_x, current_y), visited_nodes, map, width, height)
        # print('new nodes', new_nodes)

        for new_x, new_y in new_nodes:
            heapq.heappush(priority_queue, (new_x, new_y))
            visited_nodes.add((new_x, new_y))
        # print(visited_nodes)

    path_count = 0
    for x, y in visited_nodes:
        if map[y][x] == '9':
            path_count += 1

    return path_count


def calculate_score(map):
    path_count = 0
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == '0':
                path_count += find_paths_dfs(x, y, map)

    return path_count


def main():
    # test = find_paths_dfs(2, 0, test_input_1)
    # print("test:", test)

    test = calculate_score(test_input_1)
    print("test:", test)

    start = time()
    answer = calculate_score(input_data)
    print('time:', time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()

# answer: 776
# bfs     0.014960527420043945 s
