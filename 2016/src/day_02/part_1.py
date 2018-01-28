test_input_1 = [
    "ULL",
    "RRDDD",
    "LURDL",
    "UUUUD"
]

with open("data.txt") as file:
    input_data = file.readlines()


def decode(instructions):
    code = ""
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    position_x = 1
    position_y = 1

    for digit in instructions:
        for direction in digit:
            if direction == "L":
                position_x -= 1
            if direction == "R":
                position_x += 1
            if direction == "U":
                position_y -= 1
            if direction == "D":
                position_y += 1

            # fix the position if outside keypad
            if position_x > 2:
                position_x = 2
            if position_y > 2:
                position_y = 2
            if position_x < 0:
                position_x = 0
            if position_y < 0:
                position_y = 0

        code += str(keypad[position_y][position_x])

    return code


def main():
    test_1 = decode(test_input_1)
    print("test_1:", test_1)

    answer = decode(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
