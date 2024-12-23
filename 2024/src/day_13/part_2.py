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

goal_offset = 10000000000000
# goal_offset = 0
test_machines = []

for machine in test_input_data.split("\n\n"):
    a_x, a_y = re.findall(r'A: X\+(\d+), Y\+(\d+)', machine)[0]
    b_x, b_y = re.findall(r'B: X\+(\d+), Y\+(\d+)', machine)[0]
    x, y = re.findall(r'X=(\d+), Y=(\d+)', machine)[0]

    test_machines.append([int(x) + goal_offset, int(y) + goal_offset, int(a_x), int(a_y), int(b_x), int(b_y)])

machines = []

with open('data.txt') as file:
    input_data = file.read().split("\n\n")

    for machine in input_data:
        a_x, a_y = re.findall(r'A: X\+(\d+), Y\+(\d+)', machine)[0]
        b_x, b_y = re.findall(r'B: X\+(\d+), Y\+(\d+)', machine)[0]
        x, y = re.findall(r'X=(\d+), Y=(\d+)', machine)[0]

        machines.append([int(x) + goal_offset, int(y) + goal_offset, int(a_x), int(a_y), int(b_x), int(b_y)])


def find_line(a_x, a_y, b_x, b_y):
    a = (a_y - b_y)
    b = (b_x - a_x)
    c = - (a_x * b_y - b_x * a_y)
    return a, b, c


def find_intersection(a_1, b_1, c_1, a_2, b_2, c_2):
    # if slope is equal -> parallel lines -> can't intersect
    slope_diff = a_1 * b_2 - b_1 * a_2
    if slope_diff == 0:
        return False

    d_x = c_1 * b_2 - b_1 * c_2
    d_y = a_1 * c_2 - c_1 * a_2
    x = d_x / slope_diff
    y = d_y / slope_diff

    return x, y


def find_prize(prize_x, prize_y, a_x, a_y, b_x, b_y):
    # find slope / linear function of vectors generated by pressing button B
    line_b = find_line(0, 0, b_x, b_y)

    # find slope / linear function of vectors generated by substracting vector of button A from the prize point
    line_a = find_line(prize_x - a_x, prize_y - a_y, prize_x, prize_y)

    # find intersection point of those two lines
    crosspoint_x, crosspoint_y = find_intersection(*line_b, *line_a)

    # divide the distance to crosspoint by length of vectors to get the number of button presses
    press_count_b = int(crosspoint_x / b_x)
    press_count_a = int((prize_x - crosspoint_x) / a_x)

    # the lines can cross outside the integer multiple of vectors, check by multiplying by button press count
    if press_count_a * a_x + press_count_b * b_x == prize_x and press_count_a * a_y + press_count_b * b_y == prize_y:
        return 3 * press_count_a + press_count_b
    return 0


def count_tokens(machine_list):
    token_total = 0
    for x, y, a_x, a_y, b_x, b_y in machine_list:
        tokens = find_prize(x, y, a_x, a_y, b_x, b_y)
        token_total += tokens
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
