import re
from collections import deque
from time import time

test_machines = [
    [('.', '#', '#', '.'), [{3}, {1, 3}, {2}, {2, 3}, {0, 2}, {0, 1}], [3, 5, 4, 7]],
    [('.', '.', '.', '#', '.'), [{0, 2, 3, 4}, {2, 3}, {0, 4}, {0, 1, 2}, {1, 2, 3, 4}], [7, 5, 12, 7, 2]],
    [('.', '#', '#', '#', '.', '#'), [{0, 1, 2, 3, 4}, {0, 3, 4}, {0, 1, 2, 4, 5}, {1, 2}], [10, 11, 11, 5, 10, 5]],
]

machines = []

machine_manual_regex = r'\[([.#]+)\] (.*) \{(.*)\}'
buttons_regex = r''

with open("data.txt") as file:
    for line in file.readlines():
        indicator, buttons, joltage = re.findall(machine_manual_regex, line)[0]

        indicator = tuple(x for x in indicator)

        buttons = [x.replace('(', '').replace(')', '').split(',') for x in buttons.split(' ')]
        buttons = [{int(y) for y in x} for x in buttons]

        joltage = {int(x) for x in joltage.split(',')}

        machines.append([indicator, buttons, joltage])


def generate_new_possible_states(current_state, button_list):
    new_states = []
    for buttons in button_list:
        new_state = list(current_state)
        for button_press in buttons:
            if new_state[button_press] == '.':
                new_state[button_press] = '#'
            elif new_state[button_press] == '#':
                new_state[button_press] = '.'
        new_states.append(tuple(new_state))
    return new_states


def fewest_presses_bfs(indicator_goal, buttons):
    start = tuple('.' * len(indicator_goal))
    print(start, indicator_goal, end='')

    queue = deque()
    queue.append((start, 1))

    visited_nodes = set()
    visited_nodes.add(start)

    while queue:
        current_state, clicks = queue.popleft()
        new_nodes = generate_new_possible_states(current_state, buttons)

        for node in new_nodes:
            # print(node, clicks)

            if node == indicator_goal or clicks > 10:
                print(' ', clicks)
                return clicks

            queue.append((node, clicks + 1))
            if node not in visited_nodes:
                visited_nodes.add(node)

    return None


def solve(machine_list):
    total_clicks = 0
    for indicator, buttons, joltage in machine_list:
        total_clicks += fewest_presses_bfs(indicator, buttons)
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
