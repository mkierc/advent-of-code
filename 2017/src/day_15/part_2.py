import time

test_input_1 = [65, 8921]
input_data = [722, 354]


def generator_a(initial):
    a = initial
    while True:
        a = (a * 16807) % 2147483647
        if a % 4 == 0:
            yield a


def generator_b(initial):
    b = initial
    while True:
        b = (b * 48271) % 2147483647
        if b % 8 == 0:
            yield b


def generate(numbers):
    counter = 0

    gen_a = generator_a(numbers[0])
    gen_b = generator_b(numbers[1])

    for i in range(5000000):
        a = next(gen_a)
        b = next(gen_b)
        if a & 65535 == b & 65535:
            counter += 1

    return counter


def main():
    test_1 = generate(test_input_1)
    print("test_1:", test_1)

    # Intel Core i7 7700k
    # 15.8828 s - Unoptimized
    # 11.9496 s - Bitwise comparison of lowest bits
    # 11.6803 s - Without extra function call
    start = time.time()
    answer = generate(input_data)
    print("time:", time.time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()
