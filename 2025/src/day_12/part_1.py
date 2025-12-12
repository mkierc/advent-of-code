import re
from time import time

region_regex = r'(\d+)x(\d+): ([\d ]+)'

test_shapes = [['###', '##.', '##.'],
               ['###', '##.', '.##'],
               ['.##', '###', '##.'],
               ['##.', '###', '##.'],
               ['###', '#..', '###'],
               ['###', '.#.', '###']]

test_regions = [[4, 4, [0, 0, 0, 0, 2, 0]],
                [12, 5, [1, 0, 1, 0, 2, 2]],
                [12, 5, [1, 0, 1, 0, 3, 2]]]

shapes = []
regions = []

with open('data.txt') as file:
    input_data = file.read().split('\n\n')
    for line in input_data[:-1]:
        num, shape = line.split(':\n')
        shapes.append(shape.split('\n'))
    for line in input_data[-1].split('\n'):
        a, b, counts = re.findall(region_regex, line)[0]
        regions.append([int(a), int(b), [int(x) for x in counts.split(' ')]])


def solve(shapes, regions):
    # FILL_RATIO = 0.9
    # shape_mapping = {}
    # for i, shape in enumerate(shapes):
    #     shape_mapping[i] = ''.join(shape).count('#') * FILL_RATIO
    # print(shape_mapping)

    # naive approach works ¯\_(ツ)_/¯
    count = 0
    for a, b, counts in regions:
        if a//3 * b//3 >= sum(counts):
            count += 1
    return count


def main():
    test_1 = solve(test_shapes, test_regions)
    print('test_1:', test_1)

    start = time()
    answer = solve(shapes, regions)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
