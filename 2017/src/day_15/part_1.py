import time

test_input_1 = [65, 8921]
input_data = [722, 354]


def generate(numbers):
    counter = 0
    a = numbers[0]
    b = numbers[1]

    for i in range(40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if a & 65535 == b & 65535:
            counter += 1

    return counter


def main():
    test_1 = generate(test_input_1)
    print("test_1:", test_1)

    # Intel Core i7 7700k
    # 47.1393 s - Unoptimized
    # 15.6327 s - Bitwise comparison of lowest bits
    # 13.2834 s - Without extra function call
    start = time.time()
    answer = generate(input_data)
    print("time:", time.time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()
