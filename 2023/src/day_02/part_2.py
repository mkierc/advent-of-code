import re

test_list = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]

game_list = []

with open("data.txt") as file:
    for line in file.readlines():
        game_list.append(line)


def parse_game(game_line):
    game_id, rounds = re.search(r'Game (\d+): (.*)', game_line).groups()
    rounds = rounds.split(";")

    max_red = 0
    max_green = 0
    max_blue = 0

    for _round in rounds:
        red_re = re.search(r'(\d+) red', _round)
        green_re = re.search(r'(\d+) green', _round)
        blue_re = re.search(r'(\d+) blue', _round)

        red = 0
        green = 0
        blue = 0

        if red_re:
            red = int(red_re.groups()[0])
        if green_re:
            green = int(green_re.groups()[0])
        if blue_re:
            blue = int(blue_re.groups()[0])

        if red > max_red:
            max_red = red
        if green > max_green:
            max_green = green
        if blue > max_blue:
            max_blue = blue

    return max_red*max_blue*max_green


def possible_game_sum(games):
    game_sum = 0
    for game in games:
        game_sum += parse_game(game)
    return game_sum


def main():
    test = possible_game_sum(test_list)
    print("test:", test)

    answer = possible_game_sum(game_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
