from time import time

test_secret_1 = [
    123,
]

test_secret_2 = [
    1,
    10,
    100,
    2024,
]

secrets = []

with open('data.txt') as file:
    input_data = file.read().splitlines()

    for line in input_data:
        secrets.append(int(line))


def calculate_secret(secret, iterations):
    for i in range(iterations):
        result = secret * 64
        secret = result ^ secret
        secret = secret % 16777216
        result = secret // 32
        secret = result ^ secret
        secret = secret % 16777216
        result = secret * 2048
        secret = result ^ secret
        secret = secret % 16777216

    return secret


def calculate_sum(secret_list):
    checksum = 0

    for i, secret in enumerate(secret_list):
        print(i, '/', len(secret_list))
        checksum += calculate_secret(secret, 2000)

    return checksum


def main():
    test_1 = calculate_secret(test_secret_1[0], 2000)
    print('test_1:', test_1)

    test_2 = [calculate_secret(secret, 2000) for secret in test_secret_2]
    print('test_2:', test_2)

    test_3 = calculate_sum(test_secret_2)
    print('test_2:', test_3)

    start = time()
    answer = calculate_sum(secrets)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
