def solve(step):
    numbers = [0]
    current_index = 0

    for i in range(1, 2018):
        current_index = (current_index + step) % len(numbers)
        numbers.insert(current_index + 1, i)
        current_index = numbers.index(i)

    return numbers[(numbers.index(2017) + 1) % len(numbers)]


def main():
    test_1 = solve(3)
    print("test_1:", test_1)

    answer = solve(363)
    print("answer:", answer)


if __name__ == "__main__":
    main()
