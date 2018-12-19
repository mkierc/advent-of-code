test_input_1 = [
    '     |          ',
    '     |  +--+    ',
    '     A  |  C    ',
    ' F---|----E|--+ ',
    '     |  |  |  D ',
    '     +B-+  +--+ ',
    '                '
]

with open('data.txt') as file:
    input_data = file.read().split('\n')[:-1]


def count_steps(route):
    x = route[0].index('|')
    y = 0
    d_x = 0
    d_y = 1

    steps = 0

    while route[y][x] != ' ':
        x += d_x
        y += d_y

        steps += 1

        # if we stumbled upon a bend, change the direction
        if route[y][x] == '+':
            if d_x == 0:  # vertical
                if route[y][x - 1] == ' ':
                    d_y, d_x = 0, 1,
                else:
                    d_y, d_x = 0, -1

            else:  # horizontal
                if route[y - 1][x] == ' ':
                    d_y, d_x = 1, 0
                else:
                    d_y, d_x = -1, 0

    return steps


def main():
    test_1 = count_steps(test_input_1)
    print("test_1:", test_1)

    answer = count_steps(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
