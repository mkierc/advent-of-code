import re

password_regex = r'([a-z]+) (\d+)'

test_list = [
    ('forward', 5),
    ('down', 5),
    ('forward', 8),
    ('up', 3),
    ('down', 8),
    ('forward', 2)
]

command_list = []

with open("data.txt") as file:
    for line in file.readlines():
        command_list.append(*re.findall(password_regex, line))


def find_position(command_list):
    position = 0
    depth = 0
    aim = 0

    for command, delta in command_list:
        if command == 'forward':
            position += int(delta)
            depth += aim*int(delta)
        elif command == 'down':
            aim += int(delta)
        elif command == 'up':
            aim -= int(delta)

    return position, depth, position*depth


def main():
    test = find_position(test_list)
    print("test:", test)

    answer = find_position(command_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
