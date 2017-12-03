from itertools import cycle

input_number = 361527

N = 10
number_map = [[0 for x in range(N)] for y in range(N)]


def fill_until_satisfied(satistfing_number):
    x = 5
    y = 4
    current_number = 1
    direction = direction_generator()

    while True:
        number_map[x][y] = current_number

        x_delta, y_delta = next(direction)
        x = x + x_delta
        y = y + y_delta

        sum_around = 0
        for position in get_positions_around(x, y):

            sum_around += number_map[position[0]][position[1]]

        current_number = sum_around

        if current_number > satistfing_number:
            number_map[x][y] = current_number
            return current_number


def get_positions_around(x, y):
    return [
        [x - 1, y - 1],
        [x - 1, y],
        [x - 1, y + 1],
        [x, y - 1],
        [x, y + 1],
        [x + 1, y - 1],
        [x + 1, y],
        [x + 1, y + 1]
    ]


def offset_generator():
    i = 1
    while True:
        i += 1
        yield i, (i // 2)


def print_number_map():
    for line in number_map:
        for number in line:
            print(str(number).rjust(7, ' '), end='')
        print()


def direction_generator():
    # DIRECTIONS        down    right   up       left
    directions = cycle([[1, 0], [0, 1], [-1, 0], [0, -1]])
    current_direction = next(directions)

    i = 1
    switcher = 1
    next_switch = offset_generator()

    while True:
        if i == switcher:
            current_direction = next(directions)
            offset = next(next_switch)[1]
            switcher = switcher + offset

        yield current_direction
        i += 1


def main():
    answer = fill_until_satisfied(input_number)
    print_number_map()

    print("answer:", answer)


if __name__ == "__main__":
    main()
