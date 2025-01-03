from time import time

test_input_1 = '''
.....
.S-7.
.|.|.
.L-J.
.....
'''

test_input_2 = '''
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
'''

pipe_maze = ''

with open("data.txt") as file:
    for _line in file.readlines():
        pipe_maze += _line


def wrap(maze):
    maze = maze.split()

    new_maze = ['.' * (len(maze[0]) + 2)]
    for line in maze:
        new_maze.append('.' + str(line.split()[0]) + '.')
    new_maze.append('.' * (len(maze[0]) + 2))

    return new_maze


def find_start(maze):
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == 'S':
                return x, y


def find_path(maze):
    maze = wrap(maze)
    start = find_start(maze)

    x, y = start
    path = []

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
        path.append((x, y))

        if direction == 'right':
            x = x + 1
            pipe = maze[y][x]
            if pipe == 'J':
                direction = 'up'
            elif pipe == '7':
                direction = 'down'
            elif pipe == '-':
                continue
            else:
                break
        elif direction == 'left':
            x = x - 1
            pipe = maze[y][x]
            if pipe == 'L':
                direction = 'up'
            elif pipe == 'F':
                direction = 'down'
            elif pipe == '-':
                continue
            else:
                break
        elif direction == 'up':
            y = y - 1
            pipe = maze[y][x]
            if pipe == '7':
                direction = 'left'
            elif pipe == 'F':
                direction = 'right'
            elif pipe == '|':
                continue
            else:
                break
        elif direction == 'down':
            y = y + 1
            pipe = maze[y][x]
            if pipe == 'J':
                direction = 'left'
            elif pipe == 'L':
                direction = 'right'
            elif pipe == '|':
                continue
            else:
                break
    # print(path)

    return int(len(path) / 2)


def main():
    test_1 = find_path(test_input_1)
    print('test_1:', test_1)

    test_2 = find_path(test_input_2)
    print('test_2:', test_2)

    start = time()
    answer = find_path(pipe_maze)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# answer:   7030
# time:     1.50201416015625 s
