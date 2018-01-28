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
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", "1", " ", " ", " "],
        [" ", " ", "2", "3", "4", " ", " "],
        [" ", "5", "6", "7", "8", "9", " "],
        [" ", " ", "A", "B", "C", " ", " "],
        [" ", " ", " ", "D", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
    ]
    position_x = 1
    position_y = 3

    for digit in instructions:
        for direction in digit:
            if direction == "L" and keypad[position_y][position_x-1] != " ":
                position_x -= 1
            if direction == "R" and keypad[position_y][position_x+1] != " ":
                position_x += 1
            if direction == "U" and keypad[position_y-1][position_x] != " ":
                position_y -= 1
            if direction == "D" and keypad[position_y+1][position_x] != " ":
                position_y += 1

        code += str(keypad[position_y][position_x])

    return code


def main():
    test_1 = decode(test_input_1)
    print("test_1:", test_1)

    answer = decode(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
