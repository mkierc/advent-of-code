test_input_1 = [
    [5, 10, 25],
    [3, 4, 5],
    [3, 2, 1]
]

with open("data.txt") as file:
    input_data = []
    for line in file.readlines():
        a, b, c = line.rsplit()
        input_data.append([int(a), int(b), int(c)])


def count_triangles(triangles):
    triangle_count = 0

    for sides in triangles:
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            triangle_count += 1

    return triangle_count


def main():
    test_1 = count_triangles(test_input_1)
    print("test_1:", test_1)

    answer = count_triangles(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
