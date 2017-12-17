import time


def solve(step):
    current_index = 0
    second_value = -1

    for i in range(1, 50000001):
        current_index = (current_index + step) % i

        # value 0 is always at position #0, so we need to keep track of value at position #1
        if current_index == 0:
            second_value = i

        current_index += 1

    return second_value


def main():
    # Intel Core i7 7700k
    # 88 d 20 h - Unoptimized (time estimated with 2nd order polynomial regression)
    # 4.88938 s - Calculating current position only, without actually appending
    start = time.time()
    answer = solve(363)
    print("time:", time.time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()
