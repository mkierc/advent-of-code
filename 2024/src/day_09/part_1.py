from time import time

test_list = [int(_) for _ in '2333133121414131402']

with open("data.txt") as file:
    data = [int(_) for _ in file.readline()]


def calculate_checksum(disk_map):
    blocks = []
    spaces = []

    for i, num in enumerate(disk_map):
        if i % 2 == 0:
            blocks.append(num)
        else:
            spaces.append(num)

    checksum = 0

    block_index = 0
    reverse_block_index = len(blocks) - 1
    space_index = 0
    disk_index = 0

    filling_spaces = False

    disk = []

    while block_index < len(blocks) - 1 and reverse_block_index > 0:
        # print(blocks, spaces, disk)
        if not filling_spaces:
            if blocks[block_index] > 0:
                blocks[block_index] = blocks[block_index] - 1
                checksum += block_index * disk_index
                # disk.append(block_index)
                disk_index += 1
            else:
                block_index += 1
                filling_spaces = True
        else:
            if spaces[space_index] > 0:
                if blocks[reverse_block_index] > 0:
                    spaces[space_index] = spaces[space_index] - 1
                    blocks[reverse_block_index] = blocks[reverse_block_index] - 1
                    checksum += reverse_block_index * disk_index
                    # disk.append(reverse_block_index)
                    disk_index += 1
                else:
                    reverse_block_index -= 1
            else:
                space_index += 1
                filling_spaces = False

    return checksum


def main():
    test = calculate_checksum(test_list)
    print("test:", test)

    start = time()
    answer = calculate_checksum(data)
    print('time:', time() - start)
    print("answer:", answer)


if __name__ == "__main__":
    main()


# answer: 6399153661894
# without actual writes to disk        0.011967897415161133 s
# todo: compare to unoptimized version with actual writes to disk array
