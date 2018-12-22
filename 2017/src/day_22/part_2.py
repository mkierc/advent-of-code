import time
from collections import defaultdict

test_input_1 = {(-1, 1), (0, -1)}


with open('data.txt') as file:
    input_data = set()

    lines = file.read().splitlines()

    HEIGHT = len(lines) // 2
    WIDTH = len(lines[0]) // 2

    for line in range(len(lines)):
        for character in range(len(lines[line])):
            if lines[character][line] == '#':
                input_data.add((character - WIDTH, line - HEIGHT))


class Direction(tuple):
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    current_direction = 2

    def turn_right(self):
        self.current_direction = (self.current_direction + 1) % 4
        return self.directions[self.current_direction]

    def turn_left(self):
        self.current_direction = (self.current_direction - 1) % 4
        return self.directions[self.current_direction]

    def reverse(self):
        self.current_direction = (self.current_direction + 2) % 4
        return self.directions[self.current_direction]

    def get_current(self):
        return self.directions[self.current_direction]


def simulate(infected):
    current_direction = Direction()
    current_position = (0, 0)
    infection_count = 0

    state = defaultdict(lambda: '.')
    for position in infected:
        state[position] = '#'

    for step in range(10000000):
        current_state = state[current_position]

        if current_state == '.':
            current_direction.turn_right()
            state[current_position] = 'W'
        elif current_state == 'W':
            state[current_position] = '#'
            infection_count += 1
        elif current_state == '#':
            current_direction.turn_left()
            state[current_position] = 'F'
        elif current_state == 'F':
            current_direction.reverse()
            del state[current_position]
        else:
            raise AssertionError('unforeseen state: ' + str(current_state))

        new_x = current_position[0] + current_direction.get_current()[0]
        new_y = current_position[1] + current_direction.get_current()[1]
        current_position = new_x, new_y

    return infection_count


def main():
    test_1 = simulate(test_input_1)
    print("test_1:", test_1)

    start = time.time()
    answer = simulate(input_data)
    print("time:", (time.time() - start))
    print("answer:", answer)


if __name__ == "__main__":
    main()
