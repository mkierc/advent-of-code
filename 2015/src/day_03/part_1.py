from collections import defaultdict

test_input_1 = '>'
test_input_2 = '^>v<'
test_input_3 = '^v^v^v^v^v'

with open('data.txt') as file:
    input_data = file.read()


def count_houses(instructions):
    current_position = (0, 0)
    visited_houses = defaultdict(int)

    for instruction in instructions:
        visited_houses[current_position] = visited_houses[current_position] + 1
        if instruction == '^':
            current_position = (current_position[0] + 1, current_position[1])
        elif instruction == 'v':
            current_position = (current_position[0] - 1, current_position[1])
        elif instruction == '>':
            current_position = (current_position[0], current_position[1] + 1)
        elif instruction == '<':
            current_position = (current_position[0], current_position[1] - 1)
        else:
            raise NotImplementedError(instruction)

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
