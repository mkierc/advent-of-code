test_input_1 = []

input_data = []

with open("data.txt") as file:
    for line in file:
        input_data.append(line)


def solve(data):
    return data


def main():
    test_1 = solve(test_input_1)
    answer = solve(input_data)

    print("test_1:", test_1)
    print("answer:", answer)


if __name__ == "__main__":
    main()
