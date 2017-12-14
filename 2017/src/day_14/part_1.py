from functools import reduce


def hashing_round(lengths_table, rounds):
    hash_table = [x for x in range(256)]
    size = 256

    current_position = 0
    skip_size = 0

    for hash_round in range(rounds):
        for length in lengths_table:
            if current_position + length > size:
                twist_values = hash_table[current_position:] + hash_table[:(current_position + length) % size]
                twist_values = twist_values[::-1]

                twist_counter = 0
                for i in range(current_position, size):
                    hash_table[i] = twist_values[twist_counter]
                    twist_counter += 1
                for i in range(0, (current_position + length) % size):
                    hash_table[i] = twist_values[twist_counter]
                    twist_counter += 1
            else:
                twist_values = hash_table[current_position:(current_position + length)]
                twist_values = twist_values[::-1]

                twist_counter = 0
                for i in range(current_position, current_position + length):
                    hash_table[i] = twist_values[twist_counter]
                    twist_counter += 1

            current_position = (current_position + length + skip_size) % size
            skip_size += 1

    return hash_table


def knot_hash(data):
    # salt the data
    salted = []
    for character in data:
        salted.append(ord(character))
    salted += [17, 31, 73, 47, 23]

    # run 64 rounds of hashing
    sparse_hash = hashing_round(salted, 64)

    # "thicken" the hash
    dense_hash = []
    for i in range(0, 256, 16):
        current_range = sparse_hash[i: i + 16]
        xored = reduce(lambda a, b: a ^ b, current_range)
        dense_hash.append(xored)

    # return hex values
    hexed_hash = ''
    for value in dense_hash:
        hexed_hash += format(value, '0x').rjust(2, '0')

    return str(bin(int(hexed_hash, 16)))[2:].rjust(128, '0')


def solve(seed):
    solution = ''
    for i in range(128):
        partial_hash = knot_hash(seed + '-' + str(i))
        solution += partial_hash

    return solution.count('1')


def main():
    test_1 = solve('flqrgnkx')
    print("test_1:", test_1)

    answer = solve('ffayrhll')
    print("answer:", answer)


if __name__ == "__main__":
    main()
