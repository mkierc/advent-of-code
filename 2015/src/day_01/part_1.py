test_input_1 = '(())'
test_input_2 = '()()'
test_input_3 = '((('
test_input_4 = '(()(()('
test_input_5 = '))((((('
test_input_6 = '())'
test_input_7 = '))('
test_input_8 = ')))'
test_input_9 = ')())())'


with open('data.txt') as file:
    input_data = file.read()


def find_floor(instructions):
    current_floor = 0
    for character in instructions:
        if character == '(':
            current_floor = current_floor + 1
        elif character == ')':
            current_floor = current_floor - 1
        else:
            raise NotImplemented
    return current_floor


def main():
    test_1 = find_floor(test_input_1)
    print('test_1:', test_1)
    test_2 = find_floor(test_input_2)
    print('test_2:', test_2)
    test_3 = find_floor(test_input_3)
    print('test_3:', test_3)
    test_4 = find_floor(test_input_4)
    print('test_4:', test_4)
    test_5 = find_floor(test_input_5)
    print('test_5:', test_5)
    test_6 = find_floor(test_input_6)
    print('test_6:', test_6)
    test_7 = find_floor(test_input_7)
    print('test_7:', test_7)
    test_8 = find_floor(test_input_8)
    print('test_8:', test_8)
    test_9 = find_floor(test_input_9)
    print('test_9:', test_9)

    answer = find_floor(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
