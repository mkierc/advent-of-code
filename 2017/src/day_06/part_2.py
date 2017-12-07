import time

with open("data.txt") as file:
    input_data = tuple(int(char) for char in file.read().split())


def solve(data):
    cycles = 0
    visited_states = {data: cycles}
    current_config = data
    while True:
        cycles += 1
        current_config = distribute(list(current_config))

        if current_config not in visited_states.keys():
            visited_states.update({current_config: cycles})
        else:
            return cycles - visited_states.get(current_config)


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
    # 9.61188 s - Unoptimized
    # 8.34519 s - Tuples instead of lists
    # 8.25261 s - Built-in index/max instead of custom
    # 8.22655 s - Constant list size for modulo
    # 0.04410 s - Dictionary instead of list of lists
    start = time.time()
    answer = solve(input_data)
    print("time:", time.time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()
