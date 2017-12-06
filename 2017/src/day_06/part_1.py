import time

with open("data.txt") as file:
    input_data = tuple(int(char) for char in file.read().split())


def solve(data):
    cycles = 0
    visited_states = set(data)
    current_config = data
    while True:
        cycles += 1
        current_config = distribute(list(current_config))

        if current_config not in visited_states:
            visited_states.add(current_config)
        else:
            return cycles


def distribute(data):
    source_position = data.index(max(data))
    buffer = data[source_position]
    data[source_position] = 0
    while buffer > 0:
        source_position = (source_position + 1) % 16
        data[source_position] += 1
        buffer -= 1
    return tuple(data)


def main():
    # Intel Core i7 7700k
    # 1.79378 s - Unoptimized
    # 1.68781 s - Tuples instead of lists
    # 1.63569 s - Built-in index/max instead of custom
    # 1.62464 s - Constant list size for modulo
    # 0.04077 s - Set instead of list of lists
    start = time.time()
    answer = solve(input_data)
    print("time:", time.time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()
