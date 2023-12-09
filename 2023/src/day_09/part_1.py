test_input = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45],
]

number_list = []

with open("data.txt") as file:
    for _line in file.readlines():
        number_list.append([int(x) for x in _line.split()])


def find_next(number):
    difference_list = []

    if set(number) == {0}:
        return 0

    for i in range(len(number) - 1):
        difference_list.append(number[i + 1] - number[i])

    return number[-1] + find_next(difference_list)


def extrapolate(numbers):
    next_list = []

    for number in numbers:
        next = find_next(number)
        next_list.append(next)

    return sum(next_list)


def main():
    test = extrapolate(test_input)
    print("test:", test)

    answer = extrapolate(number_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
