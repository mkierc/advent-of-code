import time
from collections import defaultdict

A = 0
B = 1
C = 2
D = 3
E = 4
F = 5

LEFT = 0
RIGHT = 1

test_steps = 6
test_input = {
    (A, 0): (1, RIGHT, B),
    (A, 1): (0, LEFT, B),

    (B, 0): (1, LEFT, A),
    (B, 1): (1, RIGHT, A),
}

input_steps = 12317297
input_data = {
    (A, 0): (1, RIGHT, B),
    (A, 1): (0, LEFT, D),

    (B, 0): (1, RIGHT, C),
    (B, 1): (0, RIGHT, F),

    (C, 0): (1, LEFT, C),
    (C, 1): (1, LEFT, A),

    (D, 0): (0, LEFT, E),
    (D, 1): (1, RIGHT, A),

    (E, 0): (1, LEFT, A),
    (E, 1): (0, RIGHT, B),

    (F, 0): (0, RIGHT, C),
    (F, 1): (0, RIGHT, E),
}


def run(steps, states):
    tape = defaultdict()
    cursor = 0
    state = 0

    for i in range(steps):
        value = tape.get(cursor, 0)
        new_value, move, next_state = states.get((state, value))

        tape[cursor] = new_value
        if move == RIGHT:
            cursor = cursor + 1
        else:
            cursor = cursor - 1
        state = next_state

    return sum(tape.values())


def main():
    test_1 = run(test_steps, test_input)
    print("test_1:", test_1)

    start = time.time()
    answer = run(input_steps, input_data)
    print("time:", (time.time() - start))
    print("answer:", answer)


if __name__ == "__main__":
    main()
