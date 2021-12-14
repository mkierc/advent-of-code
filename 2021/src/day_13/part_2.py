import copy
import re
import numpy as np
from PIL import Image

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
    for axis, distance in _instructions:
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
    return old_points


def draw(_points, name):
    max_x = 0
    max_y = 0
    for point in _points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]

    # invert axes to draw code the correct way
    code = np.zeros((max_y+1, max_x+1))

    for point in _points:
        code[point[1], point[0]] = 255

    im = Image.fromarray(code.astype(np.uint8))
    im.save(f"{name}.png")


def main():
    test = fold(test_points, test_folding_instructions)
    draw(test, "test")

    answer = fold(points, folding_instructions)
    draw(answer, "answer")


if __name__ == "__main__":
    main()
