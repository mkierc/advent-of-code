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


def find_letters(route):
    x = route[0].index('|')
    y = 0
    d_x = 0
    d_y = 1

    letters = []

    while route[y][x] != ' ':
        x += d_x
        y += d_y

        # if we stumbled upon a letter, append it to the list
        if route[y][x] not in '|-+':
            letters.append(route[y][x])

        # if we stumbled upon a bend, change the direction
        elif route[y][x] == '+':
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

    return ''.join(letters)


def main():
    test_1 = find_letters(test_input_1)
    print("test_1:", test_1)

    answer = find_letters(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
