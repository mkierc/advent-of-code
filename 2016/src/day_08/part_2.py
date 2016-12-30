from day_08.part_1 import parse_instruction
from day_08.part_1 import main_screen
from day_08.part_1 import input_data


def display(screen):
    for row in screen:
        print(*row, sep="")


def main():
    for instruction in input_data:
        function, x, y = parse_instruction(instruction)
        function(main_screen, x, y)

    display(main_screen)

if __name__ == "__main__":
    main()
