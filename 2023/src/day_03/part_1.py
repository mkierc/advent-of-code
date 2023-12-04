import re
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


def count_parts(engine_map):
    new_engine_map = wrap(engine_map)
    pprint(new_engine_map)

    part_sum = 0

    for n, line in enumerate(new_engine_map):
        nums = re.finditer(r'(\d+)', line)
        if nums:
            for num in nums:
                start, end = num.span()
                surroundings = new_engine_map[n-1][start-1:end+1] + new_engine_map[n][start-1] + new_engine_map[n][end] + new_engine_map[n+1][start-1:end+1]
                print(f'{n:>3}   :', surroundings, ''.join(set(surroundings)))
                if len(''.join(set(surroundings))) > 1:
                    part_sum += int(num.group())
    return part_sum


def main():
    test = count_parts(test_list)
    print("test:", test)

    answer = count_parts(game_list)
    print("answer:", answer)


if __name__ == "__main__":
    main()
