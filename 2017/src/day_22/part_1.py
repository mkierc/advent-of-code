import time

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

    def get_current(self):
        return self.directions[self.current_direction]


def simulate(infected):
    current_direction = Direction()
    current_position = (0, 0)
    infection_count = 0

    for step in range(10000):

        if current_position in infected:
            current_direction.turn_left()
            infected.remove(current_position)
        else:
            current_direction.turn_right()
            infected.inc(current_position)
            infection_count += 1

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
