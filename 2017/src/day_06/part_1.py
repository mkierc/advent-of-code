import time

test_input_1 = [0, 2, 7, 0]

with open("data.txt") as file:
    input_data = tuple(int(char) for char in file.read().split())


def solve(data):
    cycles = 0
    seen_configurations = set(data)
    current_config = data
    while True:
        cycles += 1
        current_config = distribute(list(current_config), find_max_pos(list(current_config)))

        if current_config not in seen_configurations:
            seen_configurations.add(current_config)
        else:
            return cycles


def find_max_pos(data):
    max_value = 0
    position = 0
    for i in range(len(data)):
        if data[i] > max_value:
            max_value = data[i]
            position = i
    return position


def distribute(data, source_position):
    buffer = data[source_position]
    data[source_position] = 0
    while buffer > 0:
        source_position = (source_position + 1) % len(data)
        data[source_position] += 1
        buffer -= 1
    return tuple(data)


def main():
    test_1 = solve(test_input_1)

    # Intel Core i7 4770:
    # 2.363 s - unoptimized, using list of lists
    # 0.073 s - optimized, using dict with tuples as keys
    start = time.time()
    answer = solve(input_data)
    print("time:", time.time() - start)

    print("test_1:", test_1)
    print("answer:", answer)


if __name__ == "__main__":
    main()
