import heapq
import re
from collections import defaultdict
from math import sqrt
from time import time

test_input_data = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''

test_machines = []

for machine in test_input_data.split("\n\n"):
    a_x, a_y = re.findall(r'A: X\+(\d+), Y\+(\d+)', machine)[0]
    b_x, b_y = re.findall(r'B: X\+(\d+), Y\+(\d+)', machine)[0]
    x, y = re.findall(r'X=(\d+), Y=(\d+)', machine)[0]

    test_machines.append([int(x), int(y), int(a_x), int(a_y), int(b_x), int(b_y)])

machines = []

with open('data.txt') as file:
    input_data = file.read().split("\n\n")

    for machine in input_data:
        a_x, a_y = re.findall(r'A: X\+(\d+), Y\+(\d+)', machine)[0]
        b_x, b_y = re.findall(r'B: X\+(\d+), Y\+(\d+)', machine)[0]
        x, y = re.findall(r'X=(\d+), Y=(\d+)', machine)[0]

        machines.append([int(x), int(y), int(a_x), int(a_y), int(b_x), int(b_y)])


def a_star_search(prize_x, prize_y, a_x, a_y, b_x, b_y):
    def heuristic(x, y):
        return sqrt(pow(prize_x - x, 2) + (pow(prize_y - y, 2)))

    goal = (prize_x, prize_y)

    priority_queue = []
    heapq.heappush(priority_queue, (0, (0, 0)))

    visited_nodes = defaultdict(tuple)
    cost_to_node = defaultdict(int)

    visited_nodes[(0, 0)] = None
    cost_to_node[(0, 0)] = 0

    while priority_queue:
        current_x, current_y = heapq.heappop(priority_queue)[1]

        if (current_x, current_y) == goal:
            return cost_to_node[(current_x, current_y)]

        if current_x + a_x <= prize_x and current_y + a_y <= prize_y:
            new_cost = cost_to_node[(current_x, current_y)] + 3
            if (current_x + a_x, current_y + a_y) not in cost_to_node or \
                    new_cost < cost_to_node[(current_x + a_x, current_y + a_y)]:
                cost_to_node[(current_x + a_x, current_y + a_y)] = new_cost
                priority = new_cost + heuristic(current_x + a_x, current_y + a_y)
                heapq.heappush(priority_queue, (priority, (current_x + a_x, current_y + a_y)))
                visited_nodes[(current_x + a_x, current_y + a_y)] = (current_x, current_y)

        if current_x + b_x <= prize_x and current_y + b_y <= prize_y:
            new_cost = cost_to_node[(current_x, current_y)] + 1
            if (current_x + b_x, current_y + b_y) not in cost_to_node or \
                    new_cost < cost_to_node[(current_x + b_x, current_y + b_y)]:
                cost_to_node[(current_x + b_x, current_y + b_y)] = new_cost
                priority = new_cost + heuristic(current_x + b_x, current_y + b_y)
                heapq.heappush(priority_queue, (priority, (current_x + b_x, current_y + b_y)))
                visited_nodes[(current_x + b_x, current_y + b_y)] = (current_x, current_y)

    return 0


def count_tokens(machine_list):
    token_total = 0
    for x, y, a_x, a_y, b_x, b_y in machine_list:
        tokens = a_star_search(x, y, a_x, a_y, b_x, b_y)
        token_total += tokens
        print(tokens)
        # break
    return token_total


def main():
    test_1 = count_tokens(test_machines)
    print('test_1:', test_1)

    start = time()
    answer = count_tokens(machines)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# todo: run with and without heuristic
