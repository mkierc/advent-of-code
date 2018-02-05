import re

test_input_1 = 'qjhvhtzxzqqjkmpb'
test_input_2 = 'xxyxx'
test_input_3 = 'uurcxstgmygtbstg'
test_input_4 = 'ieodomkazucvgmuy'

with open('data.txt') as file:
    input_data = file.read().splitlines()


def is_nice(string):
    # does it contain two letters that appear twice without overlapping?
    if len(re.findall('([a-z][a-z]).*\\1', string)) == 0:
        return False

    # does it contain a triplet of letters, in which first and third letter match?
    if len(re.findall('([a-z]).\\1', string)) == 0:
        return False

    return True


def count_nice(string_list):
    nice_count = 0

    for string in string_list:
        if is_nice(string):
            nice_count += 1

    return nice_count


def main():
    test_1 = is_nice(test_input_1)
    print('test_1:', test_1)
    test_2 = is_nice(test_input_2)
    print('test_2:', test_2)
    test_3 = is_nice(test_input_3)
    print('test_2:', test_3)
    test_4 = is_nice(test_input_4)
    print('test_4:', test_4)

    answer = count_nice(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
