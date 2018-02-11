import re

test_input_1 = '1'

input_data = '1113122113'


def generate_next_sequence(sequence):
    next_sequence = ''

    # regex returns list of tuples containing the subsequence and the character
    # for example '22233' generates: [('222', '2'), ('33', '3')]
    subsequences = re.findall(r'((\d)\2*)', sequence)

    # iterate through the list and return the length of subsequence + the character
    for subsequence in subsequences:
        next_sequence += str(len(subsequence[0])) + subsequence[1]

    return next_sequence


def calculate_length(sequence, iterations):
    for i in range(iterations):
        sequence = generate_next_sequence(sequence)
    return len(sequence)


def main():
    test_1 = calculate_length(test_input_1, 5)
    print('test_1:', test_1)

    part_1 = calculate_length(input_data, 40)
    print('part_1:', part_1)
    part_2 = calculate_length(input_data, 50)
    print('part_2:', part_2)


if __name__ == '__main__':
    main()
