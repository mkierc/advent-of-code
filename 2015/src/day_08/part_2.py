test_input_1 = [
    r'""',
    r'"abc"',
    r'"aaa\"aaa"',
    r'"\x27"'
]

with open('data.txt') as file:
    input_data = file.read().splitlines()


# TODO do it in a more pythonic way (using escape from re)
def count_encoded_characters(string: str):
    encoded = string

    encoded = encoded.replace('\\', '\\\\')
    encoded = encoded.replace(r'"', '\\"')
    encoded = '"' + encoded + '"'

    return len(encoded)


def count_code_characters(string):
    return len(string)


def calculate_memory_footprint(string_list):
    total = 0
    for string in string_list:
        total += count_encoded_characters(string) - count_code_characters(string)
    return total


def main():
    test_1 = calculate_memory_footprint(test_input_1)
    print('test_1:', test_1)

    answer = calculate_memory_footprint(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
