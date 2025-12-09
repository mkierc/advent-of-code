from math import sqrt
from time import time

test_boxes = [
    (162, 817, 812),
    (57, 618, 57),
    (906, 360, 560),
    (592, 479, 940),
    (352, 342, 300),
    (466, 668, 158),
    (542, 29, 236),
    (431, 825, 988),
    (739, 650, 466),
    (52, 470, 668),
    (216, 146, 977),
    (819, 987, 18),
    (117, 168, 530),
    (805, 96, 715),
    (346, 949, 466),
    (970, 615, 88),
    (941, 993, 340),
    (862, 61, 35),
    (984, 92, 344),
    (425, 690, 689),
]

boxes = []

with open('data.txt') as file:
    input_data = file.read().split()
    for line in input_data:
        x, y, z = line.split(',')
        boxes.append((int(x), int(y), int(z)))


def distance(x1, y1, z1, x2, y2, z2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def solve(box_list):
    distances = {}

    for x1, y1, z1 in box_list:
        for x2, y2, z2 in box_list:
            if x1 != x2 and y1 != y2 and z1 != z2:
                if x1 < x2:
                    distances[(x1, y1, z1), (x2, y2, z2)] = distance(x1, y1, z1, x2, y2, z2)
                elif x1 > x2:
                    distances[(x2, y2, z2), (x1, y1, z1)] = distance(x1, y1, z1, x2, y2, z2)
                elif y1 < y2:
                    distances[(x1, y1, z1), (x2, y2, z2)] = distance(x1, y1, z1, x2, y2, z2)
                elif y1 > y2:
                    distances[(x2, y2, z2), (x1, y1, z1)] = distance(x1, y1, z1, x2, y2, z2)
                elif z1 < z2:
                    distances[(x1, y1, z1), (x2, y2, z2)] = distance(x1, y1, z1, x2, y2, z2)
                else:
                    distances[(x2, y2, z2), (x1, y1, z1)] = distance(x1, y1, z1, x2, y2, z2)

    circuits = []

    for k, v in sorted(distances.items(), key=lambda x: x[1]):
        # pprint(circuits)
        # print(k, v)

        in_circuit = []

        for i, circuit in enumerate(circuits):
            if circuit & set(k):
                in_circuit.append(i)

        if not in_circuit:
            circuits.append({k[0], k[1]})
        elif len(in_circuit) == 1:
            circuits[in_circuit[0]].add(k[0])
            circuits[in_circuit[0]].add(k[1])
        else:
            circuits[in_circuit[0]] = circuits[in_circuit[0]] | circuits.pop(in_circuit[1])

        if len(circuits[0]) == len(box_list):
            # print(k)
            return k[0][0] * k[1][0]



def main():
    test_1 = solve(test_boxes)
    print('test_1:', test_1)

    start = time()
    answer = solve(boxes)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
