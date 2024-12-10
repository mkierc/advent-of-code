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

test_input_2 = [[*_] for _ in [
    '.....0.',
    '..4321.',
    '..5..2.',
    '..6543.',
    '..7..4.',
    '..8765.',
    '..9....',
]]

input_data = []

with open('data.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        input_data.append([*line])


def next_nodes(current_path, visited, map, height, width):
    new_points = set()

    for d_x, d_y in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        last = current_path[-1]
        x, y = last[0], last[1]
        new_x, new_y = x + d_x, y + d_y

        if 0 <= new_x < width and 0 <= new_y < height:
            if map[new_y][new_x].isdigit() and int(map[new_y][new_x]) == int(map[y][x]) + 1:
                new_path = [*current_path, (new_x, new_y)]
                if not new_path in visited:
                    new_points.add((new_x, new_y))

    return new_points


def find_all_paths_dfs(x, y, map):
    height = len(map)
    width = len(map[0])

    priority_queue = []
    heapq.heappush(priority_queue, [(x, y)])

    visited_nodes = []
    visited_nodes.append([(x, y)])

    paths = []

    while priority_queue:
        # print(priority_queue)
        current_path = heapq.heappop(priority_queue)
        current_x, current_y = current_path[-1]

        # print(current_path, type(current_path), current_x, current_y)
        current_depth = map[current_y][current_x]

        if current_depth == '9':
            paths.append(current_path)

        new_nodes = next_nodes(current_path, visited_nodes, map, width, height)
        # print('new nodes', new_nodes)

        for new_x, new_y in new_nodes:
            new_path = [*current_path, (new_x, new_y)]
            heapq.heappush(priority_queue, new_path)
            visited_nodes.append(new_path)
        # print(visited_nodes)

    return len(paths)


def calculate_score(map):
    path_count = 0
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == '0':
                path_count += find_all_paths_dfs(x, y, map)

    return path_count


def main():
    # test = find_all_paths_dfs(2, 0, test_input_1)
    # print("test:", test)

    # test = find_all_paths_dfs(5, 0, test_input_2)
    # print("test:", test)

    test = calculate_score(test_input_1)
    print("test:", test)

    start = time()
    answer = calculate_score(input_data)
    print('time:', time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()

# answer: 1657
# bfs     0.18451285362243652 s
