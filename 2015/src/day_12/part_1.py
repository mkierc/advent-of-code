import re

test_input_1 = '[1,2,3]'
test_input_2 = '{"a":2,"b":4}'
test_input_3 = '[[[3]]]'
test_input_4 = '{"a":{"b":4},"c":-1}'
test_input_5 = '{"a":[-1,1]}'
test_input_6 = '[-1,{"a":1}]'
test_input_7 = '[]'
test_input_8 = '{}'

with open('data.txt') as file:
    input_data = file.read()


def add_numbers(string):
    number_sum = 0

    for number in re.findall(r'-?\d+', string):
        number_sum += int(number)

    return number_sum


def main():
    test_1 = add_numbers(test_input_1)
    print('test_1:', test_1)
    test_2 = add_numbers(test_input_2)
    print('test_2:', test_2)
    test_3 = add_numbers(test_input_3)
    print('test_3:', test_3)
    test_4 = add_numbers(test_input_4)
    print('test_4:', test_4)
    test_5 = add_numbers(test_input_5)
    print('test_5:', test_5)
    test_6 = add_numbers(test_input_6)
    print('test_6:', test_6)
    test_7 = add_numbers(test_input_7)
    print('test_7:', test_7)
    test_8 = add_numbers(test_input_8)
    print('test_8:', test_8)

    answer = add_numbers(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
