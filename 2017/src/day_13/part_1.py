import re

test_input_1 = {
    0: [3, 0, 'u'],
    1: [2, 0, 'u'],
    4: [4, 0, 'u'],
    6: [4, 0, 'u']
}

input_data = {}

with open("data.txt") as file:
    for line in file.read().split('\n'):
        regex = re.search('(\d+): (\d+)', line)
        input_data.update({int(regex.group(1)): [int(regex.group(2)), 0, 'u']})


def calculate_severity(data):
    # build firewall
    length = max(data.keys()) + 1
    firewall = [[0, -1, 'X'] for x in range(length)]
    for layer in data.keys():
        firewall[layer] = data.get(layer)

    packet_position = 0
    severity = 0

    while packet_position < length:
        # check whether you're caught and calculate severity
        if firewall[packet_position][1] == 0:
            severity += packet_position * firewall[packet_position][0]

        # move scanners
        for scanner in firewall:
            wall_size = scanner[0]
            scanner_position = scanner[1]
            direction = scanner[2]
            if wall_size > 0:
                if direction == 'u':
                    if scanner_position == wall_size - 1:
                        scanner[2] = 'd'
                        scanner[1] -= 1
                    else:
                        scanner[1] += 1
                else:  # direction == 'd'
                    if scanner_position == 0:
                        scanner[2] = 'u'
                        scanner[1] += 1
                    else:
                        scanner[1] -= 1
        packet_position += 1

    return severity


def main():
    test_1 = calculate_severity(test_input_1)
    print("test_1:", test_1)

    answer = calculate_severity(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
