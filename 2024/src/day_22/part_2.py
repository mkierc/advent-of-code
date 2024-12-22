from collections import defaultdict
from time import time

test_secret_1 = [
    123,
]

test_secret_2 = [
    1,
    2,
    3,
    2024,
]

secrets = []

with open('data.txt') as file:
    input_data = file.read().splitlines()

    for line in input_data:
        secrets.append(int(line))


def next_secret(secret):
    result = secret * 64
    secret = result ^ secret
    secret = secret % 16777216
    result = secret // 32
    secret = result ^ secret
    secret = secret % 16777216
    result = secret * 2048
    secret = result ^ secret
    return secret % 16777216


def generate_sequence_to_price_map(secret, length):
    # print(secret)
    price_sequence = [(int(str(secret)[-1]))]
    change_sequence = [None]

    for i in range(length - 1):
        new_secret = next_secret(secret)
        price_sequence.append(int(str(new_secret)[-1]))
        change_sequence.append(int(str(new_secret)[-1]) - int(str(secret)[-1]))
        secret = new_secret

    sequences = {}

    for i in range(1, len(change_sequence) - 3):
        current_sequence = (change_sequence[i], change_sequence[i + 1], change_sequence[i + 2], change_sequence[i + 3])
        current_price = price_sequence[i + 3]

        if current_sequence not in sequences.keys():
            sequences.update({current_sequence: current_price})
        # print(current_sequence, current_price)
    return sequences


def find_optimal_sequence(secret_list):
    sequence_price_map = defaultdict(int)

    for secret in secret_list:
        current_sequence_to_price_map = generate_sequence_to_price_map(secret, 2000)
        for k, v in current_sequence_to_price_map.items():
            sequence_price_map.update({k: sequence_price_map[k] + v})

    return max([v for v in sequence_price_map.values()])


def main():
    test_1 = generate_sequence_to_price_map(test_secret_1[0], 10)
    print('test_1:', test_1)

    test_2 = find_optimal_sequence(test_secret_2)
    print('test_2:', test_2)

    start = time()
    answer = find_optimal_sequence(secrets)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# answer:   1727
# time:     6.560455560684204 s
