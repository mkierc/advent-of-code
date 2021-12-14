import copy
import numpy as np

test_input = [
    [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
    [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
    [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
    [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
    [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
    [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
    [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
    [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
    [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
    [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
]

input_data = []

with open("data.txt") as file:
    for line in file.read().splitlines():
        row = []
        for value in line:
            row.append(int(value))
        input_data.append(row)


def count_flashes(_octopus_map, steps):
    octopus_map = np.array(_octopus_map)
    octopus_map = np.pad(octopus_map, ((1, 1), (1, 1)), mode='constant', constant_values=-1.0)
    flash_counter = 0
    for i in range(0, steps+1):
        new_octopus_map = step(octopus_map)
        flashes = np.count_nonzero(octopus_map == 0)
        flash_counter += flashes
        octopus_map = new_octopus_map

    return flash_counter


def step(_octopus_map):
    previous_step = copy.deepcopy(_octopus_map)

    # increase energy level
    current_step = copy.deepcopy(_octopus_map)
    np.add(current_step, 1, out=current_step, where=current_step >= 0)
    np.mod(current_step, 10, out=current_step, where=current_step >= 0)

    # propagate flashing
    while not np.array_equal(current_step, previous_step):
        previous_step = copy.deepcopy(current_step)
        flashing = np.array(np.where(current_step == 0)).T
        current_step[current_step == 0] = -2
        for x, y in flashing:
            np.add(current_step[x-1:x+2, y-1:y+2], 1, out=current_step[x-1:x+2,y-1:y+2], where=current_step[x-1:x+2,y-1:y+2]>0)
            np.mod(current_step[x-1:x+2, y-1:y+2], 10, out=current_step[x-1:x+2,y-1:y+2], where=current_step[x-1:x+2,y-1:y+2]>0)
    current_step[current_step == -2] = 0
    return current_step


def main():
    test = count_flashes(test_input, 100)
    print("test:", test)

    answer = count_flashes(input_data, 100)
    print("answer:", answer)


if __name__ == "__main__":
    main()
