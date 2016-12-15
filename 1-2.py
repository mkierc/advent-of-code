instructions = [
    'R4', 'R1', 'L2', 'R1', 'L1', 'L1', 'R1', 'L5', 'R1', 'R5', 'L2', 'R3', 'L3', 'L4', 'R4', 'R4', 'R3', 'L5', 'L1',
    'R5', 'R3', 'L4', 'R1', 'R5', 'L1', 'R3', 'L2', 'R3', 'R1', 'L4', 'L1', 'R1', 'L1', 'L5', 'R1', 'L2', 'R2', 'L3',
    'L5', 'R1', 'R5', 'L1', 'R188', 'L3', 'R2', 'R52', 'R5', 'L3', 'R79', 'L1', 'R5', 'R186', 'R2', 'R1', 'L3', 'L5',
    'L2', 'R2', 'R4', 'R5', 'R5', 'L5', 'L4', 'R5', 'R3', 'L4', 'R4', 'L4', 'L4', 'R5', 'L4', 'L3', 'L1', 'L4', 'R1',
    'R2', 'L5', 'R3', 'L4', 'R3', 'L3', 'L5', 'R1', 'R1', 'L3', 'R2', 'R1', 'R2', 'R2', 'L4', 'R5', 'R1', 'R3', 'R2',
    'L2', 'L2', 'L1', 'R2', 'L1', 'L3', 'R5', 'R1', 'R4', 'R5', 'R2', 'R2', 'R4', 'R4', 'R1', 'L3', 'R4', 'L2', 'R2',
    'R1', 'R3', 'L5', 'R5', 'R2', 'R5', 'L1', 'R2', 'R4', 'L1', 'R5', 'L3', 'L3', 'R1', 'L4', 'R2', 'L2', 'R1', 'L1',
    'R4', 'R3', 'L2', 'L3', 'R3', 'L2', 'R1', 'L4', 'R5', 'L1', 'R5', 'L2', 'L1', 'L5', 'L2', 'L5', 'L2', 'L4', 'L2',
    'R3'
]

test_input_1 = ['R2', 'L3']  # result: 5 (2E, 3N)
test_input_2 = ['R2', 'R2', 'R2']  # result: 2 (2S)
test_input_3 = ['R5', 'L5', 'R5', 'R3']  # result: 12
test_input_4 = ['R8', 'R4', 'R4', 'R8']  # result: 4


###

class Direction(tuple):
    """ Direction wrapper """
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    current_direction = 0

    def right(self):
        self.current_direction = (self.current_direction + 1) % 4
        return self.directions[self.current_direction]

    def left(self):
        self.current_direction = (self.current_direction - 1) % 4
        return self.directions[self.current_direction]

    def current(self):
        return self.directions[self.current_direction]


def solve(_input):
    current_direction = Direction()
    current_position = (0, 0)
    previous_positions = [(0, 0)]

    for move in _input:
        move_direction = move[:1]
        move_distance = int(move[1:])
        # print("DEBUG: direction:", move_direction, "distance:", move_distance)

        if move_direction == 'R':
            current_direction.right()
        else:
            current_direction.left()

        for i in range(move_distance):
            new_x = int(current_position[0] + current_direction.current()[0])
            new_y = int(current_position[1] + current_direction.current()[1])
            current_position = new_x, new_y
            if current_position in previous_positions:
                return abs(current_position[0]) + abs(current_position[1])
            previous_positions.append(current_position)
            print("DEBUG: position:", current_position)

    return abs(current_position[0]) + abs(current_position[1])


test_1 = solve(test_input_1)
test_2 = solve(test_input_2)
test_3 = solve(test_input_3)
test_4 = solve(test_input_4)
answer = solve(instructions)

print("test_1:", test_1)
print("test_2:", test_2)
print("test_3:", test_3)
print("test_4:", test_4)
print("answer:", answer)
