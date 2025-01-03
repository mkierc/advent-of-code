import sys
from time import time

sys.setrecursionlimit(5000)

test_input_1 = '''
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
'''

test_input_2 = '''
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
'''

test_input_3 = '''
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
'''

pipe_maze = ''

with open("data.txt") as file:
    for _line in file.readlines():
        pipe_maze += _line


def print_maze(maze):
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            print(char, end='')
        print('')


def wrap(maze):
    maze = maze.split()

    new_maze = []
    for i in range(len(maze) + 2):
        new_maze.append([])
    for i in range(len(maze[0]) + 2):
        new_maze[0].append('.')
    for i, line in enumerate(maze):
        new_maze[i + 1].append('.')
        new_maze[i + 1].extend(line.split()[0])
        new_maze[i + 1].append('.')
    for i in range(len(maze[0]) + 2):
        new_maze[-1].append('.')

    return new_maze


def find_start(maze):
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == 'S':
                return x, y


def flood_fill(maze, y, x, char='O'):
    maze[y][x] = char
    try:
        if maze[y][x - 1] == '.':
            flood_fill(maze, y, x - 1, char)
    except IndexError:
        pass
    try:
        if maze[y][x + 1] == '.':
            flood_fill(maze, y, x + 1, char)
    except IndexError:
        pass
    try:
        if maze[y - 1][x] == '.':
            flood_fill(maze, y - 1, x, char)
    except IndexError:
        pass
    try:
        if maze[y + 1][x] == '.':
            flood_fill(maze, y + 1, x, char)
    except IndexError:
        pass


def find_area_inside(maze):
    maze = wrap(maze)
    start = find_start(maze)

    x, y = start
    path = []

    a_side_tiles = []
    b_side_tiles = []
    sides_map = [['.' for char in range(len(maze[0]))] for line in range(len(maze))]

    # print_maze(sides_map)

    if maze[y][x - 1] in ['F', 'L', '-']:
        direction = 'left'
    elif maze[y][x + 1] in ['J', '7', '-']:
        direction = 'right'
    elif maze[y - 1][x] in ['7', 'F', '|']:
        direction = 'up'
    elif maze[y + 1][x] in ['J', 'L', '|']:
        direction = 'down'
    else:
        raise NotImplemented

    # trace the pipe
    while (x, y) not in path:
        path.append((x, y, direction))
        sides_map[y][x] = 'X'

        if direction.split('-')[-1] == 'right':
            x = x + 1
            pipe = maze[y][x]
            if pipe == 'J':
                direction = 'right-up'
            elif pipe == '7':
                direction = 'right-down'
            elif pipe == '-':
                continue
            else:
                break
        elif direction.split('-')[-1] == 'left':
            x = x - 1
            pipe = maze[y][x]
            if pipe == 'L':
                direction = 'left-up'
            elif pipe == 'F':
                direction = 'left-down'
            elif pipe == '-':
                continue
            else:
                break
        elif direction.split('-')[-1] == 'up':
            y = y - 1
            pipe = maze[y][x]
            if pipe == '7':
                direction = 'up-left'
            elif pipe == 'F':
                direction = 'up-right'
            elif pipe == '|':
                continue
            else:
                break
        elif direction.split('-')[-1] == 'down':
            y = y + 1
            pipe = maze[y][x]
            if pipe == 'J':
                direction = 'down-left'
            elif pipe == 'L':
                direction = 'down-right'
            elif pipe == '|':
                continue
            else:
                break

    # assign A/B to tiles on the sides of path tiles
    for (x, y, direction) in path:
        if 'right' in direction:
            if sides_map[y + 1][x] != 'X':
                sides_map[y + 1][x] = 'B'
                b_side_tiles.append((x, y + 1))
            if sides_map[y - 1][x] != 'X':
                sides_map[y - 1][x] = 'A'
                a_side_tiles.append((x, y - 1))
        elif 'left' in direction:
            if sides_map[y + 1][x] != 'X':
                sides_map[y + 1][x] = 'A'
                a_side_tiles.append((x, y + 1))
            if sides_map[y - 1][x] != 'X':
                sides_map[y - 1][x] = 'B'
                b_side_tiles.append((x, y - 1))
        elif 'up' in direction:
            if sides_map[y][x + 1] != 'X':
                sides_map[y][x + 1] = 'B'
                b_side_tiles.append((x + 1, y))
            if sides_map[y][x - 1] != 'X':
                sides_map[y][x - 1] = 'A'
                a_side_tiles.append((x - 1, y))
        elif 'down' in direction:
            if sides_map[y][x + 1] != 'X':
                sides_map[y][x + 1] = 'A'
                a_side_tiles.append((x + 1, y))
            if sides_map[y][x - 1] != 'X':
                sides_map[y][x - 1] = 'B'
                b_side_tiles.append((x - 1, y))

    # flood-fill each of the tiles in both sides
    for x, y in a_side_tiles:
        flood_fill(sides_map, y, x, 'A')
    for x, y in b_side_tiles:
        flood_fill(sides_map, y, x, 'B')

    # print_maze(sides_map)

    a_count = 0
    b_count = 0
    for line in sides_map:
        for char in line:
            if char == 'A':
                a_count += 1
            elif char == 'B':
                b_count += 1

    return min(a_count, b_count)


def main():
    test_1 = find_area_inside(test_input_1)
    print('test_1:', test_1)

    test_2 = find_area_inside(test_input_2)
    print('test_2:', test_2)

    test_3 = find_area_inside(test_input_3)
    print('test_3:', test_3)

    start = time()
    answer = find_area_inside(pipe_maze)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# answer:   285
# time:     1.1379570960998535 s
