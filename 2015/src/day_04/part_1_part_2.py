from hashlib import md5

test_input_1 = 'abcdef'
test_input_2 = 'pqrstuv'

input_data = 'yzbqklnj'


def decode(secret_key, zeroes):
    index = 0

    while True:
        index += 1
        current_hash = md5(bytes(secret_key + str(index), 'utf-8')).hexdigest()

        if current_hash.startswith(''.ljust(zeroes, '0')):
            return str(current_hash) + ', ' + str(index)


def main():
    test_1 = decode(test_input_1, 5)
    print('test_1:', test_1)
    test_2 = decode(test_input_2, 5)
    print('test_2:', test_2)

    part_1 = decode(input_data, 5)
    print('part_1:', part_1)
    part_2 = decode(input_data, 6)
    print('part_2:', part_2)


if __name__ == '__main__':
    main()
