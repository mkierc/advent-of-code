test_input_1 = 1
test_input_2 = 12
test_input_3 = 23
test_input_4 = 1024

input_data = 361527


# TODO - solution is wonky, needs refactoring
def do_the_thing(n):
    if n == 1:
        return 0

    level = 1
    level_range = (level*2+1)**2

    while n > level_range:
        level += 1
        level_range = (level * 2 + 1) ** 2

    min = level
    max = level * 2

    i = level_range
    distance = max

    print(n, level, min, max)

    if n == level_range:
        return max

    direction = 'down'

    while i != n:
        if direction == 'down':
            distance -= 1
        else:
            distance += 1
        if distance == min:
            direction = 'up'
        if distance == max:
            direction = 'down'
        i -= 1
        print(i, distance)

    return distance


def main():
    test_1 = do_the_thing(test_input_1)
    print("test_1:", test_1)
    test_2 = do_the_thing(test_input_2)
    print("test_2:", test_2)
    test_3 = do_the_thing(test_input_3)
    print("test_3:", test_3)
    test_4 = do_the_thing(test_input_4)
    print("test_4:", test_4)

    answer = do_the_thing(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
