from time import time

test_tiles = [
    (7, 1),
    (11, 1),
    (11, 7),
    (9, 7),
    (9, 5),
    (2, 5),
    (2, 3),
    (7, 3),
]

tiles = []

with open('data.txt') as file:
    input_data = file.read().split()
    for line in input_data:
        x, y = line.split(',')
        tiles.append((int(x), int(y)))


def size(x1, y1, x2, y2):
    width = max(x1, x2) - min(x1, x2) + 1
    height = max(y1, y2) - min(y1, y2) + 1
    return width * height


def solve(tile_list):
    max_area = 0

    for x1, y1 in tile_list:
        for x2, y2 in tile_list:
            if x1 != x2 and y1 != y2:
                area = size(x1, y1, x2, y2)
                # print(x1, y1, x2, y2, area)
                if area > max_area:
                    max_area = area


    return max_area


def main():
    test_1 = solve(test_tiles)
    print('test_1:', test_1)

    start = time()
    answer = solve(tiles)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
