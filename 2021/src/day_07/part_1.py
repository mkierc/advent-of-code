import statistics

test_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
positions = []

with open("data.txt") as file:
    for number in file.read().split(','):
        positions.append(int(number))


def align_crabs(_positions):
    m = statistics.median(_positions)
    cost = 0
    for crab in _positions:
        cost += abs(crab - m)
    return cost


def main():
    test = align_crabs(test_positions)
    print("test:", test)

    answer = align_crabs(positions)
    print("answer:", answer)


if __name__ == "__main__":
    main()
