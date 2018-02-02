test_input_1 = (2, 3, 4)
test_input_2 = (1, 1, 10)

with open('data.txt') as file:
    input_data = []
    for line in file.read().splitlines():
        a, b, c = line.split('x')
        input_data.append((int(a), int(b), int(c)))


def find_length(w, l, h):
    sides = sorted((w, l, h))
    perimeter = 2 * (sides[0] + sides[1])
    volume = w * l * h

    return perimeter + volume


def find_total_length(sizes):
    total_length = 0

    for box in sizes:
        total_length += find_length(*box)

    return total_length


def main():
    test_1 = find_length(*test_input_1)
    print('test_1:', test_1)
    test_2 = find_length(*test_input_2)
    print('test_2:', test_2)

    answer = find_total_length(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
