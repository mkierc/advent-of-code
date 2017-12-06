test_input_1 = [0, 2, 7, 0]

input_data = []

with open("data.txt") as file:
    input_chars = file.read().split()
    for char in input_chars:
        input_data.append(int(char))


def solve(data):
    cycles = 0
    seen_configurations = [[data, cycles]]
    current_config = data
    while True:
        cycles += 1
        current_config = distribute(list(current_config), find_max_pos(list(current_config)))

        if current_config not in list(zip(*seen_configurations))[0]:
            seen_configurations.append([current_config, cycles])
        else:
            return cycles - find_position_in_list(seen_configurations, current_config)


def find_position_in_list(list, position):
    for pos in list:
        if pos[0] == position:
            return pos[1]


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
    return data


def main():
    test_1 = solve(test_input_1)
    answer = solve(input_data)

    print("test_1:", test_1)
    print("answer:", answer)


if __name__ == "__main__":
    main()
