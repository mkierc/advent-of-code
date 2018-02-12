import re

test_input_1 = '[1,2,3]'
test_input_2 = '[1,{"c":"red","b":2},3]'
test_input_3 = '{"d":"red","e":[1,2,3,4],"f":5}'
test_input_4 = '[1,"red",5]'

with open('data.txt') as file:
    input_data = file.read()


def add_numbers(string):
    number_sum = 0

    for number in re.findall(r'-?\d+', string):
        number_sum += int(number)

    return number_sum


def find_not_red_sum(string):
    regex = re.findall(r'({[^{}]+})', string)

    # remove 'red' substrings and sum not-red objects, until there are no objects left
    while regex:
        for substring in regex:
            if ':"red"' in substring:
                string = string.replace(substring, '')
            else:
                string = string.replace(substring, str(add_numbers(substring)))
        regex = re.findall(r'({[^{}]+})', string)

    return add_numbers(string)


def main():
    test_1 = find_not_red_sum(test_input_1)
    print('test_1:', test_1)
    test_2 = find_not_red_sum(test_input_2)
    print('test_2:', test_2)
    test_3 = find_not_red_sum(test_input_3)
    print('test_3:', test_3)
    test_4 = find_not_red_sum(test_input_4)
    print('test_4:', test_4)

    answer = find_not_red_sum(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
