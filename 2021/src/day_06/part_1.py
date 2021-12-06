import copy

test_initial_state = [3, 4, 3, 1, 2]
initial_state = []

with open("data.txt") as file:
    for number in file.read().split(','):
        initial_state.append(int(number))


def simulate(_state, cycles):
    state = copy.deepcopy(_state)
    for cycle in range(cycles):
        for i in range(len(state)):
            if state[i] > 0:
                state[i] = state[i] - 1
            elif state[i] == 0:
                state[i] = 6
                state.append(8)

        # print(cycle+1, state)

    return len(state)


def main():
    test = simulate(test_initial_state, 18)
    print("test:", test)

    test = simulate(test_initial_state, 80)
    print("test:", test)

    answer = simulate(initial_state, 80)
    print("answer:", answer)


if __name__ == "__main__":
    main()
