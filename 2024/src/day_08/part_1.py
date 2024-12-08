import itertools

test_input_1 = [[*_] for _ in [
    '............',
    '........0...',
    '.....0......',
    '.......0....',
    '....0.......',
    '......A.....',
    '............',
    '............',
    '........A...',
    '.........A..',
    '............',
    '............',
]]

input_data = []

with open('data.txt') as file:
    lines = file.read().splitlines()
    for line in lines:
        input_data.append([*line])


def pprint(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            print(char, end='')
        print('')


def solve(grid):
    antenna_map = {}
    antinode_set = set()

    width = len(grid[0])
    height = len(grid)

    for y, line in enumerate(grid):
        for x, character in enumerate(line):
            if character != '.':
                if character not in antenna_map.keys():
                    antenna_map.update({character: [(x, y)]})
                else:
                    value = antenna_map.get(character)
                    value.append((x, y))
                    antenna_map.update({character: value})

    for k, v in antenna_map.items():
        for location_1, location_2 in itertools.combinations(v, 2):
            x_1, y_1 = location_1
            x_2, y_2 = location_2

            d_x = x_1 - x_2
            d_y = y_1 - y_2

            antinode_1_x, antinode_1_y = x_1 + d_x, y_1 + d_y
            antinode_2_x, antinode_2_y = x_2 - d_x, y_2 - d_y

            if 0 <= antinode_1_x < width and 0 <= antinode_1_y < height:
                antinode_set.add((antinode_1_x, antinode_1_y))
                # grid[antinode_1_y][antinode_1_x] = 'x'
            if 0 <= antinode_2_x < width and 0 <= antinode_2_y < height:
                antinode_set.add((antinode_2_x, antinode_2_y))
                # grid[antinode_2_y][antinode_2_x] = 'x'

    # print(antenna_map)
    # print(antinode_set)

    # pprint(grid)

    return len(antinode_set)


def main():
    test_1 = solve(test_input_1)
    print('test_1:', test_1)

    answer = solve(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
