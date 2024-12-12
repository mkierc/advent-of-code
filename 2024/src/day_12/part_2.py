import itertools
from collections import defaultdict
from copy import deepcopy

test_input_1 = [[*_] for _ in [
    'AAAA',
    'BBCD',
    'BBCC',
    'EEEC',

]]

test_input_2 = [[*_] for _ in [
    'RRRRIICCFF',
    'RRRRIICCCF',
    'VVRRRCCFFF',
    'VVRCCCJFFF',
    'VVVVCJJCFE',
    'VVIVCCJJEE',
    'VVIIICJJEE',
    'MIIIIIJJEE',
    'MIIISIJEEE',
    'MMMISSJEEE',

]]

input_data = []

with open('data.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        input_data.append([*line])


def extend_grid(grid: list, extent: int, character: str):
    new_grid = deepcopy(grid)
    width = len(grid[0])

    for i, line in enumerate(new_grid):
        padding = [*(character * extent)]
        line = padding + line + padding
        new_grid[i] = [*line]

    for i in range(extent):
        new_grid.insert(0, [*(character * int(width + 2 * extent))])
    for i in range(extent):
        new_grid.append([*(character * int(width + 2 * extent))])

    return new_grid


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(char, end='')
        print('')


def flood_fill(x, y, grid, char):
    old_char = grid[y][x]
    grid[y][x] = char

    # print(x, y)

    if grid[y][x - 1] == old_char:
        flood_fill(x - 1, y, grid, char)
    if grid[y - 1][x] == old_char:
        flood_fill(x, y - 1, grid, char)
    if grid[y + 1][x] == old_char:
        flood_fill(x, y + 1, grid, char)
    if grid[y][x + 1] == old_char:
        flood_fill(x + 1, y, grid, char)

    # pprint(grid)


def separate_regions(grid, extent):
    substituted = []
    current_substitute_number = 0

    for y, line in enumerate(grid[extent:-extent], start=extent):
        for x, character in enumerate(line[extent:-extent], start=extent):
            if grid[y][x] not in substituted:
                flood_fill(x, y, grid, current_substitute_number)
                substituted.append(current_substitute_number)
                current_substitute_number += 1


def separate_edges(edge_list):
    indexed_edges = defaultdict(int)
    current_substitute_index = 0

    for x, y in edge_list:
        # if touches any other - use same index
        if (x, y + 1) in indexed_edges:
            indexed_edges.update({(x, y): indexed_edges[x, y + 1]})
        elif (x, y - 1) in indexed_edges:
            indexed_edges.update({(x, y): indexed_edges[x, y - 1]})
        elif (x + 1, y) in indexed_edges:
            indexed_edges.update({(x, y): indexed_edges[x + 1, y]})
        elif (x - 1, y) in indexed_edges:
            indexed_edges.update({(x, y): indexed_edges[x - 1, y]})
        # if it doesn't touch - create new index
        else:
            indexed_edges.update({(x, y): current_substitute_index})
            current_substitute_index += 1

    # print('indexed', indexed_edges, len(set([v for k, v in indexed_edges])))

    # return sum of unique values (indexes)
    return len(set([v for k, v in indexed_edges.items()]))


def solve(grid):
    extent = 1
    pad = '.'
    extended = extend_grid(grid, extent, pad)

    area = defaultdict(int)
    edge_map = defaultdict(lambda: defaultdict(list))

    separate_regions(extended, 1)

    for y, line in enumerate(extended[extent:-extent], start=extent):
        for x, character in enumerate(line[extent:-extent], start=extent):
            area.update({character: area[character] + 1})
            if extended[y][x + 1] != character:
                edge_map[character]['right'].append((x, y))
            if extended[y][x - 1] != character:
                edge_map[character]['left'].append((x, y))
            if extended[y - 1][x] != character:
                edge_map[character]['top'].append((x, y))
            if extended[y + 1][x] != character:
                edge_map[character]['bottom'].append((x, y))

    # count unique edges for each direcion
    edge_count = defaultdict(int)
    for region, directions in edge_map.items():
        for direction, edge_points in directions.items():
            edge_count.update({region: edge_count[region] + separate_edges(edge_points)})

    score = 0
    for k, v in area.items():
        score += v * edge_count[k]
    return score


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    test_2 = solve(test_input_2)
    print('test_2:', test_2)

    answer = solve(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
