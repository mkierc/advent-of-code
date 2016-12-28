from part_1 import Direction

with open("data.txt") as file:
    input_data = str(file.readlines()[0]).split(", ")

test_input_1 = ["R2", "L3"]  # result: 5 (2E, 3N)
test_input_2 = ["R2", "R2", "R2"]  # result: 2 (2S)
test_input_3 = ["R5", "L5", "R5", "R3"]  # result: 12
test_input_4 = ["R8", "R4", "R4", "R8"]  # result: 4


def find_distance(instructions):
    current_direction = Direction()
    current_position = (0, 0)
    previous_positions = [current_position]

    for move in instructions:
        move_direction = move[:1]
        move_distance = int(move[1:])

        if move_direction == "R":
            current_direction.turn_right()
        else:
            current_direction.turn_left()

        for step in range(move_distance):
            new_x = int(current_position[0] + current_direction.get_current()[0])
            new_y = int(current_position[1] + current_direction.get_current()[1])

            current_position = new_x, new_y
            if current_position in previous_positions:
                return abs(current_position[0]) + abs(current_position[1])
            previous_positions.append(current_position)

    return abs(current_position[0]) + abs(current_position[1])


def main():
    test_1 = find_distance(test_input_1)
    test_2 = find_distance(test_input_2)
    test_3 = find_distance(test_input_3)
    test_4 = find_distance(test_input_4)
    answer = find_distance(input_data)

    print("test_1:", test_1)
    print("test_2:", test_2)
    print("test_3:", test_3)
    print("test_4:", test_4)
    print("answer:", answer)

if __name__ == "__main__":
    main()
