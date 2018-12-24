import time

test_input = [
    (0, 2),
    (2, 2),
    (2, 3),
    (3, 4),
    (3, 5),
    (0, 1),
    (10, 1),
    (9, 10)
]

with open('data.txt', 'r') as file:
    input_data = []
    for line in file.read().splitlines():
        a, b = (int(x) for x in line.split('/'))
        input_data.append((a, b))


def generate_bridges(previous_bridge, previous_end, previous_components):

    # filter out components that don't have the compatible end type
    compatible_components = []

    for component in previous_components:
        if previous_end in component:
            compatible_components.append(component)

    # if there are no available components left, just return the previous bridge and it's end type
    if not compatible_components:
        return [(previous_bridge, previous_end)]

    # if there *are* compatible components, generate new bridges using those components
    bridge_list = []

    for component in compatible_components:
        # remove the component we used from available components list
        available_components = previous_components.copy()
        available_components.remove(component)

        # find which end of component matches the previous bridge end
        if previous_end == component[1]:
            current_end = component[0]
        else:
            current_end = component[1]

        # create a new bridge
        current_bridge = previous_bridge + [component]

        # recursively find bridges extending the current one
        for bridge in generate_bridges(current_bridge, current_end, available_components):
            bridge_list.append(bridge)

    return bridge_list


def find_longest(component_list):
    bridge_list = generate_bridges([], 0, component_list)

    max_length = 0
    longest_bridges = []

    for bridge, _ in bridge_list:
        length = len(bridge)
        if length >= max_length:
            max_length = length

    for bridge, _ in bridge_list:
        if len(bridge) == max_length:
            longest_bridges.append(bridge)

    max_strength = 0

    for bridge in longest_bridges:
        strength = 0
        for component in bridge:
            strength += component[0]
            strength += component[1]
        if strength > max_strength:
            max_strength = strength

    return max_strength


def main():
    test_1 = find_longest(test_input)
    print("test_1:", test_1)

    start = time.time()
    answer = find_longest(input_data)
    print("time:", (time.time() - start))
    print("answer:", answer)


if __name__ == "__main__":
    main()
