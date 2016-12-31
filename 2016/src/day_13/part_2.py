from day_13.part_1 import MAZE_WIDTH
from day_13.part_1 import MAZE_HEIGHT
from day_13.part_1 import generate_maze
from day_13.part_1 import find_path


def main():
    maze = generate_maze()
    find_path(0, (1, 1), maze)

    location_sum = 0
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if type(maze[y][x]) == int and maze[y][x] <= 50:
                location_sum += 1

    print("answer:", location_sum)

if __name__ == "__main__":
    main()
