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
    answer = solve(363)
    print("answer:", answer)


if __name__ == "__main__":
    main()

