test_input_1 = ['ne', 'ne', 'ne']
test_input_2 = ['ne', 'ne', 'sw', 'sw']
test_input_3 = ['ne', 'ne', 's', 's']
test_input_4 = ['se', 'sw', 'se', 'sw', 'sw']

with open("data.txt") as file:
    input_data = file.read().split(',')

moves = {
    'n': (-1, 0),
    'ne': (0, 1),
    'se': (1, 1),
    's': (1, 0),
    'sw': (0, -1),
    'nw': (-1, -1)
}


def calculate_distance(position):
    if position[0] >= 0 and position[1] >= 0:
        return max(abs(position[0]), abs(position[1]))
    elif position[0] < 0 and position[1] < 0:
        return max(abs(position[0]), abs(position[1]))
    elif position[0] >= 0 > position[1]:
        return abs(position[0]) + abs(position[1])
    elif position[0] < 0 <= position[1]:
        return abs(position[0]) + abs(position[1])
    else:
        raise AssertionError('impossibru')


def find_distance(directions):
    current_position = [0, 0]

    max_distance = 0

    for direction in directions:
        current_position[0] += moves.get(direction)[0]
        current_position[1] += moves.get(direction)[1]
        current_distance = calculate_distance(current_position)
        if current_distance > max_distance:
            max_distance = current_distance

    return max_distance


def main():
    test_1 = find_distance(test_input_1)
    print("test_1:", test_1)
    test_2 = find_distance(test_input_2)
    print("test_2:", test_2)
    test_3 = find_distance(test_input_3)
    print("test_3:", test_3)
    test_4 = find_distance(test_input_4)
    print("test_4:", test_4)

    answer = find_distance(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
