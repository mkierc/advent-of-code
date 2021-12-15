import collections
import heapq

import numpy as np

test_cave = [
    [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
    [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
    [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
    [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
    [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
    [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
    [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
    [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
    [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
    [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
]

input_cave = []

with open("data.txt") as file:
    input_data = file.read().splitlines()
    for line in input_data:
        row = []
        for character in line:
            row.append(int(character))
        input_cave.append(row)


def enlarge_map(_cave):
    old_cave = np.array(_cave)

    horizontal_caves = [old_cave]
    for i in range(4):
        new_cave = old_cave + 1
        new_cave = new_cave % 10
        np.add(new_cave, 1, out=new_cave, where=new_cave == 0)
        horizontal_caves.append(new_cave)
        old_cave = new_cave

    row = np.concatenate((horizontal_caves[0], horizontal_caves[1], horizontal_caves[2], horizontal_caves[3], horizontal_caves[4]), axis=1)

    vertical_caves = [row]
    for i in range(4):
        new_row = row + 1
        new_row = new_row % 10
        np.add(new_row, 1, out=new_row, where=new_row == 0)
        vertical_caves.append(new_row)
        row = new_row

    new_map = np.concatenate((vertical_caves[0], vertical_caves[1], vertical_caves[2], vertical_caves[3], vertical_caves[4]))

    return new_map


def find_path(_cave):
    goal = (len(_cave)-1, len(_cave[0])-1)

    priority_queue = []
    heapq.heappush(priority_queue, (0, (0, 0)))

    visited_nodes = collections.defaultdict(tuple)
    cost_to_node = collections.defaultdict(int)

    visited_nodes[(0, 0)] = None
    cost_to_node[(0, 0)] = 0

    while priority_queue:
        current = heapq.heappop(priority_queue)[1]

        if current == goal:
            return cost_to_node[goal]

        # generate destinations
        new_destinations = {
            (current[0]-1, current[1]),
            (current[0]+1, current[1]),
            (current[0], current[1]-1),
            (current[0], current[1]+1),
        }

        for dest in new_destinations:
            # check for out of bounds:
            if dest[0] < 0 or dest[1] < 0 or dest[0] >= len(_cave[0]) or dest[1] >= len(_cave):
                continue

            # add cost to node
            new_cost = cost_to_node[current] + _cave[dest[0]][dest[1]]

            if dest not in cost_to_node or new_cost < cost_to_node[dest]:
                cost_to_node[dest] = new_cost
                heapq.heappush(priority_queue, (new_cost, dest))
                visited_nodes[dest] = current


def main():
    test = find_path(enlarge_map(test_cave))
    print("test:", test)

    answer = find_path(enlarge_map(input_cave))
    print("answer:", answer)


if __name__ == "__main__":
    main()
