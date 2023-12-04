import itertools
import re
from collections import defaultdict
from pprint import pprint

test_list = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]

game_list = []

with open("data.txt") as file:
    for _line in file.readlines():
        game_list.append(_line)


def wrap(engine_map):
    new_map = ['.' * (len(engine_map[0])+2)]
    for line in engine_map:
        new_map.append('.' + str(line.split()[0]) + '.')
    new_map.append('.' * (len(engine_map[0])+2))
    return new_map


def find_gears(engine_map):
    new_engine_map = wrap(engine_map)

    gear_map = defaultdict(lambda: list())

    for n, line in enumerate(new_engine_map):
        nums = re.finditer(r'(\d+)', line)
        if nums:
            for num in nums:
                start, end = num.span()
                surroundings = [new_engine_map[n-1][start-1:end+1], new_engine_map[n][start-1], new_engine_map[n][end], new_engine_map[n+1][start-1:end+1]]
                if '*' in ''.join(surroundings):
                    if match := re.search(r"\*", surroundings[0]):
                        gear_map[(n-1, start+match.span()[0])].append(int(num.group()))
                    elif new_engine_map[n][start-1] == '*':
                        gear_map[(n, start)].append(int(num.group()))
                    elif new_engine_map[n][end] == '*':
                        gear_map[(n, end+1)].append(int(num.group()))
                    elif match := re.search(r"\*", surroundings[3]):
                        gear_map[(n+1, start+match.span()[0])].append(int(num.group()))

    pprint(gear_map)

    gear_ratio_sum = 0
    for k, v in gear_map.items():
        if len(v) > 1:
            gear_ratio_sum += v[0] * v[1]

    return gear_ratio_sum


def main():
    # test = find_gears(test_list)
    # print("test:", test)

    answer = find_gears(game_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()

# 61621587 too low
# 62118152 too low
# 72246648