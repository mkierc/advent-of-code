test_initial_state = [3, 4, 3, 1, 2]
initial_state = []

with open("data.txt") as file:
    for number in file.read().split(','):
        initial_state.append(int(number))


def quick_simulate(_state, cycles):
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in _state:
        state[fish] = state[fish] + 1
    for cycle in range(cycles):
        new_state = [
            state[1], state[2], state[3], state[4], state[5], state[6], state[7] + state[0], state[8], state[0]
        ]
        state = new_state
        # print(cycle+1, state)

    return sum(state)


def main():
    test = quick_simulate(test_initial_state, 18)
    print("test:", test)

    test = quick_simulate(test_initial_state, 80)
    print("test:", test)

    test = quick_simulate(test_initial_state, 256)
    print("test:", test)

    answer = quick_simulate(initial_state, 80)
    print("answer:", answer)

    answer = quick_simulate(initial_state, 256)
    print("answer:", answer)


if __name__ == "__main__":
    main()
