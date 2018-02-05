import re

import matplotlib.pyplot as plt
import numpy

with open('data.txt') as file:
    input_data = file.read().splitlines()


def turn_on(screen, x_1, y_1, x_2, y_2):
    for row in range(x_1, x_2):
        for column in range(y_1, y_2):
            screen[column][row] = 1


def turn_off(screen, x_1, y_1, x_2, y_2):
    for row in range(x_1, x_2):
        for column in range(y_1, y_2):
            screen[column][row] = 0


def toggle(screen, x_1, y_1, x_2, y_2):
    for row in range(x_1, x_2):
        for column in range(y_1, y_2):
            if screen[column][row] == 0:
                screen[column][row] = 1
            elif screen[column][row] == 1:
                screen[column][row] = 0
            else:
                raise NotImplementedError(screen[column][row])


def parse_instruction(instruction):
    x_1, y_1, x_2, y_2 = re.search(r'(\d+),(\d+) through (\d+),(\d+)', instruction).groups()

    if instruction.startswith('turn on'):
        return turn_on, int(x_1), int(y_1), int(x_2) + 1, int(y_2) + 1
    elif instruction.startswith('turn off'):
        return turn_off, int(x_1), int(y_1), int(x_2) + 1, int(y_2) + 1
    elif instruction.startswith('toggle'):
        return toggle, int(x_1), int(y_1), int(x_2) + 1, int(y_2) + 1
    else:
        raise NotImplementedError


def deploy_lights(instruction_list):
    screen = [[0 for _ in range(1000)] for _ in range(1000)]

    # process instructions and apply functions
    for instruction in instruction_list:
        _function, x_1, y_1, x_2, y_2 = parse_instruction(instruction)
        _function(screen, x_1, y_1, x_2, y_2)

    # count the lights
    lights_count = 0
    for row in screen:
        lights_count += row.count(1)

    # draw the image to satisfy my curiosity
    numpy_array = numpy.array([numpy.array(row) for row in screen])
    plt.imsave('image_1.png', numpy_array, cmap='Greys')

    return lights_count


def main():
    answer = deploy_lights(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
