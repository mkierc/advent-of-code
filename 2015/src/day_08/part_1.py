import re

test_input_1 = [
    r'""',
    r'"abc"',
    r'"aaa\"aaa"',
    r'"\x27"'
]

with open('data.txt') as file:
    input_data = file.read().splitlines()


def count_code_characters(string):
    return len(string)


def count_memory_characters(string: str):
    escaped = string.lstrip('"').rstrip('"')

    regex2 = re.findall(r'\\[\\"]', escaped)
    if regex2:
        for match in regex2:
            escaped = escaped.replace(match, '.')

    regex = re.findall(r'\\x[a-f0-9]{2}', escaped)
    if regex:
        for match in regex:
            escaped = escaped.replace(match, '.')

    return len(escaped)


def calculate_memory_footprint(string_list):
    total = 0
    for string in string_list:
        # print(count_code_characters(string))
        # print(count_memory_characters(string))
        total += count_code_characters(string) - count_memory_characters(string)
    return total


def main():
    test_1 = calculate_memory_footprint(test_input_1)
    print('test_1:', test_1)

    answer = calculate_memory_footprint(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
