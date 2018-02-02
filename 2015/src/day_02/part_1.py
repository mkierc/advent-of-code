test_input_1 = (2, 3, 4)
test_input_2 = (1, 1, 10)

with open('data.txt') as file:
    input_data = []
    for line in file.read().splitlines():
        a, b, c = line.split('x')
        input_data.append((int(a), int(b), int(c)))


def find_area(w, l, h):
    a = 2 * w * l
    b = 2 * l * h
    c = 2 * h * w
    slack = min((a, b, c)) // 2

    return a + b + c + slack


def find_total_area(sizes):
    total_area = 0

    for box in sizes:
        total_area += find_area(*box)

    return total_area


def main():
    test_1 = find_area(*test_input_1)
    print('test_1:', test_1)
    test_2 = find_area(*test_input_2)
    print('test_2:', test_2)

    answer = find_total_area(input_data)
    print('answer:', answer)


if __name__ == '__main__':
    main()
