import re

with open("data.txt") as file:
    input_data = file.read().splitlines()

SCREEN_WIDTH = 50
SCREEN_HEIGHT = 6
main_screen = [['.' for col in range(SCREEN_WIDTH)] for row in range(SCREEN_HEIGHT)]


def draw_rectangle(screen, width, height):
    for row in range(width):
        for column in range(height):
            screen[column][row] = "#"


def rotate_column(screen, column, offset):
    transposed_screen = list(zip(*screen))
    rotate_row(transposed_screen, column, offset)
    untransposed_screen = list(zip(*transposed_screen))
    for row in range(SCREEN_WIDTH):
        for column in range(SCREEN_HEIGHT):
            screen[column][row] = untransposed_screen[column][row]


def rotate_row(screen, row, offset):
    offset %= SCREEN_WIDTH
    screen[row] = screen[row][-offset:] + screen[row][:-offset]


def parse_instruction(_instruction):
    if _instruction.startswith("rect"):
        x, y = re.search(r"(\d+)x(\d+)", _instruction).groups()
        return draw_rectangle, int(x), int(y)
    elif _instruction.startswith("rotate column"):
        column, offset = re.search(r"x=(\d+) by (\d+)", _instruction).groups()
        return rotate_column, int(column), int(offset)
    elif _instruction.startswith("rotate row"):
        row, offset = re.search(r"y=(\d+) by (\d+)", _instruction).groups()
        return rotate_row, int(row), int(offset)


def solve(instruction_list):
    for instruction in instruction_list:
        _function, x, y = parse_instruction(instruction)
        _function(main_screen, x, y)

    pixel_count = sum(x.count("#") for x in main_screen)
    return pixel_count


def main():
    answer = solve(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
