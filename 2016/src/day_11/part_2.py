import heapq
from collections import defaultdict
from itertools import combinations
from time import time

input_data_1 = [
    0, [
        ['AG', 'AM'],
        ['BG', 'CG', 'DG', 'EG'],
        ['BM', 'CM', 'DM', 'EM'],
        [],
    ]
]

input_data_2 = [
    0, [
        ['AG', 'AM', 'FG', 'GG', 'FM', 'GM'],
        ['BG', 'CG', 'DG', 'EG'],
        ['BM', 'CM', 'DM', 'EM'],
        [],
    ]
]

test_input = [
    0, [
        ['AM', 'BM'],
        ['AG'],
        ['BG'],
        [],
    ]
]


def is_solved(state):
    return state[0] == 3 \
           and len(state[1][0]) == 0 \
           and len(state[1][1]) == 0 \
           and len(state[1][2]) == 0


def are_floors_valid(old_floor, new_floor):
    return is_floor_valid(old_floor) and is_floor_valid(new_floor)


def is_floor_valid(floor):
    for item in floor:
        if item[1] == 'M':  # is a microchip
            any_generator = False
            matching_generator = False
            for another_item in floor:
                if another_item[1] == 'G':  # is a generator
                    any_generator = True
                    if item[0] == another_item[0]:  # are items of same type
                        matching_generator = True
                        break
            if not matching_generator and any_generator:
                return False
    return True


def heuristic(state):
    return 3 - state[0] + len(state[1][2]) + len(state[1][1]) * 2 + len(state[1][0]) * 3


def hashable(state):
    return (
        state[0], (
            tuple(frozenset(x) for x in state[1])
        )
    )


def deeplist(state):
    return [
        state[0], [
            list(x) for x in state[1]
        ]
    ]


def find_possible_next_states(current_state, visited):
    new_states = set()

    # try moving items down
    if current_state[0] != 0:  # lowest floor
        # move 1 item down
        for item in current_state[1][current_state[0]]:
            new_state = deeplist(current_state)
            new_state[1][new_state[0]].remove(item)
            new_state[0] -= 1
            new_state[1][new_state[0]].append(item)
            if are_floors_valid(new_state[1][new_state[0] + 1], new_state[1][new_state[0]]):
                if hashable(new_state) not in visited:
                    new_states.add(hashable(new_state))
        # move 2 items down
        for items in combinations(current_state[1][current_state[0]], 2):
            new_state = deeplist(current_state)
            new_state[1][new_state[0]].remove(items[0])
            new_state[1][new_state[0]].remove(items[1])
            new_state[0] -= 1
            new_state[1][new_state[0]].append(items[0])
            new_state[1][new_state[0]].append(items[1])
            if are_floors_valid(new_state[1][new_state[0] + 1], new_state[1][new_state[0]]):
                if hashable(new_state) not in visited:
                    new_states.add(hashable(new_state))

    # try moving items up
    if current_state[0] != 3:  # highest floor
        # move 1 item up
        for item in current_state[1][current_state[0]]:
            new_state = deeplist(current_state)
            new_state[1][new_state[0]].remove(item)
            new_state[0] += 1
            new_state[1][new_state[0]].append(item)
            if are_floors_valid(new_state[1][new_state[0] - 1], new_state[1][new_state[0]]):
                if hashable(new_state) not in visited:
                    new_states.add(hashable(new_state))
        # move 2 items up
        for items in combinations(current_state[1][current_state[0]], 2):
            new_state = deeplist(current_state)
            new_state[1][new_state[0]].remove(items[0])
            new_state[1][new_state[0]].remove(items[1])
            new_state[0] += 1
            new_state[1][new_state[0]].append(items[0])
            new_state[1][new_state[0]].append(items[1])
            if are_floors_valid(new_state[1][new_state[0] - 1], new_state[1][new_state[0]]):
                if hashable(new_state) not in visited:
                    new_states.add(hashable(new_state))
    return new_states


def a_star_search(initial_state):
    priority_queue = []
    heapq.heappush(priority_queue, (0, initial_state))

    visited_nodes = defaultdict(int)
    cost_to_node = defaultdict(lambda: 0)

    visited_nodes[hashable(initial_state)] = None
    cost_to_node[hashable(initial_state)] = 0

    max_depth = 0

    while priority_queue:
        current = heapq.heappop(priority_queue)[1]

        if is_solved(current):
            # retrace the steps of path
            total_path = [(0, current)]
            while current in visited_nodes.keys():
                current = visited_nodes[current]
                total_path.append(current)

            # return size minus 2 (first and last step are **not** molecule replaces)
            return len(total_path) - 2

        # generate new possible states
        new_states = find_possible_next_states(current, visited_nodes)
        for new in new_states:
            new_cost = cost_to_node[hashable(current)] + 1

            if new_cost > max_depth:
                max_depth = new_cost
                print('max depth', max_depth, 'visited nodes', len(visited_nodes), 'queue size', len(priority_queue))

            if new not in cost_to_node or new_cost < cost_to_node[new]:
                cost_to_node[new] = new_cost
                priority = new_cost + heuristic(new)
                heapq.heappush(priority_queue, (priority, new))
                visited_nodes[new] = hashable(current)


def main():
    # Intel Core i7 7700k
    # test        0.00100
    # part 1      3.15034
    # part 2    515.63303

    start = time()
    test_1 = a_star_search(test_input)
    print('test_1:', test_1)
    print('time:', time() - start)

    start = time()
    answer = a_star_search(input_data_2)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
