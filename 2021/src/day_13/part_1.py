import copy
import re

test_points = (
    (6, 10),
    (0, 14),
    (9, 10),
    (0, 3),
    (10, 4),
    (4, 11),
    (6, 0),
    (6, 12),
    (4, 1),
    (0, 13),
    (10, 12),
    (3, 4),
    (3, 0),
    (8, 4),
    (1, 10),
    (2, 14),
    (8, 10),
    (9, 0),
)

test_folding_instructions = [
    ['y', 7],
    ['x', 5],
]

point_regex = re.compile(r'(\d+),(\d+)')
instruction_regex = re.compile(r'.* ([xy])=(\d+)')

points = set()
folding_instructions = []

with open("data.txt") as file:
    input_data = file.read().split('\n\n')
    for point in input_data[0].split('\n'):
        x, y = re.findall(point_regex, point)[0]
        points.add((int(x), int(y)))
    for instruction in input_data[1].split('\n'):
        axis, dist = re.findall(instruction_regex, instruction)[0]
        folding_instructions.append([axis, int(dist)])


def fold(_points, _instructions):
    old_points = copy.deepcopy(_points)
    axis, distance = _instructions[0]
    new_points = set()
    for x, y in old_points:
        if axis == 'x':
            if x > distance:
                new_x = distance - (x - distance)
                new_y = y
            else:
                new_x = x
                new_y = y
        elif axis == 'y':
            if y > distance:
                new_x = x
                new_y = distance - (y - distance)
            else:
                new_x = x
                new_y = y
        else:
            raise BrokenPipeError
        new_points.add((new_x, new_y))
    old_points = new_points
    return len(old_points)


def main():
    test = fold(test_points, test_folding_instructions)
    print("test:", test)

    answer = fold(points, folding_instructions)
    print("answer:", answer)


if __name__ == "__main__":
    main()
