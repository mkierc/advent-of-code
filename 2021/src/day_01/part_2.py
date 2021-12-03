test_list = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263
]

number_list = []

with open("data.txt") as file:
    for line in file.readlines():
        number_list.append(int(line))


def make_sums(numbers):
    sums = []
    a, b = 0, 0

    for i in numbers:
        sums.append(a + b + i)
        a = b
        b = i

    return sums[2:]


def count_increases(numbers):
    sums = make_sums(numbers)

    counter = 0
    previous = 0

    for i in sums:
        if i > previous:
            counter += 1
        previous = i

    return counter-1


def main():
    test = count_increases(test_list)
    print("test:", test)

    answer = count_increases(number_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
