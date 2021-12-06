import re

import numpy

test_coord_list = [
    (0, 9, 5, 9),
    (8, 0, 0, 8),
    (9, 4, 3, 4),
    (2, 2, 2, 1),
    (7, 0, 7, 4),
    (6, 4, 2, 0),
    (0, 9, 2, 9),
    (3, 4, 1, 4),
    (0, 0, 8, 8),
    (5, 5, 8, 2),
]

coord_list = []
min_x = 99999
max_x = -99999
min_y = 99999
max_y = -99999

with open("data.txt") as file:
    for line in file.readlines():
        x_1, y_1, x_2, y_2 = re.findall(coord_regex, line)[0]
        x_1, y_1, x_2, y_2 = int(x_1), int(y_1), int(x_2), int(y_2)
        coord_list.append((x_1, y_1, x_2, y_2))
        # check for board boundaries
        if x_1 > max_x:
            max_x = x_1
        if x_2 > max_x:
            max_x = x_2

        if y_1 > max_y:
            max_y = x_1
        if y_2 > max_y:
            max_y = y_2


def find_vents(coords, _max_x, _max_y):
    ocean_map = numpy.zeros((_max_x, _max_y))
    for x_1, y_1, x_2, y_2 in coords:
        if x_1 == x_2:
            if y_1 < y_2:
                ocean_map[x_1, y_1:y_2 + 1] += 1
            else:
                ocean_map[x_1, y_2:y_1 + 1] += 1

        if y_1 == y_2:
            if x_1 < x_2:
                ocean_map[x_1:x_2 + 1, y_1] += 1
            else:
                ocean_map[x_2:x_1 + 1, y_2] += 1
    return sum(numpy.unique(ocean_map, return_counts=True)[1][2:])


def main():
    test = find_vents(test_coord_list, 10, 10)
    print("test:", test)

    answer = find_vents(coord_list, max_x+1, max_y+1)
    print("answer:", answer)


if __name__ == "__main__":
    main()
