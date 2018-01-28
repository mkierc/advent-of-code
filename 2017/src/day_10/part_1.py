test_input_1 = [3, 4, 1, 5]

with open("data.txt") as file:
    input_data = [int(x) for x in file.read().split(',')]


def knot_hash(data, size):
    hash_table = [x for x in range(size)]

    current_position = 0
    skip_size = 0

    for length in data:
        if current_position + length > size:
            twist_values = hash_table[current_position:] + hash_table[:(current_position + length) % size]
            reversed_values = twist_values[::-1]

            twist_counter = 0
            for i in range(current_position, size):
                hash_table[i] = reversed_values[twist_counter]
                twist_counter += 1
            for i in range(0, (current_position + length) % size):
                hash_table[i] = reversed_values[twist_counter]
                twist_counter += 1
        else:
            twist_values = hash_table[current_position:(current_position + length)]
            reversed_values = twist_values[::-1]

            twist_counter = 0
            for i in range(current_position, current_position + length):
                hash_table[i] = reversed_values[twist_counter]
                twist_counter += 1

        current_position = (current_position + length + skip_size) % size
        skip_size += 1
    return hash_table[0] * hash_table[1]


def main():
    test_1 = knot_hash(test_input_1, 5)
    print("test_1:", test_1)

    answer = knot_hash(input_data, 256)
    print("answer:", answer)


if __name__ == "__main__":
    main()
