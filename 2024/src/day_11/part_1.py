from time import time

test_list_1 = [125, 17]
test_list_2 = [0, 1, 10, 99, 999]

with open("data.txt") as file:
    data = [int(_) for _ in file.readline().split()]


def blink(stone_list):
    new_stones = []
    for stone in stone_list:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            left, right = int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(stone*2024)
    return new_stones


def count_stones(stone_list, turns):
    for turn in range(turns):
        stone_list = blink(stone_list)
        # print(stone_list)
    return len(stone_list)


def main():
    test_1 = count_stones(test_list_1, 25)
    print("test_1:", test_1)

    test_2 = count_stones(test_list_2, 6)
    print("test_2:", test_2)

    test_2 = count_stones(test_list_2, 25)
    print("test_2:", test_2)

    start = time()
    answer = count_stones(data, 25)
    print('time:', time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()

# answer: 186203
# time:   0.1814866065979004 s
