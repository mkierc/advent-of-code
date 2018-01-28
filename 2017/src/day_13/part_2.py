import re

import time

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


def find_delay(firewall):
    packet_positions = {}
    current_delay = 0
    while True:
        # add new packet
        packet_positions.update({current_delay: 0})

        # check if there are survivors at the end of firewall
        for position in packet_positions.keys():
            if packet_positions.get(position) == len(firewall):
                return position

        # check whether any of packets was caught...
        to_delete = set()
        for position in packet_positions.keys():
            if firewall[packet_positions.get(position)][1] == 0:
                to_delete.add(position)

        # ...and remove them from the dict
        for position in to_delete:
            del packet_positions[position]

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

        # move packets
        for packet in packet_positions:
            value = packet_positions.get(packet)
            packet_positions[packet] = value + 1

        current_delay += 1


def solve(data):
    # build firewall
    length = max(data.keys()) + 1
    firewall = [[0, -1, 'X'] for _ in range(length)]
    for layer in data.keys():
        firewall[layer] = data.get(layer)

    return find_delay(firewall)


def main():
    test_1 = solve(test_input_1)
    print("test_1:", test_1)

    # Intel Core i7 7700k
    # 52.0704 s - Unoptimized
    start = time.time()
    answer = solve(input_data)
    print("time:", time.time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()
