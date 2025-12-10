import heapq
import re
from collections import defaultdict
from time import time

import scipy

test_machines = [
    [[{3}, {1, 3}, {2}, {2, 3}, {0, 2}, {0, 1}], [3, 5, 4, 7]],
    [[{0, 2, 3, 4}, {2, 3}, {0, 4}, {0, 1, 2}, {1, 2, 3, 4}], [7, 5, 12, 7, 2]],
    [[{0, 1, 2, 3, 4}, {0, 3, 4}, {0, 1, 2, 4, 5}, {1, 2}], [10, 11, 11, 5, 10, 5]],
]

machines = []

machine_manual_regex = r'\[[.#]+\] (.*) \{(.*)\}'
buttons_regex = r''

with open("data.txt") as file:
    for line in file.readlines():
        buttons, joltage = re.findall(machine_manual_regex, line)[0]

        buttons = [x.replace('(', '').replace(')', '').split(',') for x in buttons.split(' ')]
        buttons = [[int(y) for y in x] for x in buttons]

        joltage = [int(x) for x in joltage.split(',')]

        machines.append([buttons, joltage])


def generate_new_possible_states(current_state, button_list, joltage_goal):
    new_states = []
    for buttons in button_list:
        new_state = list(current_state)
        overjolted = False
        for button_press in buttons:
            new_state[button_press] += 1
            if new_state[button_press] > joltage_goal[button_press]:
                overjolted = True
                break

        if not overjolted:
            new_states.append(tuple(new_state))
    return new_states


## way too slow, even with pruning (prune at too-high joltage) and heuristic (element-wise difference to goal state)
#
# def fewest_presses_a_star(joltage_goal, buttons):
#     start = tuple(0 for _ in range(len(joltage_goal)))
#     joltage_goal = tuple(joltage_goal)
#     buttons = sorted(buttons, key=lambda x: -len(x))
#     print(start, joltage_goal, end='')
#
#     def heuristic(x, y):
#         return 1000 * sum(abs(x[_] - y[_]) for _ in range(len(joltage_goal)))
#
#     priority_queue = []
#     heapq.heappush(priority_queue, (0, start))
#
#     visited_nodes = defaultdict(tuple)
#     cost_to_node = defaultdict(int)
#
#     visited_nodes[start] = None
#     cost_to_node[start] = 0
#
#     max_depth = 0
#
#     while priority_queue:
#         current = heapq.heappop(priority_queue)[1]
#
#         # print(current, joltage_goal)
#         if current == joltage_goal:
#             print(' ', cost_to_node[current])
#             return cost_to_node[current]
#
#         for new in generate_new_possible_states(current, buttons, joltage_goal):
#             # print(new)
#             new_cost = cost_to_node[current] + 1
#
#             if new_cost > max_depth:
#                 max_depth = new_cost
#                 print('max depth', max_depth, 'visited nodes', len(visited_nodes), 'queue size', len(priority_queue))
#
#             if new not in cost_to_node or new_cost < cost_to_node[new]:
#                 cost_to_node[new] = new_cost
#                 priority = new_cost + heuristic(current, new)
#                 heapq.heappush(priority_queue, (priority, new))
#                 visited_nodes[new] = current
#
#     return None


def fewest_presses_linear(joltage_goal, buttons):
    button_mask_matrix = []

    for button in buttons:
        mask = []
        for i in range(len(joltage_goal)):
            if i in button:
                mask.append(1)
            else:
                mask.append(0)
        button_mask_matrix.append(mask)

    # print(button_mask_matrix)

    c = [1 for _ in range(len(button_mask_matrix))]

    A = list(map(list, zip(*button_mask_matrix))) # transpose button matrix
    b = joltage_goal

    return int(scipy.optimize.linprog(c=c, A_eq=A, b_eq=b, method='highs', integrality=1).fun)


def solve(machine_list):
    total_clicks = 0
    for buttons, joltage in machine_list:
        # total_clicks += fewest_presses_a_star(joltage, buttons)
        total_clicks += fewest_presses_linear(joltage, buttons)
    return total_clicks


def main():
    test_1 = solve(test_machines)
    print('test_1:', test_1)

    start = time()
    answer = solve(machines)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
