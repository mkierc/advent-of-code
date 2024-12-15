import re
from time import time

test_input_data = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''

test_robots = []

for machine in test_input_data.splitlines():
    a, b, c, d = re.findall(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', machine)[0]
    test_robots.append((int(a), int(b), int(c), int(d)))

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


def simulate(robot_list, step_count, width, height):
    for step in range(step_count):
        new_robot_list = []
        for robot in robot_list:
            x, y, v_x, v_y = robot
            new_x, new_y = (x + v_x) % width, (y + v_y) % height,
            new_robot_list.append((new_x, new_y, v_x, v_y))
        robot_list = new_robot_list

    q_1 = [0, (width // 2), 0, (height // 2)]
    q_2 = [width // 2 + 1, width, 0, (height // 2)]
    q_3 = [0, (width // 2), (height // 2) + 1, height]
    q_4 = [(width // 2) + 1, width, (height // 2) + 1, height]

    q_1_count = 0
    q_2_count = 0
    q_3_count = 0
    q_4_count = 0

    pprint(robot_list, width, height)
    for robot in robot_list:
        if q_1[0] <= robot[0] < q_1[1] and q_1[2] <= robot[1] < q_1[3]:
            q_1_count += 1
        elif q_2[0] <= robot[0] < q_2[1] and q_2[2] <= robot[1] < q_2[3]:
            q_2_count += 1
        elif q_3[0] <= robot[0] < q_3[1] and q_3[2] <= robot[1] < q_3[3]:
            q_3_count += 1
        elif q_4[0] <= robot[0] < q_4[1] and q_4[2] <= robot[1] < q_4[3]:
            q_4_count += 1
    return q_1_count * q_2_count * q_3_count * q_4_count


def main():
    test_1 = simulate(test_robots, 100, 11, 7)
    print('test_1:', test_1)

    start = time()
    answer = simulate(robots, 100, 101, 103)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
