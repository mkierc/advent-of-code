from itertools import permutations

test_list = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

number_list = []

with open("data.txt") as file:
    for line in file.readlines():
        number_list.append(int(line))


def run_expense_report(numbers):
    number_pairs = permutations(numbers, 3)

    for a, b, c in number_pairs:
        if a + b + c == 2020:
            return a * b * c

    raise AssertionError("There's no solution")


def main():
    test = run_expense_report(test_list)
    print("test:", test)

    answer = run_expense_report(number_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
