from itertools import permutations

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


def count_increases(numbers):
    counter = 0
    previous = 0

    for i in numbers:
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
