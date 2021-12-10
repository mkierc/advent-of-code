import copy
import numpy as np
from skimage import measure

test_map = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
]

floor_map = []

with open("../day_08/data.txt") as file:
    for line in file.read().splitlines():
        floor_map.append([int(x) for x in line])


def find_low_spots(_map):
    low_spots = []
    for i, row in enumerate(_map):
        for j, value in enumerate(row):
            adjacent = []
            if not j == 0:
                adjacent.append(_map[i][j-1])
            if not j == len(row)-1:
                adjacent.append(_map[i][j+1])
            if not i == 0:
                adjacent.append(_map[i-1][j])
            if not i == len(_map) - 1:
                adjacent.append(_map[i+1][j])

            is_low = True
            for a in adjacent:
                if value >= a:
                    is_low = False
                    break
            if is_low:
                low_spots.append((i, j))
    return low_spots


def find_basins(_map):
    basins = np.array(copy.deepcopy(_map))
    basins[basins < 9] = 1
    basins[basins == 9] = 0
    basins = measure.label(basins, background=0, connectivity=1)
    basin_sizes = np.unique(basins, return_counts=True)[1]
    top_3 = sorted(basin_sizes[1:])[-3:]

    return np.prod(top_3)


def main():
    test = find_basins(test_map)
    print("test:", test)

    answer = find_basins(floor_map)
    print("answer:", answer)


if __name__ == "__main__":
    main()
