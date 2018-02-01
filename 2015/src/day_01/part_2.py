test_input_1 = ')'
test_input_2 = '()())'


with open('data.txt') as file:
    input_data = file.read()


def find_position(instructions):
    current_floor = 0
    floor_counter = 0
    for character in instructions:
        if character == '(':
            current_floor = current_floor + 1
        elif character == ')':
            current_floor = current_floor - 1
        else:
            raise NotImplemented
        floor_counter = floor_counter + 1

        if current_floor == -1:
            return floor_counter
    return 0


def main():
    test_1 = find_position(test_input_1)
    print('test_1:', test_1)
    test_2 = find_position(test_input_2)
    print('test_2:', test_2)

    answer = find_position(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
