test_input_1 = [0, 3, 0, 1, -3]

input_instruction_set = []

with open("data.txt") as file:
    for line in file:
        input_instruction_set.append(int(line))


def solve(instruction_set):
    pointer = 0
    counter = 0
    while 0 <= pointer < len(instruction_set):
        # save current instruction position for incrementation later
        previous_pointer = pointer
        # read current instruction & change pointer to new location
        pointer = previous_pointer + instruction_set[previous_pointer]
        # increment old instruction by one
        instruction_set[previous_pointer] += 1
        # increment instruction counter
        counter += 1
    return counter


def main():
    test_1 = solve(test_input_1)
    print("test_1:", test_1)

    answer = solve(input_instruction_set)
    print("answer:", answer)


if __name__ == "__main__":
    main()
