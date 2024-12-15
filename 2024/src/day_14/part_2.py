import itertools
import re
from time import time

robots = []

with open('data.txt') as file:
    input_data = file.read().splitlines()

    for machine in input_data:
        a, b, c, d = re.findall(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', machine)[0]
        robots.append((int(a), int(b), int(c), int(d)))


def pprint(robot_list, width, height):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for x, y, v_x, v_y in robot_list:
        grid[y][x] = 'X'

    for y in range(height):
        for x in range(width):
            print(grid[y][x], end='')
        print('')


def simulate(robot_list, width, height):
    for step in range(10000):
        new_robot_list = []
        for robot in robot_list:
            x, y, v_x, v_y = robot
            new_x, new_y = (x + v_x) % width, (y + v_y) % height,
            new_robot_list.append((new_x, new_y, v_x, v_y))
        robot_list = new_robot_list

        adj_count = 0
        # todo: find a better way to recognize patterns
        for a, b in itertools.combinations(robot_list, 2):
            if (abs(a[0] - b[0]) == 1 and a[1] == b[1]) or (abs(a[1] - b[1]) == 1 and a[0] == b[0]):
                adj_count += 1

        if adj_count > 200:
            pprint(robot_list, width, height)
            print(adj_count)
            return step + 1

        # dirty solution based on printing everything
        # if ((step - 38) % 101) == 0:
        #     print(step)
        #     pprint(robot_list, width, height)


def main():
    start = time()
    answer = simulate(robots, 101, 103)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# 543 too low
# 2462 too low
# 2563 too low
# 7411 too low
#
# answer: 7412
# brute-force with combinations       113.78566980361938 s
