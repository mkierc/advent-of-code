from collections import defaultdict
from time import time

test_list_1 = [125, 17]
test_list_2 = [0, 1, 10, 99, 999]

with open("data.txt") as file:
    data = [int(_) for _ in file.readline().split()]


def blink(stone_map):
    new_stones = defaultdict(int)

    for stone, count in stone_map.items():
        if stone == 0:
            new_stones.update({1: new_stones[1] + count})
        elif len(str(stone)) % 2 == 0:
            left, right = int(str(stone)[:len(str(stone)) // 2]), int(str(stone)[len(str(stone)) // 2:])

            new_stones.update({left: new_stones[left] + count})
            new_stones.update({right: new_stones[right] + count})
        else:
            new_stones.update({stone * 2024: new_stones[stone * 2024] + count})
    return new_stones


def count_stones(stone_list, turns):
    stone_map = defaultdict(int)
    for stone in stone_list:
        stone_map.update({stone: stone_map[stone] + 1})

    for turn in range(turns):
        stone_map = blink(stone_map)
        # print(stone_list)
    return sum(stone_map.values())


def main():
    test_1 = count_stones(test_list_1, 25)
    print("test_1:", test_1)

    start = time()
    answer = count_stones(data, 75)
    print('time:', time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()

# answer: 221291560078593
# time:   0.11771202087402344 s

# todo: compare against memoized
