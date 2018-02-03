from collections import defaultdict

test_input_1 = '^v'
test_input_2 = '^>v<'
test_input_3 = '^v^v^v^v^v'

with open('data.txt') as file:
    input_data = file.read()


def count_houses(instructions):
    santa_position = (0, 0)
    robo_santa_position = (0, 0)
    visited_houses = defaultdict(int)
    visited_houses[santa_position] = 0

    for index, instruction in enumerate(instructions):
        if instruction == '^':
            delta = (1, 0)
        elif instruction == 'v':
            delta = (-1, 0)
        elif instruction == '>':
            delta = (0, 1)
        elif instruction == '<':
            delta = (0, -1)
        else:
            raise NotImplementedError(instruction)

        if index % 2 == 0:
            santa_position = (santa_position[0] + delta[0], santa_position[1] + delta[1])
            visited_houses[santa_position] = visited_houses[santa_position] + 1
        else:
            robo_santa_position = (robo_santa_position[0] + delta[0], robo_santa_position[1] + delta[1])
            visited_houses[robo_santa_position] = visited_houses[robo_santa_position] + 1

    return len(visited_houses)


def main():
    test_1 = count_houses(test_input_1)
    print('test_1:', test_1)
    test_2 = count_houses(test_input_2)
    print('test_2:', test_2)
    test_3 = count_houses(test_input_3)
    print('test_3:', test_3)

    answer = count_houses(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
