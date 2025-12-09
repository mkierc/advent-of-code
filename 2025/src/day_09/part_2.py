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


def find_edges(vertex_list):
    edges = []

    x1, y1 = vertex_list[0][0], vertex_list[0][1]
    for x2, y2 in vertex_list[1:]:
        edges.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
        x1, y1 = x2, y2

    # wrap around the last vertex to first, to form a cycle
    x1, y1 = vertex_list[0][0], vertex_list[0][1]
    x2, y2 = vertex_list[-1][0], vertex_list[-1][1]
    edges.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    return edges


def solve(tile_list):
    edges = find_edges(tile_list)
    # print(edges)
    # print(tile_list)

    max_area = 0
    max_enclosed_area = 0

    for a, b in tile_list:
        for c, d in tile_list:
            if a != c and b != d:
                x1, y1, x2, y2 = (min(a, c), min(b, d), max(a, c), max(b, d))
                area = size(x1, y1, x2, y2)

                if area > max_area:
                    max_area = area
                    # print(area, max_area, max_enclosed_area, (x1, y1, x2, y2))

                if area > max_enclosed_area:
                    edge_crossed = False
                    for e1, f1, e2, f2 in edges:
                        # if any edge of the polygon cuts through a side of rectangle don't consider the area
                        if e1 < x2 and f1 < y2 and e2 > x1 and f2 > y1:
                            edge_crossed = True
                            break

                    if not edge_crossed:
                        max_enclosed_area = area
                        # print(area, max_area, max_enclosed_area, (x1, y1, x2, y2), (e1, f1, e2, f2))

    return max_enclosed_area


def main():
    test_1 = solve(test_tiles)
    print('test_1:', test_1)

    start = time()
    answer = solve(tiles)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
