import re

import time

test_input_1 = [('s', '1'), ('x', '3', '4'), ('p', 'e', 'b')]


def parse_input():
    with open("data.txt") as file:
        input_data = file.read().split(',')

    commands = []

    for line in input_data:
        if re.match('[a-z]\d+/\d+', line):
            regex = re.search('([a-z])(\d+)/(\d+)', line)
            dance_type = regex.group(1)
            position_1 = regex.group(2)
            position_2 = regex.group(3)
            commands.append((dance_type, position_1, position_2))
        elif re.match('[a-z][a-z]/[a-z]+', line):
            regex = re.search('([a-z])([a-z])/([a-z])', line)
            dance_type = regex.group(1)
            position_1 = regex.group(2)
            position_2 = regex.group(3)
            commands.append((dance_type, position_1, position_2))
        elif re.match('[a-z]\d+', line):
            regex = re.search('([a-z])(\d+)', line)
            dance_type = regex.group(1)
            position = regex.group(2)
            commands.append((dance_type, position))
        else:
            raise AssertionError('unforeseen position: ' + line)

    return commands


def dance(commands, size, cycles):
    state = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    # trim the list for the test case
    state = state[:size]

    # remember previous states to find a cycle
    states = []

    for i in range(cycles):

        # when cycle is found, calculate the order of bilionth dance
        if ''.join(state) in states:
            return states[cycles % i]

        states.append(''.join(state))

        for command in commands:
            if command[0] == 's':
                spin_offset = int(command[1])
                state = state[-spin_offset:] + state[:-spin_offset]
            elif command[0] == 'x':
                position_1 = int(command[1])
                position_2 = int(command[2])
                state[position_1], state[position_2] = state[position_2], state[position_1]
            elif command[0] == 'p':
                position_1 = state.index(command[1])
                position_2 = state.index(command[2])
                state[position_1], state[position_2] = state[position_2], state[position_1]
            else:
                raise AssertionError('unforeseen command: ' + command)

    # if cycle wasn't found, return current state for test case
    return ''.join(state)


def main():
    test_1 = dance(test_input_1, 5, 2)
    print("test_1:", test_1)

    # Intel Core i7 7700k
    # 61 d 21 h - Unoptimized (extrapolated from 5.34541 s / 1000 cycles)
    # 0.18183 s - Calculating the order using cycle in dance positions
    start = time.time()
    answer = dance(parse_input(), 16, 1000000000)
    print("time:", (time.time() - start))
    print("answer:", answer)

    # Incidentally I found the correct answer with unoptimized version, by running it for 100 cycles,
    # that let me get the second star in a minute...
    incidental_correct_answer = dance(parse_input(), 16, 100)
    print("accidental correct answer after only 100 cycles\nbungle:", incidental_correct_answer)


if __name__ == "__main__":
    main()
