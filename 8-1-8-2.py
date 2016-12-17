import re

instructions = [
    "rect 1x1",
    "rotate row y=0 by 6",
    "rect 1x1",
    "rotate row y=0 by 3",
    "rect 1x1",
    "rotate row y=0 by 5",
    "rect 1x1",
    "rotate row y=0 by 4",
    "rect 2x1",
    "rotate row y=0 by 5",
    "rect 2x1",
    "rotate row y=0 by 2",
    "rect 1x1",
    "rotate row y=0 by 5",
    "rect 4x1",
    "rotate row y=0 by 2",
    "rect 1x1",
    "rotate row y=0 by 3",
    "rect 1x1",
    "rotate row y=0 by 3",
    "rect 1x1",
    "rotate row y=0 by 2",
    "rect 1x1",
    "rotate row y=0 by 6",
    "rect 4x1",
    "rotate row y=0 by 4",
    "rotate column x=0 by 1",
    "rect 3x1",
    "rotate row y=0 by 6",
    "rotate column x=0 by 1",
    "rect 4x1",
    "rotate column x=10 by 1",
    "rotate row y=2 by 16",
    "rotate row y=0 by 8",
    "rotate column x=5 by 1",
    "rotate column x=0 by 1",
    "rect 7x1",
    "rotate column x=37 by 1",
    "rotate column x=21 by 2",
    "rotate column x=15 by 1",
    "rotate column x=11 by 2",
    "rotate row y=2 by 39",
    "rotate row y=0 by 36",
    "rotate column x=33 by 2",
    "rotate column x=32 by 1",
    "rotate column x=28 by 2",
    "rotate column x=27 by 1",
    "rotate column x=25 by 1",
    "rotate column x=22 by 1",
    "rotate column x=21 by 2",
    "rotate column x=20 by 3",
    "rotate column x=18 by 1",
    "rotate column x=15 by 2",
    "rotate column x=12 by 1",
    "rotate column x=10 by 1",
    "rotate column x=6 by 2",
    "rotate column x=5 by 1",
    "rotate column x=2 by 1",
    "rotate column x=0 by 1",
    "rect 35x1",
    "rotate column x=45 by 1",
    "rotate row y=1 by 28",
    "rotate column x=38 by 2",
    "rotate column x=33 by 1",
    "rotate column x=28 by 1",
    "rotate column x=23 by 1",
    "rotate column x=18 by 1",
    "rotate column x=13 by 2",
    "rotate column x=8 by 1",
    "rotate column x=3 by 1",
    "rotate row y=3 by 2",
    "rotate row y=2 by 2",
    "rotate row y=1 by 5",
    "rotate row y=0 by 1",
    "rect 1x5",
    "rotate column x=43 by 1",
    "rotate column x=31 by 1",
    "rotate row y=4 by 35",
    "rotate row y=3 by 20",
    "rotate row y=1 by 27",
    "rotate row y=0 by 20",
    "rotate column x=17 by 1",
    "rotate column x=15 by 1",
    "rotate column x=12 by 1",
    "rotate column x=11 by 2",
    "rotate column x=10 by 1",
    "rotate column x=8 by 1",
    "rotate column x=7 by 1",
    "rotate column x=5 by 1",
    "rotate column x=3 by 2",
    "rotate column x=2 by 1",
    "rotate column x=0 by 1",
    "rect 19x1",
    "rotate column x=20 by 3",
    "rotate column x=14 by 1",
    "rotate column x=9 by 1",
    "rotate row y=4 by 15",
    "rotate row y=3 by 13",
    "rotate row y=2 by 15",
    "rotate row y=1 by 18",
    "rotate row y=0 by 15",
    "rotate column x=13 by 1",
    "rotate column x=12 by 1",
    "rotate column x=11 by 3",
    "rotate column x=10 by 1",
    "rotate column x=8 by 1",
    "rotate column x=7 by 1",
    "rotate column x=6 by 1",
    "rotate column x=5 by 1",
    "rotate column x=3 by 2",
    "rotate column x=2 by 1",
    "rotate column x=1 by 1",
    "rotate column x=0 by 1",
    "rect 14x1",
    "rotate row y=3 by 47",
    "rotate column x=19 by 3",
    "rotate column x=9 by 3",
    "rotate column x=4 by 3",
    "rotate row y=5 by 5",
    "rotate row y=4 by 5",
    "rotate row y=3 by 8",
    "rotate row y=1 by 5",
    "rotate column x=3 by 2",
    "rotate column x=2 by 3",
    "rotate column x=1 by 2",
    "rotate column x=0 by 2",
    "rect 4x2",
    "rotate column x=35 by 5",
    "rotate column x=20 by 3",
    "rotate column x=10 by 5",
    "rotate column x=3 by 2",
    "rotate row y=5 by 20",
    "rotate row y=3 by 30",
    "rotate row y=2 by 45",
    "rotate row y=1 by 30",
    "rotate column x=48 by 5",
    "rotate column x=47 by 5",
    "rotate column x=46 by 3",
    "rotate column x=45 by 4",
    "rotate column x=43 by 5",
    "rotate column x=42 by 5",
    "rotate column x=41 by 5",
    "rotate column x=38 by 1",
    "rotate column x=37 by 5",
    "rotate column x=36 by 5",
    "rotate column x=35 by 1",
    "rotate column x=33 by 1",
    "rotate column x=32 by 5",
    "rotate column x=31 by 5",
    "rotate column x=28 by 5",
    "rotate column x=27 by 5",
    "rotate column x=26 by 5",
    "rotate column x=17 by 5",
    "rotate column x=16 by 5",
    "rotate column x=15 by 4",
    "rotate column x=13 by 1",
    "rotate column x=12 by 5",
    "rotate column x=11 by 5",
    "rotate column x=10 by 1",
    "rotate column x=8 by 1",
    "rotate column x=2 by 5",
    "rotate column x=1 by 5"
]


screen_width = 50
screen_height = 6
main_screen = [['.' for col in range(screen_width)] for row in range(screen_height)]


def draw_rectangle(screen, width, height):
    for row in range(width):
        for column in range(height):
            screen[column][row] = "#"


def rotate_column(screen, column, offset):
    transposed_screen = list(zip(*screen))
    rotate_row(transposed_screen, column, offset)
    untransposed_screen = list(zip(*transposed_screen))
    for row in range(screen_width):
        for column in range(screen_height):
            screen[column][row] = untransposed_screen[column][row]


def rotate_row(screen, row, offset):
    offset %= screen_width
    screen[row] = screen[row][-offset:] + screen[row][:-offset]


def display(screen):
    for row in screen:
        print(*row, sep="")
    print()


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

for instruction in instructions:
    function, x, y = parse_instruction(instruction)
    print(function.__name__, x, y)
    function(main_screen, x, y)
    display(main_screen)

pixel_count = 0
for row in main_screen:
    for pixel in row:
        if pixel == "#":
            pixel_count += 1

print("answer:", pixel_count)
