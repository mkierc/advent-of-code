test_input_1 = []
test_input_2 = []
test_input_3 = []

pass_phrases = []

with open("data.txt") as file:
    for line in file:
        pass


def solve(x):
    return x


def main():
    test_1 = solve(test_input_1)
    test_2 = solve(test_input_2)
    test_3 = solve(test_input_3)
    answer = solve(pass_phrases)

    print("test_1:", test_1)
    print("test_2:", test_2)
    print("test_3:", test_3)
    print("answer:", answer)


if __name__ == "__main__":
    main()
