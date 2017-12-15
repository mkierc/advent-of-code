import time

test_input_1 = [65, 8921]
input_data = [722, 354]


def compare_low_bits(a, b):
    a_bin = bin(a)[2:].rjust(32, '0')
    b_bin = bin(b)[2:].rjust(32, '0')
    return a_bin[-16:] == b_bin[-16:]


def generate(numbers):
    counter = 0
    a = numbers[0]
    b = numbers[1]

    for i in range(40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if compare_low_bits(a, b):
            counter += 1

    return counter


def main():
    test_1 = generate(test_input_1)
    print("test_1:", test_1)

    # Intel Core i7 7700k
    # 47.1393 s - Unoptimized
    start = time.time()
    answer = generate(input_data)
    print("time:", time.time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()
