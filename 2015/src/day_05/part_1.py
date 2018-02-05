import re

test_input_1 = 'ugknbfddgicrmopn'
test_input_2 = 'aaa'
test_input_3 = 'jchzalrnumimnmhp'
test_input_4 = 'haegwjzuvuyypxyu'
test_input_5 = 'dvszwmarrgswjxmb'

with open('data.txt') as file:
    input_data = file.read().splitlines()


def is_nice(string):
    # does it contain at least three vowels?
    vowel_count = 0
    for letter in string:
        if letter in 'aeiou':
            vowel_count += 1
    if vowel_count < 3:
        return False

    # does it contain at least two consecutive letters?
    if len(re.findall('([a-z])\\1', string)) == 0:
        return False

    # does it contain on of naugthy substrings?
    for naugthy_substring in ['ab', 'cd', 'pq', 'xy']:
        if naugthy_substring in string:
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
    test_5 = is_nice(test_input_5)
    print('test_5:', test_5)

    answer = count_nice(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
