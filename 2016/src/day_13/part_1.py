MAZE_WIDTH = 60
MAZE_HEIGHT = 60
OFFICERS_NUMBER = 1350
DESTINATION = (31, 39)
MAX_DEPTH = 150


def generate_maze():
    maze = []
    for y in range(MAZE_HEIGHT):
        line = []
        for x in range(MAZE_WIDTH):
            number = bin(x * x + 3 * x + 2 * x * y + y + y * y + OFFICERS_NUMBER)
            if number.count("1") % 2 == 0:
                line.append(".")
            else:
                line.append("#")
        maze.append(line)
    return maze


def find_path(depth: int, position: tuple, maze: list):
    # simple recursive DFS pathfinding
    if depth < MAX_DEPTH:
        maze[position[1]][position[0]] = depth
        depth += 1
        for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_x = position[0] + direction[0]
            new_y = position[1] + direction[1]
            new_position = (new_x, new_y)
            if MAZE_WIDTH > new_x >= 0 and MAZE_HEIGHT > new_y >= 0:
                if maze[new_y][new_x] == ".":
                    find_path(depth, new_position, maze)
                elif type(maze[new_y][new_x]) == int and maze[new_y][new_x] >= depth:
                    find_path(depth, new_position, maze)


def main():
    maze = generate_maze()
    find_path(0, (1, 1), maze)

    answer = maze[DESTINATION[1]][DESTINATION[0]]
    print("answer:", answer)

if __name__ == "__main__":
    main()
